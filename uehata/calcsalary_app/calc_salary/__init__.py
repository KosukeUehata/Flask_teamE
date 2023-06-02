from flask import Flask 

app = Flask(__name__)
app.config.from_object("calc_salary.config")

import calc_salary.views.views