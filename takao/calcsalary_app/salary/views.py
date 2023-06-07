# ビューファイル
from flask import request, redirect, url_for, render_template, flash, session
from salary import app


@app.route('/',methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/output',methods=['GET', 'POST'])
def logout():
    if request.method == 'POST':
        if request.form['username'] == '':
            flash('給与が未入力です。入力してください')
            return redirect(url_for('login'))
        else:
            sal = int(request.form['username'])
            if sal <= 1000000:
                tax = sal * 0.1
            else:
                tax = (sal - 1000000) * 0.2 + 1000000 * 0.1

            pay_amount = sal - tax

    return render_template('output.html',sal = f'{int(sal):,}', pay_amount = f'{int(pay_amount):,}', tax = f'{int(tax):,}')