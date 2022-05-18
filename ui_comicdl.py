# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './comicdl.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_comicdl(object):
    def setupUi(self, comicdl):
        comicdl.setObjectName("comicdl")
        comicdl.resize(807, 600)
        self.centralwidget = QtWidgets.QWidget(comicdl)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-10, 0, 341, 291))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.formLayoutWidget = QtWidgets.QWidget(self.tab)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 311, 211))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        self.progressBar = QtWidgets.QProgressBar(self.tab)
        self.progressBar.setGeometry(QtCore.QRect(10, 230, 311, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        comicdl.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(comicdl)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 807, 25))
        self.menubar.setObjectName("menubar")
        self.menuComic_DL = QtWidgets.QMenu(self.menubar)
        self.menuComic_DL.setObjectName("menuComic_DL")
        comicdl.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(comicdl)
        self.statusbar.setObjectName("statusbar")
        comicdl.setStatusBar(self.statusbar)
        self.actionSetting = QtWidgets.QAction(comicdl)
        self.actionSetting.setObjectName("actionSetting")
        self.actionExit = QtWidgets.QAction(comicdl)
        self.actionExit.setObjectName("actionExit")
        self.menuComic_DL.addAction(self.actionSetting)
        self.menuComic_DL.addAction(self.actionExit)
        self.menubar.addAction(self.menuComic_DL.menuAction())

        self.retranslateUi(comicdl)
        self.tabWidget.setCurrentIndex(0)
        self.lineEdit.returnPressed.connect(comicdl.startDl) # type: ignore
        self.pushButton.clicked.connect(comicdl.startDl) # type: ignore
        self.comboBox.currentIndexChanged['int'].connect(comicdl.changeSites) # type: ignore
        self.progressBar.valueChanged['int'].connect(comicdl.progress) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(comicdl)
        comicdl.setTabOrder(self.comboBox, self.lineEdit)
        comicdl.setTabOrder(self.lineEdit, self.pushButton)
        comicdl.setTabOrder(self.pushButton, self.tabWidget)

    def retranslateUi(self, comicdl):
        _translate = QtCore.QCoreApplication.translate
        comicdl.setWindowTitle(_translate("comicdl", "MainWindow"))
        self.label_2.setText(_translate("comicdl", "Sites"))
        self.comboBox.setItemText(0, _translate("comicdl", "MangaTX"))
        self.label.setText(_translate("comicdl", "Link"))
        self.pushButton.setText(_translate("comicdl", "Download"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("comicdl", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("comicdl", "Tab 2"))
        self.menuComic_DL.setTitle(_translate("comicdl", "Comic DL"))
        self.actionSetting.setText(_translate("comicdl", "Setting"))
        self.actionExit.setText(_translate("comicdl", "Exit"))