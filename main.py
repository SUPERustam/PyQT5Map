import sys

import requests
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap

from req_maps import get_map, MyBadRequest
from config import API_KEY  # api key doesn't work


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(820, 500)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Координаты:"))
        self.label_4.setText(_translate("Form", "Масштаб:"))
        self.pushButton.setText(_translate("Form", "Отобразить"))
        self.label.setText(_translate("Form", "TextLabel"))


class Front_Widget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pixmap = QPixmap('data/welcome.jpg')
        self.label.setPixmap(self.pixmap)

        self.pushButton.clicked.connect(self.shower)

        self.cord = '37.630481,55.772105'

        self.params_maps = {
            # 'key': API_KEY,
            'll': self.cord,
            'size': '550,450',
            'l': 'map',
            'z': '8',
            'spn': '0.005,0.005'
        }

    def shower(self):
        self.x = self.lineEdit.text()  # Эти координаты мы получаем от пользователя
        self.params_maps['ll'] = self.cord = self.lineEdit_3.text().replace(' ', '').replace('%2C', ',')
        self.size = self.lineEdit_2.text()

        try:
            get_map(self.params_maps)
        except requests.exceptions.ConnectionError:
            print('Connection error')
        else:
            self.pixmap = QPixmap('data/map.png')
            self.label.setPixmap(self.pixmap)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


def main():
    app = QApplication(sys.argv)
    ex = Front_Widget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
