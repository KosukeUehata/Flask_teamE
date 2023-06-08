from portal import db

class Reserve(db.Model):
    __tablename__ = "reserve"
    room_id = db.Column(db.Integer,primary_key=True)
    type = db.Column(db.String(10),primary_key=True)
    day = db.Column(db.Date ,primary_key=True)
    index = db.Column(db.Integer, nullable=False)
    
    def __init__(self, room_id=None, type=None, day=None, index=None):
        self.room_id = room_id
        self.type = type 
        self.day = day
        self.index = index        
    
    def __repr__(self):
        return '<Reserve room_id:{} type:{} day:{} index:{}>'.format(self.room_id, self.type, self.day, self.index)
        
        