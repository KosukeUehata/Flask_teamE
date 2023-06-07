# ビューファイル
from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app, db
from flask_blog.models.entries import Holiday


@app.route("/",methods=['GET', 'POST'])
def input():
    return render_template("input.html")


@app.route("/maintenance_date",methods=["POST", "GET"])
def result():
    if request.method == "POST":
        if request.form["holi_date"] == '':
            flash("日付を入力してください")
            return  render_template("input.html")
        else:
            if request.form["button"] == "insert_update":
                if request.form["holi_text"] == '':
                    flash("テキストを入力してください")
                    return  render_template("input.html")
                holiday = Holiday(
                holi_date=request.form["holi_date"],
                holi_text=request.form["holi_text"])

                holiday_aru = Holiday.query.get(holiday.holi_date)

                if holiday_aru != None: # 更新
                    db.session.merge(holiday)
                    db.session.commit()
                    shori = "update"
                    holi_date=holiday.holi_date
                    holi_text=holiday.holi_text
                    return render_template('result.html', shori=shori, holi_date=holi_date, holi_text=holi_text) 
                

                elif holiday_aru == None: # 登録
                    db.session.add(holiday)
                    db.session.commit()
                    shori = "add"
                    holi_date=holiday.holi_date
                    holi_text=holiday.holi_text
                    return render_template('result.html', shori=shori, holi_date=holi_date, holi_text=holi_text) 
            
            elif request.form["button"] == "delete": # 削除
                holiday = Holiday(
                holi_date=request.form["holi_date"],
                holi_text=request.form["holi_text"])
                holi_kesu = Holiday.query.get(holiday.holi_date)

                if holi_kesu == None: # 削除するものがない場合
                    flash(f"{holiday.holi_date}は、祝日マスタに登録されていません")
                    return  render_template("input.html")
                else:
                    db.session.delete(holi_kesu)
                    db.session.commit()
                    shori = "delete"
                    holi_date=holiday.holi_date
                    holi_text=holiday.holi_text
                    return render_template('result.html', shori=shori, holi_date=holi_date, holi_text=holi_text) ###
            

@app.route("/list",methods=["POST","GET"]) ###
def list():
    holidays = Holiday.query.order_by(Holiday.holi_date.desc()).all()
    return render_template("list.html",holidays=holidays)