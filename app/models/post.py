from app import db

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(120))
    content = db.Column(db.Text)
    created = db.Column(db.DateTime, default=db.func.now())

    def __init__(self,title, content, created):
        self.title = title
        self.content = content
        self.created = created

    def __repr__(self):
        return '<Post Title:%r>' % self.title