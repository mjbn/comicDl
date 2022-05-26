from html.parser import HTMLParser

class shiraziSalad(HTMLParser):
    starttags = {}
    tag = None
    html = None

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

    def find(self, ftag):
        self.ftag = ftag

    def getElementById(self, _id):
        op = {}
        for tag in self.starttags:
            if tag['id'] == _id:
                op[tag] = tag
        return op
    def getElementByClass(self, _class):
        op = {}
        for tag in self.starttags:
            if tag['class'] == _class:
                op[tag] = tag
        return op

    def getElementByTag(self, _tag):
        op = {}
        for tag in self.starttags:
            if tag['tag'] == _tag:
                op[tag] = tag
        return op

if __name__=="__main__":
    salad = shiraziSalad("<html><body><h1 style='mj' src='s'>hello shiraz</h1><img src='s'></body></html>")
    salad.find('img')
    print(salad.starttags)

        

