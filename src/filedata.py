from matcher import *
import sys, re

class FileData:
    class ResultEntry:
        def __init__(self, text, jumlah, tanggal):
            self.text = text
            self.jumlah = jumlah
            self.tanggal = tanggal
        
        def getText(self):
            return self.text

        def getTanggal(self):
            return self.tanggal

        def getJumlah(self):
            return  self.jumlah

    def __init__(self, filename, text):
        self.filename = filename
        self.text = text
        self.parsedText = text.split(". ")

    def fetchInfo(self, pattern, method = "KMP"):
        self.result, matcher = [], None
        if(method == "KMP"):
            matcher = KMPMatcher(pattern = pattern)
        elif(method == "BM"):
            matcher = BoyerMooreMatcher(pattern = pattern)
        elif(method == "Regex"):
            matcher = RegexMatcher(pattern = pattern)
            pass

        for i in self.parsedText:
            matcher.changeText(i)
            matcher.solver()
            if(matcher.hasPattern()):
                newEntry = FileData.ResultEntry(i, matcher.getJumlah(), matcher.getTanggal())
                self.result.append(newEntry)

        self.nResult = len(self.result)
        if(self.nResult != 0):
            return self

    def getResultText(self):
        return self.result

    def getResultNum(self):
        return self.nResult
            

    # def matchPattern(self, pattern, method = "KMP"):
        
