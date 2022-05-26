#!/bin/python3
from shiraziSalad import shiraziSalad
from requests import get
from sys import argv, exit
from os import makedirs,mkdir,path
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget
from PyQt5.QtWidgets import *
from ui_comicdl import Ui_comicdl
from ui_setting import Ui_setting

class comicdl(QMainWindow, Ui_comicdl):
    # Window Init
    def __init__(self):
        # Parent Window Init
        super().__init__()
        # Setup Ui
        self.setupUi(self)
        # Seting The Value of Progressbar
        self.progressBar.setValue(0)
        # Window Title
        self.setWindowTitle('Comic DL')
        # Menu Bar actions
        self.actionSetting.triggered.connect(self.opensetting)
        self.actionExit.triggered.connect(self.close)
        # Setting Page Init
        self.s = self.setting()

    def opensetting(self):
        self.s.show()


    def startDl(self):
        percentPerChSteps = int(100/(self.toch.value() - self.fromch.value()))

        for ch in range(self.fromch.value(), self.toch.value()+1):
            pth = path.join('.',self.lineEdit_2.text(),str(ch))
            makedirs(pth)
            if self.s.chsites == 0:
                img_links = self.getLinks_mangatx(ch)
            elif self.s.chsites == 1:
                img_links = self.getLinks_1stkissmanga(ch)
            elif self.s.chsites == 2:
                img_links = self.getLinks_readm(ch)
            pecentPerImgSteps = int(100/(len(img_links) + 2))
            self.progressBar.setValue(pecentPerImgSteps)
            i = 1
            self.statusbar.showMessage(' ' + str(pecentPerImgSteps) +'% - '+str(ch)+'/'+str(percentPerChSteps))
            for link in img_links:
                file = open(path.join(pth,str(i)+'.jpg'), 'wb')
                file.write(get(link).content)
                file.close()
                self.statusbar.showMessage(' ' + str(i*pecentPerImgSteps) +'% - '+str(ch)+'/'+str(percentPerChSteps))
                self.progressBar.setValue(i*pecentPerImgSteps)
                i+=1
            self.statusbar.showMessage(' ' + str(i*pecentPerImgSteps) +'% - '+str(ch)+'/'+str(percentPerChSteps))
            self.progressBar.setValue(i*pecentPerImgSteps)

    def getLinks_mangatx(self, ch):
        url = self.lineEdit.text()+'chapter-'+str(ch)
        page = get(url)
        salad = shiraziSalad(page.content)
        img_tags = salad.getElementByTag(html, None)
        img_links = []
        for img_tag in img_tags:
            img_links.append(img_tag['data-src'])
        return img_links

    def getLinks_1stkissmanga(self, ch):
        # url = self.lineEdit.text()+'chapter-'+str(ch)
        # page = get(url)
        # print(page.content)
        # salad = shiraziSalad(page.content)
        # img_tags = salad.getElementByTag('img', None)
        # print(img_tags)
        # img_links = []
        # for img_tag in img_tags:
        #     img_links.append(img_tag['src'])
        # return img_links
        exit("Error: Cloudflare cookie error")

    def getLinks_readm(self, ch):
        url = self.lineEdit.text()+str(ch)+'/all-pages'
        page = get(url)
        salad = shiraziSalad(page.content)
        img_tags = salad.getElementByTag('img', None)
        img_links = []
        for img_tag in img_tags:
            img_links.append('https://readm.org'+img_tag['src'])
        return img_links

    class setting(QMainWindow, Ui_setting):
        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.setWindowTitle('Comic Dl - Setting')
            self.chsites = 0
        
        def changeSites(self, i):
            self.chsites = i

        def savesetting(self):
            self.close()

    

if __name__=="__main__":
    pycalc = QApplication(argv)
    view = comicdl()
    view.show()
    exit(pycalc.exec_())
