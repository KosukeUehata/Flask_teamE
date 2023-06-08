from portal import db
from datetime import datetime

class Notice(db.Model):
    __tablename__ = "notice"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime)
    
    def __init__(self, id=None, title=None, content=None):
        self.id = id
        self.title = title
        self.content = content
        self.created_at = datetime.utcnow()
        
    
    def __repr__(self):
        return '<Notice id:{} title:{} content:{}>'.format(self.id, self.title, self.content)
        
        