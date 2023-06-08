from flask_script import Command
from portal import db
# from portal.models.notice import Notice
from portal.models.reserve import Reserve

class InitDB(Command):
    "create database"
    def run(self):
        db.create_all()
    