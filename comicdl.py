#!/bin/python3
from bs4 import BeautifulSoup
from requests import get
from sys import argv, exit
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget
from PyQt5.QtWidgets import *
from ui_comicdl import Ui_comicdl
from wget import download


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

    def changeSites(self):
        pass

    def startDl(self):
        img_links = self.getImgLinks()
        pecentPerSteps = int(100/(len(img_links) + 2))
        self.progressBar.setValue(pecentPerSteps)
        i = 1
        for link in img_links:
            file = open('./'+str(i)+'.jpg', 'wb')
            file.write(get(link).content)
            file.close()
            self.statusbar.showMessage(' ' + str(i*pecentPerSteps) +'% - ')
            i+=1
        self.statusbar.showMessage(' ' + str(i*pecentPerSteps) +'% - Done')

    def progress(self,i):
        pass

    def getImgLinks(self):
        url = self.lineEdit.text()
        page = get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find("div", class_="reading-content")
        img_tags = results.find_all("img")
        img_links = []
        for img_tag in img_tags:
            img_links.append(img_tag['data-src'])
        return img_links

    




if __name__=="__main__":
    pycalc = QApplication(argv)
    view = comicdl()
    view.show()
    exit(pycalc.exec_())

