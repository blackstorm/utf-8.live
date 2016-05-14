from datetime import datetime
from app import app
from flask import render_template, request, session, redirect, url_for
from app.models.post import Post
from app.models.box import Box
from app.config import POSTS_PER_PAGE
from app import validator
from app import db
import markdown2
from app.auth import login_required

#页面
@app.route('/', methods=['GET'])
@app.route('/page/<int:page>', methods=['GET'])
def index(page = 1):
    # 分页查询
    pagination = Post.query.order_by(Post.id.desc()).paginate(page, per_page = POSTS_PER_PAGE, error_out = False)
    items = pagination.items
    index_boxs = Box.query.filter_by(type="index")
    if len(items) < 1:
        return render_template('404.html'), 404
    return render_template("index.html",
                           title = "主页",
                           posts = items,
                           boxs = index_boxs,
                           total = pagination.total,
                           page = pagination.page,
                           per_page = pagination.per_page)

# 文章
@app.route("/post/<int:postid>", methods = ['GET'])
def post(postid = 1):
    post = Post.query.filter_by(id = postid).first()

    if post == None:
        return render_template('404.html'), 404

    return render_template("post.html", post = post)


# 登录
@app.route("/login", methods = ['POST','GET'])
def login():
    if request.method == "POST":
        username = request.form['name']
        password = request.form['password']
        if username == '' or password == '':
            return render_template("login.html",
                                   message = "用户名或密码为空")
        if validator.user_login(username,password) == False:
            return render_template("login.html",
                                   message = "用户名或密码错误")
        session['user'] = username
        return redirect(url_for('index'))
    return render_template("login.html")

# 退出
@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('user', None)
    return redirect(url_for('index'))


# 发布
@app.route("/markdown", methods = ['POST','GET'])
@login_required
def markdown():
    if request.method == "GET":
        return render_template("markdown.html")
    title = request.form['title']
    content = request.form['content']
    if title == '' or content == '':
        return render_template("markdown.html",
                               messgae = "请填写标题和正文")
    post = Post(title, markdown2.markdown(content),datetime.now())
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('index'))


#更新文章
@app.route("/markdown/update/<int:postid>", methods = ['POST','GET'])
@login_required
def post_edit(postid = 1):
    if request.method == "GET":
        post = Post.query.filter_by(id=postid).first()
        return render_template("markdown_edit.html",
                               post = post)
    title = request.form['title']
    content = request.form['content']
    if title == '' or content == '':
        post = Post.query.filter_by(id=postid).first()
        return render_template("markdown_edit.html",
                               post = post,
                               messgae = "没有填写完善")
    db.session.query(Post).filter(Post.id == postid).update({Post.title: title,
                                                       Post.content: markdown2.markdown(content)})
    db.session.commit()
    return redirect(url_for('post', postid = postid))


# 获取
@app.route("/box",methods = ['GET','POST'])
@login_required
def box():
    if request.method == "POST":
        type = request.form['type']
        name = request.form['name']
        order = request.form['order']
        content = markdown2.markdown(request.form['content'])
        if type == '' or name == '' or order == '' or content == '':
            return render_template("box.html",message = "请填写完整信息")
        box = Box(name, content, type, order)
        db.session.add(box)
        db.session.commit()
        redirect(url_for('box'))
    boxs = Box.query.all()
    return render_template("box.html",
                           boxs = boxs)

# 修改BOX
@app.route("/box/update",methods = ['POST'])
@login_required
def box_update():
    id = int(request.form['id'])
    name = request.form['name']
    content = request.form['content']
    type = request.form['type']
    order = int(request.form['order'])
    db.session.query(Box).filter(Box.id == id).update({Box.name:name,
                                                       Box.content:content,
                                                       Box.name:name,
                                                       Box.type:type})
    db.session.commit()
    return redirect(url_for('box'))

@app.route("/box/del/<int:id>",methods = ['GET'])
@login_required
def box_del(id = 1):
    db.session.query(Box).filter(Box.id == id).delete()
    db.session.commit()
    return redirect(url_for('box'))

# 404 页面
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404