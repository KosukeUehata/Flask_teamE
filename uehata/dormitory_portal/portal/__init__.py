from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("portal.config")

db = SQLAlchemy(app)

from portal.views import views