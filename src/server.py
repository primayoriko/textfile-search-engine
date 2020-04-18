from matcher import *
from flask import Flask
import sys

app = Flask(__name__)

@app.route('/')
def hehe():
    return {"msg" : "hello kitty"}

