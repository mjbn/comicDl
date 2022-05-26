from html.parser import HTMLParser

class shiraziSalad(HTMLParser):
    starttags = {}
    tag = None

    def __init__(self, html):
        super().__init__()
        self.feed(html)
    
    def handle_starttag(self, tag, attrs):
        tagTmp = '<'+tag
        atrTmp = {}
        atrTmp['tag'] = tag
        for atr in attrs:
            tagTmp += ' '+atr[0]+'=\"'+atr[1]+'\"'
            atrTmp[atr[0]] = atr[1]
        tagTmp += '>'
        self.tag = tagTmp
        self.starttags[tagTmp] = atrTmp

    def handle_data(self, data):
        self.starttags[self.tag]['value'] = data

    def getElementById(self, _id, htmlArray=None):
        op = {}
        if htmlArray == None:
            htmlArray = self.starttags
        for tag in htmlArray:
            if htmlArray[tag]['id'] == _id:
                op[tag] = htmlArray[tag]
        return op

    def getElementByClass(self, _class, htmlArray):
        op = {}
        if htmlArray == None:
            htmlArray = self.starttags
        for tag in htmlArray:
            if htmlArray[tag]['class'] == _class:
                op[tag] = htmlArray[tag]
        return op

    def getElementByTag(self, _tag, htmlArray):
        op = {}
        if htmlArray == None:
            htmlArray = self.starttags
        for tag in htmlArray:
            if htmlArray[tag]['tag'] == _tag:
                op[tag] = htmlArray[tag]
        return op

if __name__=="__main__":
    pass

        

