from filedata import *
from time import time
from flask import Flask, flash, g, redirect, render_template, request, session, url_for
import sys, re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def handlerEvent():
    if request.method == 'GET':
        return render_template('mainpage.html', init = True)

    elif request.method == 'POST':
        algorithm = request.form['algorithm']
        keyword = request.form['keyword']
        filesData = request.files.getlist('files')
        
        files = {}
        for x in filesData:
            y = x.read(); y = y.decode("ASCII")
            y = re.sub("\r", " ", y)
            y = re.sub("\n", "", y)
            y = re.sub("\t", "", y)
            files[x.filename] = y
        
        result, nResult, timestamp1 = [], 0, time()
        for x, y in files.items():
            newFile = FileData(x, y)
            newFile = newFile.fetchInfo(keyword, algorithm)
            if(newFile is not None):
                result.append(newFile)
                nResult += newFile.getResultNum()
        
        timestamp2 = time()
        elapsedTime = (timestamp2 - timestamp1) * 1000

        return render_template('mainpage.html', keyword = keyword, init = False, result = result, nResult = nResult, elapsedTime = elapsedTime)

