from flask import render_template, request
from app import app
from schedule_api import *

class Posting:
    def __init__(self, text):
        self.text = text
        self.score = 0

posts = [ Posting('test post 1'), Posting('test post 2') ]

@app.route('/')
def index():
    options = { 'posts': posts }

    return render_template('index.html', **options)

@app.route('/posting/<id>')
def details(id):
    options = { 'post': posts[int(id)] }

    return render_template('details.html', **options)
