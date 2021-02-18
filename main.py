import sys

import requests
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QShortcut
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap, QKeySequence

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

        self.tags = []
        self.cord = ''
        self.params_maps = {
            # 'key': API_KEY,
            'll': self.cord,  # coordinate of center map
            'size': '550,450',
            'l': 'map',  # type of map: sat/sat,skl/map
            'z': '8',  # quality of map
            'spn': '0.005,0.005',  # length of map
            'pt': self.tags,  # tag on map
            'scale': 1.0  # 1.0 4.0
        }

        # hot keys
        self.go_button = QShortcut(QKeySequence("Return"), self)
        self.resolution_up = QShortcut(QKeySequence("PgUp"), self)
        self.resolution_down = QShortcut(QKeySequence("PgDown"), self)
        self.map_left = QShortcut(QKeySequence('Left'), self)
        # self.map_right = QShortcut(QKeySequence("Right"), self)
        # self.map_down = QShortcut(QKeySequence("Down"), self)
        # self.map_up = QShortcut(QKeySequence("Up"), self)
        self.resolution_up.activated.connect(self.fresolution_up)
        self.resolution_down.activated.connect(self.fresolution_down)
        self.go_button.activated.connect(self.shower)
        self.map_left.activated.connect(self.fmap_left)
        # self.map_right.activated.connect(self.fmap_right)
        # self.map_down.activated.connect(self.fmap_down)
        # self.map_up.activated.connect(self.fmap_up)

    def fresolution_up(self):
        if self.params_maps["scale"] < 4.0:
            self.params_maps["scale"] += 0.1
            pass

    def fresolution_down(self):
        if self.params_maps["scale"] >= 1.1:
            self.params_maps["scale"] -= 0.1
            self.show_map()

    def fmap_left(self):
        temp_ll = self.params_maps['ll'].split(',')
        temp_ll[1] = str(float(temp_ll[1]) + 0.0005)
        self.params_maps['ll'] = ','.join(temp_ll)
        self.show_map()
        print('left', self.params_maps)

    def shower(self):
        self.params_maps['ll'] = self.cord = self.lineEdit_3.text().replace(' ', '').replace('%2C', ',')
        self.x = self.lineEdit.text()  # Эти координаты мы получаем от пользователя
        self.size = self.lineEdit_2.text()
        self.show_map()

    def show_map(self):
        try:
            get_map(self.params_maps)
        except requests.exceptions.ConnectionError:
            print('Connection error')
        else:
            self.pixmap = QPixmap('data/map.png')
            self.label.setPixmap(self.pixmap)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Front_Widget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
