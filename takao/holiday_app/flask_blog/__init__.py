# アプリケーション本体ファイル
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # Flaskのアプリケーション本体を作成
app.config.from_object('flask_blog.config')

db = SQLAlchemy(app)

from flask_blog.views import views, entries