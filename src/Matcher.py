import re, sys

class Matcher:
    def __init__(self, text = "", pattern = "-"):
        self.text = text
        self.pattern = pattern
        self.textLength = len(self.text)
        self.patLength = len(self.pattern)
        self.resultIdx = []

    def changeText(self, text):
        self.text = text
        return self

    def changePattern(self, pattern):
        self.pattern = pattern
        return self

    def solver(self, findAll = True):
        pass

    def showResIdx(self):
        return self.resultIdx

    def hasPattern(self):
        return len(self.resultIdx) > 0

    def writeSolution(self):
        for i in self.resultIdx:
            print(i + '. ' + self.text[i:i+self.patLength])

class BoyerMooreMatcher(Matcher):
    def __init__(self, text = "", pattern = "-"):
        super().__init__(text=text, pattern=pattern)
        
    def initLookbackArray(self):
        # Find last occurence of a char in the pattern, if not found then -1
        lookback = [-1] * 256
        for i in range(self.patLength):
            lookback[ord(self.pattern[i])] = i
        return lookback

    def solver(self, findAll = True):
        self.resultIdx = []
        lookback = self.initLookbackArray()
        i, j = self.patLength - 1, self.patLength - 1
        while(i < self.textLength):
            if(self.pattern[j] == self.text[i]):
                if(j == 0):
                    self.resultIdx.append(i)
                    if(not findAll):
                        break
                    i, j = i + self.patLength, self.patLength - 1
                else:
                    i, j = i - 1, j - 1
            else:
                lookback_val = lookback[ord(self.text[i])]
                if(lookback_val < j and lookback_val != -1):
                    j = lookback_val
                else:
                    i, j = i + self.patLength, self.patLength - 1
        return self.resultIdx

class KMPMatcher(Matcher):
    def __init__(self, text = "", pattern = "-"):
        super().__init__(text=text, pattern=pattern)

    def initKMPBorder(self):
        KMPBorder = [-1] * self.patLength
        i, j = 0, 0
        while(i < self.patLength):
            pass
        return KMPBorder

    def solver(self, findAll = True):
        self.resultIdx = []
        KMPBorder = self.initKMPBorder()
        i, j = 0, 0
        while(i < self.textLength):
            if(self.pattern[j] == self.text[i]):
                if(j == self.patLength - 1):
                    self.resultIdx.append(i - self.patLength + 1)
                    if(not findAll):
                        break
                    i, j = i + 1, KMPBorder(j) 
                else:
                    i, j = i + 1, j + 1
            else:
                if(j > 0):
                    j = KMPBorder[j - 1]
                else:
                    i += 1
        return self.resultIdx

class RegexMatcher(Matcher):
    def __init__(self, text='', pattern='-'):
        super().__init__(text=text, pattern=pattern)

    def solver(self):
        pass

