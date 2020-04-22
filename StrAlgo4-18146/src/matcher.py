import re, sys

class Matcher:
    def __init__(self, text = "", pattern = "-"):
        self.text = text.lower()
        self.pattern = pattern.lower()
        self.textLength = len(self.text)
        self.patLength = len(self.pattern)
        self.resultIdx = []

    def changeText(self, text):
        self.text = text.lower()
        self.textLength = len(text)
        return self

    def changePattern(self, pattern):
        self.pattern = pattern.lower()
        self.patLength = len(pattern)
        return self

    def getFirstTanggal(self):
        if(len(self.tanggal) == 0):
            return '-'
        return self.tanggal[0]

    def getFirstJumlah(self):
        if(len(self.jumlah) == 0):
            return '-'
        return self.jumlah[0]

    def findPattern(self, findAll = True):
        pass

    def findTanggal(self, findAll = True):
        self.tanggal = []
        tanggalType = ['\d\d?[-/]\d?\d[-/]\d{4}','\d{4}[-/]\d?\d[-/]\d\d?','\d\d?[-/]\d?\d[-/]\d\d',\
            '[Kk]emarin','\d\d[-/]\d?\d[-/]\d\d?', 
            '[Hh]ari ini', '[Kk]emarin lusa', '[Ss]enin', '[Ss]elasa', '[Rr]abu', '[Kk]amis',\
            '[Jj]um\'?at', '[Ss]abtu', '[Mm]inggu']
        for pat in tanggalType:
            self.tanggal = re.findall(pat, self.text)
            if(len(self.tanggal) != 0):
                break
        if(findAll):
            return self.tanggal
        if(len(self.tanggal) == 0):
            return '-'
        return self.tanggal[0]

    def findJumlah(self, findAll = True):
        self.jumlah = []
        # jumlahType = ['\d{1,3}[.,](\d{3}[.,])*\d{3} [Oo]rang', '(\d{1,3}[.,](\d{3}[.,])*\d{3}|\d+) [Kk]orban',\
        #     '(\d{1,3}[.,](\d{3}[.,])*\d{3}|\d+) [Pp]enderita', '(\d{1,3}[.,](\d{3}[.,])*\d{3}|\d+) [Jj]iwa']
        jumlahType = ['\d+ [Oo]rang', '\d+ [Kk]orban', '\d+ [Pp]enderita', '\d+ [Jj]iwa']
        for pat in jumlahType:
            self.jumlah = re.findall(pat, self.text)
            if(len(self.jumlah) != 0):
                self.jumlah =  re.findall('\d+ ', self.jumlah[0])
                break
        if(findAll):
            return self.jumlah
        if(len(self.jumlah) == 0):
            return '-'
        return self.jumlah[0]

    def solver(self, findAll = True):
        a = self.findPattern(findAll)
        if(self.hasPattern()):
            b = self.findJumlah(findAll)
            c = self.findTanggal(findAll)
        else:
            b, c = None, None
        return a, b, c

    def showResIdx(self):
        return self.resultIdx

    def hasPattern(self):
        return len(self.resultIdx) > 0

    def printSolution(self):
        # for debugging 
        for i in self.resultIdx:
            print(str(i) + '. ' + self.text[i:i+self.patLength])

class BoyerMooreMatcher(Matcher):
    def __init__(self, text = "", pattern = "-"):
        super().__init__(text=text, pattern=pattern)
        
    def initLookbackArray(self):
        # Find last occurence of a char in the pattern, if not found then -1
        lookback = [-1] * 256
        for i in range(self.patLength):
            lookback[ord(self.pattern[i])] = i
        return lookback

    def findPattern(self, findAll = True):
        self.resultIdx = []
        if(self.patLength > self.textLength):
            return self.resultIdx
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
                i = i + self.patLength - min(j, 1 + lookback_val)
                j = self.patLength - 1
                # if(lookback_val < j and lookback_val != -1):
                #     j = lookback_val
                # else:
                #     i, j = i + self.patLength, self.patLength - 1
        return self.resultIdx

class KMPMatcher(Matcher):
    def __init__(self, text = "", pattern = "-"):
        super().__init__(text=text, pattern=pattern)

    def initKMPBorder(self):
        KMPBorder = [-1] * self.patLength
        KMPBorder[0] = 0
        i, j = 1, 0
        while(i < self.patLength):
            if(self.pattern[i] == self.pattern[j]):
                KMPBorder[i] = j + 1
            elif(j > 0):
                j = KMPBorder[j - 1]
            else:
                KMPBorder[i]= 0
                i += 1
        return KMPBorder

    def findPattern(self, findAll = True):
        self.resultIdx = []
        if(self.patLength > self.textLength):
            return self.resultIdx
        KMPBorder = self.initKMPBorder()
        i, j = 0, 0
        while(i < self.textLength):
            if(self.pattern[j] == self.text[i]):
                if(j == self.patLength - 1):
                    self.resultIdx.append(i - self.patLength + 1)
                    if(not findAll):
                        break
                    i, j = i + 1, KMPBorder[j] 
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

    def findPattern(self, findAll = True):
        self.resultIdx = re.findall(self.pattern, self.text)
        return self.resultIdx

if __name__ == '__main__':
    pattern = "abc"
    text = "reabcasdsabcasdaabcb"
    matcher = BoyerMooreMatcher(text = text, pattern=pattern)
    matcher.solver()
    # print(len)
    print(matcher.resultIdx)
    # print(matcher.initLookbackArray())
    matcher.printSolution()
    matcher2 = KMPMatcher(text = text, pattern=pattern)
    matcher2.solver()
    # print(len)
    print(matcher2.resultIdx)
    matcher3 = RegexMatcher(text = text, pattern=pattern)
    matcher3.solver()
    # print(len)
    print(matcher3.resultIdx)
    pass

