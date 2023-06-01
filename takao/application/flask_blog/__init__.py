# アプリケーション本体ファイル
from flask import Flask

app = Flask(__name__) # Flaskのアプリケーション本体を作成
app.config.from_object('flask_blog.config')

import flask_blog.views