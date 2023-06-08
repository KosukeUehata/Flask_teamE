from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('mahjong_app.config')

db = SQLAlchemy(app)

from mahjong_app.views import views
