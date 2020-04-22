from filedata import *
from flask import Flask, flash, g, redirect, render_template, request, session, url_for
import sys

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
            y = y.split("\r"); y = " ".join(y)
            y = y.split("\n"); y = "".join(y)
            y = y.split("\t"); y = "".join(y)
            files[x.filename] = y
        
        result, nResult, elapsedTime = [], 0, 0
        for x, y in files.items():
            newFile = FileData(x, y)
            newFile = newFile.fetchInfo(keyword, algorithm)
            if(newFile is not None):
                result.append(newFile)
                nResult += newFile.getResultNum()

        # result = list(filter(lambda iter : iter is not None, result))
        # elapsedTime = 0
        return render_template('mainpage.html', init = False, result = result, nResult = nResult, elapsedTime = elapsedTime)
        
        # response = {"algo" : request.form['algo'], "keyword" : request.form['keyword']}
        # i = 0
        # for x in request.files['attachment']:
        #     i += 1
        #     response[x.filename] = x.read()
        # return  response
        # x = ""
