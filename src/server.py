from matcher import *
from flask import Flask, flash, g, redirect, render_template, request, session, url_for
import sys

app = Flask(__name__)

@app.route('/')
def loadMainPage():
    return render_template('layout/mainpage.html')
    # return {"msg" : "hello kitty"}

