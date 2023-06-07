from flask import Flask, request, redirect, render_template, flash, session
from holiday import app
from holiday.models.mst_holiday import Holiday

@app.route('/list', methods=['POST'])
def show_list():
    holidays = Holiday.query.order_by(Holiday.holi_date)
    return render_template('list.html', holidays=holidays)
