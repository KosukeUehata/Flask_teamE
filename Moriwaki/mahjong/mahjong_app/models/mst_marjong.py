from mahjong_app import db


class DB_list(db.Model):
    __tablename__ = 'mahjong'
    num = db.Column('num', db.Integer(), autoincrement = True, primary_key = True)
    player1 = db.Column('player_1', db.String(10))
    point1 = db.Column('point_1', db.Integer())  
    player2 = db.Column('player_2', db.String(10))
    point2 = db.Column('point_2', db.Integer())
    player3 = db.Column('player_3', db.String(10))
    point3 = db.Column('point_3', db.Integer())
    player4 = db.Column('player_4', db.String(10))
    point4 = db.Column('point_4', db.Integer())

    def __init__(self, player1=None, point1=None, player2=None, point2=None, player3=None, point3=None, player4=None, point4=None):
        self.player1 = player1
        self.point1 = point1
        self.player2 = player2
        self.point2 = point2
        self.player3 = player3
        self.point3 = point3
        self.player4 = player4
        self.point4 = point4

