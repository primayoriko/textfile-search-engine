from matcher import *
import sys, re

class FileData:
    def __init__(self, filename, text):
        self.filename = filename
        self.text = text
        self.parsedText = text.split(". ")

    def fetchInfo(self, pattern, method = "KMP"):
        result, matcher = [], None
        if(method == "KMP"):
            matcher = KMPMatcher("", pattern)
        elif(method == "BM"):
            matcher = BoyerMooreMatcher("", pattern)
        elif(method == "Regex"):

            pass

        for i in self.parsedText:
            matcher.changeText(i)
            matcher.solver()
            if(matcher.hasPattern()):
                result.append(i)

        if(len(result) != 0):
            
            return self
            

    # def matchPattern(self, pattern, method = "KMP"):
        
