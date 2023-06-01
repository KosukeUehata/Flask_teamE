# ビューファイル
from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app # __init__.pyで作成したappをインポート

@app.route('/') # urlにアクセスがあった際の処理(アクセスがあったら、show_entries()というメゾットが呼び出される)
def show_entries():
    return render_template('entries/index.html') 