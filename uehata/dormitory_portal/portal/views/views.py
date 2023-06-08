from flask import request, redirect, url_for, render_template, flash, session
from portal import app
from functools import wraps
from portal.models.notice import Notice
from portal.models.reserve import Reserve
from portal import db
import datetime

def login_required(view):
    @wraps(view)
    def inner(*args, **kwargs):
        if not session.get("logged_in"):
            return redirect(url_for("login"))
        return view(*args, **kwargs)
    return inner


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["room_id"] != app.config["ROOM_ID"]:
            flash("部屋番号が異なります")
        elif request.form["password"] != app.config["PASSWORD"]:
            flash("パスワードが異なります")
        else:
            flash("ログインに成功しました")
            session["logged_in"] = True
            session["room_id"] = request.form["room_id"]
            return  redirect(url_for('top'))
        
    return render_template("login.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/logout")
def logout():
    session.pop("logged_in",None)
    session.pop("room_id",None)
    
    flash("ログアウトしました")
    return redirect(url_for("login"))

@app.route("/", methods=["GET", "POST"])
@login_required
def top():
    room_id = session.get("room_id")
    reserve = None
    if room_id is not None:
        reserve = Reserve.query.filter_by(room_id=int(room_id)).order_by(Reserve.day.asc()).all()
    notice = Notice.query.order_by(Notice.id.desc()).all()
    return render_template("top.html", notice=notice, reserve=reserve)

# お知らせ詳細画面
@app.route("/notice/<int:id>", methods=["GET","POST"])
@login_required
def notice(id):
    notice = Notice.query.get(id)
    return render_template('notice.html', notice=notice)


@app.route("/reserve" , methods=["GET", "POST"])
@login_required
def reserve():
    room_id = session.get('room_id')
    if request.method == "POST":
        datetime_now = datetime.datetime.utcnow() + datetime.timedelta(hours=9)
        reserve_day = str(request.form["reserve_date"])
        limit_time = reserve_day + " 9:00:00"
        
        room_id = int(request.form["room_id"])
        type = request.form["inlineRadioOptions"]
        day = reserve_day
        index =  len(Reserve.query.all()) + 1
        reserve = Reserve(room_id=room_id, type=type , day=day, index=index)
        
        reserved = Reserve.query.filter_by(room_id=reserve.room_id, type=reserve.type, day=reserve.day).first()
        if reserved is not None:
            flash("予約済みです")
            return redirect(url_for('reserve'))

        if request.form["inlineRadioOptions"] == "breakfast":
            # 朝食予約処理
            reserve_date = datetime.datetime.strptime(limit_time, '%Y-%m-%d %H:%M:%S')
            deleta = datetime.timedelta(days=-1)
            limit_datetime = reserve_date + deleta
            
            if datetime_now < limit_datetime:
                flash(f"{reserve_day} の朝食を予約しました")
                db.session.add(reserve)
                db.session.commit()
            else:
                flash("予約可能時間を超過しています")
            
        elif request.form["inlineRadioOptions"] == "dinner":
            # 夕食予約処理
            limit_datetime = datetime.datetime.strptime(limit_time, '%Y-%m-%d %H:%M:%S')
            if datetime_now < limit_datetime:
                flash(f"{reserve_day} の夕食を予約しました")
                db.session.add(reserve)
                db.session.commit()
            else:
                flash("予約可能時間を超過しています")
                
        return redirect(url_for('reserve'))
    
    return render_template('reserve.html' , room_id=room_id)


# 管理者ページ
@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        
        reg_notice = Notice.query.all()
        
        notice = Notice(
            id = len(reg_notice) + 1,
            title=request.form["notice_title"],
            content=request.form["notice_content"]
        )
        
        db.session.add(notice)
        db.session.commit()
        flash("登録成功しました。")
        
        return redirect(url_for("admin"))
    
    return render_template('admin.html')