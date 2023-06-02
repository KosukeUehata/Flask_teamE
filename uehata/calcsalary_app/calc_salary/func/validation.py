from flask import request, url_for, render_template, flash, redirect, session


def validate_salary(salary):
    session["input_val"] = salary
    if salary == "":
        flash("給与が未入力です。入力してください。")
        return False
    
    if int(salary) < 0:
        flash("給与にマイナスの値は入力できません。")
        return False
    
    if int(salary) > 9999999999:
        flash("給与に最大9,999,999,999まで入力可能です。")
        return False
    
    session.pop("input_val",None)
    return True
    
    
    