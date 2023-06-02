from flask import request, redirect, url_for, render_template, flash, session
from salary import app

from decimal import Decimal, ROUND_HALF_UP
import re

@app.route('/')
def show_index():
    input = ''
    if session.get('input'):
        input = session['input']
    return render_template('input.html', input=input)

@app.route('/output', methods=["POST"])
def show_salary():
    if request.method == 'POST':
        session["input"] = request.form['salary']
        if request.form['salary'] == '':
            flash('給与が未入力です。入力してください。')
            return redirect(url_for('show_index'))
        elif len(request.form['salary']) > 10:
            flash('給与には最大9,999,999,999まで入力が可能です。')
            return redirect(url_for('show_index'))
        elif  re.fullmatch('-[0-9]+', request.form['salary']) is not None:
            flash('給与にはマイナスの値は入力できません。')
            return redirect(url_for('show_index'))
        elif 'e' in request.form['salary']:
            flash('指数表記は対応していません。')
            return redirect(url_for('show_index'))
    salary = int(request.form['salary'])
    payment, tax = calcsalary(salary)
    session.pop('input', None)
    return render_template('output.html', salary=salary, payment=payment, tax=tax)


def calcsalary(salary):
    border = 1000000
    payment, tax = 0, 0
    if salary >= border:
        tax = 0.2*(salary-border)+100000
    else:
        tax = 0.1*salary

    # 小数点以下で四捨五入
    tax = Decimal(str(tax)).quantize(Decimal("0"), rounding=ROUND_HALF_UP)
    payment = salary-tax
    return payment, tax