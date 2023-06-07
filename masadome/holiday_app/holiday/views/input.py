from flask import Flask, request, redirect, render_template, flash, session
from holiday import app

@app.route('/', methods=['GET', 'POST'])
def show_index():
    return render_template('input.html')

# @app.route('/update', methods=['POST'])
# def update_record():
#     if request.form["button"] == "insert_update":
#         return "upd"
#     elif request.form["button"] == "delete":
#         return "del"