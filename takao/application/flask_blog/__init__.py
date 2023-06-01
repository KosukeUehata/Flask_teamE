# アプリケーション本体ファイル
from flask import Flask

app = Flask(__name__) # Flaskのアプリケーション本体を作成

import flask_blog.views