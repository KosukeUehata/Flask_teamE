from flask import request, render_template, flash, redirect, url_for, session
from calc_salary import app
from  calc_salary.func.validation import validate_salary

@app.route("/", methods=["GET","POST"])
def input_salary():
    return render_template("input.html")


@app.route("/output", methods=["GET","POST"])
def output():
    if request.method == "POST":

        res_validation = validate_salary(request.form["salary"])
        if not res_validation:
            return redirect(url_for("input_salary"))
        
        salary = int(request.form["salary"])
        
        # 税額と支給額の初期化
        pay = 0 
        tax = 0

        # 税率
        tax_rate = [0.1,0.2]

        # 税金計算基準額
        BASE = 1000000

        # 給与が100万を超えている時の処理
        if salary > BASE:
            # 100万を超えた分
            exceed = salary - BASE
            # 100万を超えた額に対して20%の税率
            tax += exceed * tax_rate[1]
            # 100万に対して10%の税率
            tax += BASE * tax_rate[0]
        else:
            # 給与額に対して10%の税率
            tax += salary * tax_rate[0]

        # 支給額の算出
        pay = salary - tax

        # 少数第一位を四捨五入
        tax = round(tax)
        pay = round(pay)
        
        # 3桁ごとにカンマで区切る
        salary = "{:,}".format(salary)
        pay = "{:,}".format(pay)
        tax = "{:,}".format(tax)
        
        return render_template("output.html", salary=salary, pay=pay, tax=tax)

