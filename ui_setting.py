# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './setting.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_setting(object):
    def setupUi(self, setting):
        setting.setObjectName("setting")
        setting.resize(357, 386)
        self.centralwidget = QtWidgets.QWidget(setting)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 310, 88, 28))
        self.pushButton.setObjectName("pushButton")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 341, 291))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        setting.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(setting)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 357, 25))
        self.menubar.setObjectName("menubar")
        setting.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(setting)
        self.statusbar.setObjectName("statusbar")
        setting.setStatusBar(self.statusbar)

        self.retranslateUi(setting)
        self.comboBox.currentIndexChanged['int'].connect(setting.changeSites) # type: ignore
        self.pushButton.clicked.connect(setting.savesetting) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(setting)
        setting.setTabOrder(self.comboBox, self.pushButton)

    def retranslateUi(self, setting):
        _translate = QtCore.QCoreApplication.translate
        setting.setWindowTitle(_translate("setting", "MainWindow"))
        self.pushButton.setText(_translate("setting", "Ok"))
        self.label.setText(_translate("setting", "Sites:"))
        self.comboBox.setItemText(0, _translate("setting", "MangaTx"))
        self.comboBox.setItemText(1, _translate("setting", "1stKissManga"))
