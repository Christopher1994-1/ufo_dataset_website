from flask import Flask
import os


app = Flask(__name__)
app.secret_key = 'kjnkjankj4nkj3naiona90anjnioj099'
# app.secret_key = os.environ('ufo_key')


from flask_app import routes