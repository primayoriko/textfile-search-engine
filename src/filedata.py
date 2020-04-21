from matcher import *
import sys, re

class FileData:
    def __init__(self, filename, text):
        self.filename = filename
        self.text = text
        self.parsedText = text.split(". ")
        self.jumlah = 0
        self.tanggal = 0

    def fetchInfo(self, pattern, method = "KMP"):
        matcher = None
        if(method == "KMP"):

            pass
        elif(method == "BM"):

            pass
        elif(method == "Regex"):

            pass

        if(matcher != None):

            return self
            

    # def matchPattern(self, pattern, method = "KMP"):
        
