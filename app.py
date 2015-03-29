from flask import Flask
from flask import render_template
import os

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = os.urandom(24)
