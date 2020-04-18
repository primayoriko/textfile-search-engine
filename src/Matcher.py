import re, sys

class Matcher:
    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern
        self.solution = []

    def changeText(self, text):
        self.text = text

    def changePattern(self, pattern):
        self.pattern = pattern

    def solver(self):
        pass

    def showResIdx(self):
        return self.resultIdx

class BooyerMooreMatcher(Matcher):
    def __init__(self, text, pattern):
        super().__init__(text, pattern)
        
    def initLookbackArray(self):
        self.lookback = [-1] * 256
        for i in range(len(self.pattern)):
            self.lookback[ord(self.pattern[i])] = i

    def solver(self):
        self.resultIdx = []
        self.initLookbackArray()
        i, j = len(self.pattern)-1, len(self.pattern)-1
        while(i<len(self.pattern)):
            if(self.pattern[j] == self.text[i]):
                if(j == 0):
                    self.resultIdx.append(i)
                    i, j = i+len(self.pattern), len(self.pattern)-1
                else:
                    i, j = i-1, j-1
            else:
                lookback_val = self.lookback[ord(self.text[i])]
                if(lookback_val < j and lookback_val!=-1):
                    j = lookback_val
                else:
                    i, j = i+len(self.pattern), len(self.pattern)-1

class KMPMatcher(Matcher):
    def __init__(self, text, pattern):
        super().__init__(text, pattern)        

    def solver(self):
        return super().solver()