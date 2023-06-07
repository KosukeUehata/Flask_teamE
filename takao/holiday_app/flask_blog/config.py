"""アプリケーションの環境情報や設定情報を記載したファイル"""
import os

DEBUG = True
SECRET_KEY = 'secret key'


user = os.getenv("DB_USER","root")
password = os.getenv("DB_PASSWORD","mysql")
host = os.getenv("DB_HOST","localhost")
database = os.getenv("DB_DATABASE","ENSHU")

SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8"
SQLALCHEMY_TRACK_MODIFICATIONS = False