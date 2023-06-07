from datetime import datetime
from flask import Flask, request, redirect, render_template, flash, session, url_for
from holiday import app
from holiday import db
from holiday.models.mst_holiday import Holiday


@app.route('/update', methods=["POST"])
def update():
    """
    飛んできた処理によって
    新規登録・更新/削除
    に飛ばす

    dayが空ならここではじく
    """
    session["day"] = request.form["holiday"]
    session["name"] = request.form["holiday_text"]
    if request.form["holiday"] == "":
        flash('日付が入力されていません')
        return redirect( url_for('show_index') )

    if request.form["button"] == "insert_update":
        return redirect( url_for('overwrite') )
    elif request.form["button"] == "delete":
        return redirect( url_for('delete') )

@app.route('/maintenance_date', methods=["GET"])
def show_result():
    result = ''
    if session["status"] == "delete":
        result = f'{session["day"]}({session["name"]})は削除されました。'


    elif session["status"] == "insert":
        result = f'{session["day"]}({session["name"]})が登録されました。'
        
    
    elif session["status"] == "update":
        result = f'{session["day"]}は「{session["name"]}」に更新されました。'
    
    session.pop("status", None)
    session.pop("day", None)
    session.pop("name", None)
    return render_template('result.html', result=result)


@app.route('/overwrite')
def overwrite():
    day = session.get("day")
    name = session.get("name")

    if not 1 <= len(name) <= 20:
        flash('祝日名は1文字以上20文字以下でなければなりません。')
        return redirect(url_for('show_index'))

    target_day = Holiday(day, name)
    same_name_days_list = search_by_name(target_day)
    # 同じ名前の日があるか
    for same_name_day in same_name_days_list:
        if is_same_year(same_name_day, target_day): #同じ名前の日が同年に合ったらダメ
            flash('同じ名前の祝日が指定した日付と同年にあるため、登録できません。')
            return redirect(url_for('show_index'))
    
    session["day"] = target_day.holi_date.strftime("%Y-%m-%d")
    session["name"] = target_day.holi_text

    if is_found_same_day(target_day):
        db.session.merge(target_day)
        db.session.commit()
        session["status"] = "update"

    else:
        db.session.add(target_day)
        db.session.commit()
        session["status"] = "insert"

    return redirect( url_for('show_result') )


    pass


def search_by_name(target_day:Holiday):
    target_name = target_day.holi_text
    same_name_days = Holiday.query.filter_by(holi_text=target_name)
    return same_name_days

def is_found_same_day(target_day:Holiday):
    return Holiday.query.get(target_day.holi_date)


@app.route('/delete')
def delete():
    day = session.get("day")

    if day == "":
        flash('日付が入力されていません')
        return redirect(url_for('show_index'))
    
    search_day = Holiday(day, "")
    matched_day = Holiday.query.get(search_day.holi_date)

    if matched_day is not None:
        db.session.delete(matched_day)
        db.session.commit()
        session["status"] = "delete"
        session["day"] = matched_day.holi_date.strftime("%Y-%m-%d")
        session["name"] = matched_day.holi_text
        return redirect(url_for('show_result'))
    
    flash(f'{day}は祝日マスタに登録されていません')
    return redirect( url_for('show_index') )


def is_same_year(day1:Holiday, day2:Holiday) -> bool:
    dt1 = day1.holi_date
    dt2 = day2.holi_date
    return dt1.strftime("%Y") == dt2.strftime("%Y")

