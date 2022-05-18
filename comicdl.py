#!/bin/python3
from bs4 import BeautifulSoup
from requests import get
from sys import argv, exit
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget
from PyQt5.QtWidgets import *
from ui_comicdl import Ui_comicdl


class comicdl(QMainWindow, Ui_comicdl):
    # Window Init
    def __init__(self):
        # Parent Window Init
        super().__init__()
        # Setup Ui
        self.setupUi(self)
        # Window Title
        self.setWindowTitle('Comic DL')
        # Window Properties
        self._createStatusBar()

    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("I'm the Status Bar")
        self.setStatusBar(status)

    def selectionchange(self):
        pass

    def getImgLinks():
        page = get("https://mangatx.com/manga/rebirth-of-the-urban-immortal-cultivator-manhua/chapter-1/")
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find("div", class_="reading-content")
        img_tag = results.find_all("img")
        img_links = []
        for i in img_tag.index():
            img_links.append(img_tag[i]["data-src"])
        return img_links

    




if __name__=="__main__":
    pycalc = QApplication(argv)
    view = comicdl()
    view.show()
    exit(pycalc.exec_())

