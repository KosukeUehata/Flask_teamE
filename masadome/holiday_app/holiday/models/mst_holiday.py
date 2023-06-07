from datetime import datetime
from holiday import db

class Holiday(db.Model):
    __tablename__ = 'holiday'
    holi_date = db.Column(db.DateTime, primary_key=True)
    holi_text = db.Column(db.Text)

    def __init__(self, holidate, holitext):
        self.holi_date = datetime.strptime(holidate, '%Y-%m-%d')
        self.holi_text = holitext