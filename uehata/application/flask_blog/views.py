from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app

# cookieのsession情報がTrueの場合はログイン画面にリダイレクトする
@app.route("/")
def show_entries():
    if not session.get("logged_in"):
        return redirect("/login")
    return render_template("entries/index.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":
        if request.form["username"] != app.config["USERNAME"]:
            # print("ユーザ名が異なります")
            flash("ユーザ名が異なります")
        elif request.form["password"] != app.config["PASSWORD"]:
            # print("パスワードが異なります")
            flash("パスワードが異なります")
        else:
            # ログインに成功したとき
            flash("ログインしました")
            session["logged_in"] = True
            return redirect("/")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("logged_in",None)
    flash("ログアウトしました")
    return redirect("/")