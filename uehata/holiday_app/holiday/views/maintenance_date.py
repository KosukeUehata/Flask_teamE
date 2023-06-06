from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db
from holiday.models.mst_holiday import Holiday


@app.route("/maintenance_date",methods=["GET", "POST"])
def result():
    
    # バリデーション1 : 日付の未入力
    if request.form["holiday"] == "":
        flash("祝日日付が未入力です")
        return redirect(url_for("input"))

    # バリデーション2 : 祝日テキストが未入力
    elif request.form["holiday_text"] == "":
        flash("祝日テキストが未入力です")
        return redirect(url_for("input"))
    
    if request.form["button"] == "insert_update":
        
        holiday = Holiday(
            holi_date=request.form["holiday"],
            holi_text=request.form["holiday_text"]
        )
        
        registered_holiday = Holiday.query.get(holiday.holi_date)
        if registered_holiday is None:
            # 登録処理
            db.session.add(holiday)
            db.session.commit()
            return render_template("result.html", holiday=holiday,method="create")     
        else:
            # 更新処理
            db.session.merge(holiday)
            db.session.commit()
            return render_template("result.html", holiday=holiday, method="update") 
    if request.form["button"] == "delete":
        holiday = Holiday(
            holi_date=request.form["holiday"],
            holi_text=request.form["holiday_text"]
        )
        
        # 削除の処理
        delete_holiday = Holiday.query.get(holiday.holi_date)
        if delete_holiday is None:
            flash(f"{holiday.holi_date}は、祝日マスタに登録されていません")
            return redirect(url_for("input"))
        
        db.session.delete(delete_holiday)
        db.session.commit()
        return render_template("result.html",holiday=delete_holiday, method="delete")


    return redirect(url_for("input"))