from flask import request, redirect, url_for, render_template, flash, session
from mahjong_app import app
from mahjong_app import db
from mahjong_app.models.mst_marjong import DB_list


@app.route('/', methods=['GET', 'POST'])
def main_page():
    return render_template('main.html')

@app.route('/database_check', methods=['GET', 'POST'])
def database_check():
    
    point_sum = int(request.form["point1"]) + int(request.form["point2"]) + int(request.form["point3"]) + int(request.form["point4"])
    if point_sum != 100000:
        flash("点数の合計が10万点ちょうどとなるように入力してください！")
        return redirect(url_for("main_page")) 
    else:
        #データベースの読み込み
        holiday_insup = DB_list(player1 = request.form["player1"], player2 = request.form["player2"], player3 = request.form["player3"], player4 = request.form["player4"], point1 = int(request.form["point1"]), point2 = int(request.form["point2"]), point3 = int(request.form["point3"]), point4 = int(request.form["point4"]) )  
        db.session.add(holiday_insup)            
        db.session.commit()
        msg_out = "新たなレコードが登録されました！"
    return render_template("result.html", msg_out = msg_out)



@app.route("/list", methods=["POST"])
def list():
    PointList = DB_list.query.all()
    return render_template('list.html',PointList = PointList)


