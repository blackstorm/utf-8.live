from app import db

class Box(db.Model):
    __tablename__ = 'box'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120))
    content = db.Column(db.Text)
    type = db.Column(db.Text)
    order = db.Column(db.Integer)

    def __init__(self, name, content, type, order):
        self.content = content
        self.name = name
        self.type = type
        self.order = order

    def __repr__(self):
        return '<Post Title:%r>' % self.name