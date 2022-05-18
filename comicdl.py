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
        # Central Widget
        centrWidget = QWidget()
        # Widget
        lable1 = QLabel("Sites:")
        cb = QComboBox()
        cb.addItem("MangaTx")
        cb.currentIndexChanged.connect(self.selectionchange)
        lable2 = QLabel("Link:")
        lineEdit1 = QLineEdit()
        button1 = QPushButton("Download")
        # Layout
        layout = QFormLayout(centrWidget)
        layout.addRow(lable1, cb)
        layout.addRow(lable2,lineEdit1)
        layout.addRow(button1)
        # Window Properties
        self.setCentralWidget(centrWidget)
        self._createMenu()
        self._createStatusBar()
    
    def _createMenu(self):
        self.menu = self.menuBar().addMenu("&Comic DL")
        self.menu.addAction('&Setting', self.close)
        self.menu.addAction('&Exit', self.close)

    
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

