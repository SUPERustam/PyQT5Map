import sys

import requests
from PyQt5.QtWidgets import QApplication, QWidget, QShortcut
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap, QKeySequence

#from req_maps import get_map, MyBadRequest  # MyBadRequest is important
#from config import API_KEY  # api key doesn't work


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(743, 566)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Size = QtWidgets.QLineEdit(Form)
        self.Size.setObjectName("Size")
        self.gridLayout.addWidget(self.Size, 2, 1, 1, 1)

        self.Post_Index = QtWidgets.QComboBox(Form)
        self.Post_Index.setObjectName("Post_Index")
        self.gridLayout.addWidget(self.Post_Index, 7, 1, 1, 1)

        self.Save_Point_button = QtWidgets.QPushButton(Form)
        self.Save_Point_button.setObjectName("Save_Point_button")
        self.gridLayout.addWidget(self.Save_Point_button, 5, 0, 1, 1)

        self.Delete_Point_Button = QtWidgets.QPushButton(Form)
        self.Delete_Point_Button.setObjectName("Delete_Point_Button")
        self.gridLayout.addWidget(self.Delete_Point_Button, 8, 1, 1, 1)

        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 7, 0, 1, 1)

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.Address = QtWidgets.QLineEdit(Form)
        self.Address.setObjectName("Address")
        self.gridLayout.addWidget(self.Address, 6, 1, 1, 1)
        self.Address.setEnabled(False)

        self.Search_Line = QtWidgets.QLineEdit(Form)
        self.Search_Line.setObjectName("Search_Line")
        self.gridLayout.addWidget(self.Search_Line, 4, 1, 1, 1)

        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.x = QtWidgets.QLineEdit(Form)
        self.x.setObjectName("x")
        self.gridLayout.addWidget(self.x, 0, 1, 1, 1)

        self.Search_Button = QtWidgets.QPushButton(Form)
        self.Search_Button.setObjectName("Search_Button")
        self.gridLayout.addWidget(self.Search_Button, 4, 0, 1, 1)

        self.y = QtWidgets.QLineEdit(Form)
        self.y.setObjectName("y")
        self.gridLayout.addWidget(self.y, 1, 1, 1, 1)

        self.Type_Of_Map = QtWidgets.QComboBox(Form)
        self.Type_Of_Map.setObjectName("Type_Of_Map")
        self.gridLayout.addWidget(self.Type_Of_Map, 3, 1, 1, 1)

        self.Show_Button = QtWidgets.QPushButton(Form)
        self.Show_Button.setObjectName("Show_Button")
        self.gridLayout.addWidget(self.Show_Button, 1, 0, 1, 1)

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.ERROR = QtWidgets.QLineEdit(Form)
        self.ERROR.setObjectName("ERROR")
        self.gridLayout.addWidget(self.ERROR, 10, 1, 1, 1)
        self.ERROR.setEnabled(False)
        self.ERROR.hide()

        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 10, 0, 1, 1)
        self.label_6.hide()

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.Picture = QtWidgets.QLabel(Form)
        self.Picture.setObjectName("Picture")
        self.gridLayout_2.addWidget(self.Picture, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Save_Point_button.setText(_translate("Form", "Сохранить метку"))
        self.Delete_Point_Button.setText(_translate("Form", "Сброс поискового результата"))
        self.label_5.setText(_translate("Form", "Приписывание почтового индекса к полному адресу объекта"))
        self.label_3.setText(_translate("Form", "Адрес:"))
        self.label_4.setText(_translate("Form", "Масштаб"))
        self.label.setText(_translate("Form", "Координаты:"))
        self.Search_Button.setText(_translate("Form", "Искать"))
        self.Show_Button.setText(_translate("Form", "Отобразить"))
        self.label_2.setText(_translate("Form", "Слой карты:"))
        self.label_6.setText(_translate("Form", "Ошибка:"))
        self.Picture.setText(_translate("Form", "TextLabel"))


class Front_Widget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.Type_Of_Map.addItem('схема')
        self.Type_Of_Map.addItem('спутник')
        self.Type_Of_Map.addItem('гибрид')

        self.Post_Index.addItem('Включено')
        self.Post_Index.addItem('Выключено')

        self.pixmap = QPixmap('data/welcome.jpg')
        self.Picture.setPixmap(self.pixmap)

        self.Show_Button.clicked.connect(self.shower)

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
        self.go_button = QShortcut(QKeySequence("return"), self)
        self.resolution_up = QShortcut(QKeySequence("PgUp"), self)
        self.resolution_down = QShortcut(QKeySequence("PgDown"), self)
        self.map_left = QShortcut(QKeySequence('Left'), self)
        self.map_right = QShortcut(QKeySequence("Right"), self)
        self.map_down = QShortcut(QKeySequence("Down"), self)
        self.map_up = QShortcut(QKeySequence("Up"), self)
        self.resolution_up.activated.connect(self.fresolution_up)
        self.resolution_down.activated.connect(self.fresolution_down)
        self.go_button.activated.connect(self.shower)
        self.map_left.activated.connect(self.fmap_left)
        self.map_right.activated.connect(self.fmap_right)
        self.map_down.activated.connect(self.fmap_down)
        self.map_up.activated.connect(self.fmap_up)

    def fresolution_up(self):
        if self.params_maps["scale"] < 4.0:
            self.params_maps["scale"] += 0.1

    def fresolution_down(self):
        if self.params_maps["scale"] >= 1.1:
            self.params_maps["scale"] -= 0.1
            self.show_map()

    def fmap_up(self):
        temp_ll = self.params_maps['ll'].split(',')
        temp_ll[1] = str(float(temp_ll[1]) + 0.0005)
        self.params_maps['ll'] = ','.join(temp_ll)
        self.show_map()

    def fmap_left(self):
        temp_ll = self.params_maps['ll'].split(',')
        temp_ll[0] = str(float(temp_ll[0]) - 0.0005)
        self.params_maps['ll'] = ','.join(temp_ll)
        self.show_map()

    def fmap_right(self):
        temp_ll = self.params_maps['ll'].split(',')
        temp_ll[0] = str(float(temp_ll[0]) + 0.0005)
        self.params_maps['ll'] = ','.join(temp_ll)
        self.show_map()

    def fmap_down(self):
        temp_ll = self.params_maps['ll'].split(',')
        temp_ll[1] = str(float(temp_ll[1]) - 0.0005)
        self.params_maps['ll'] = ','.join(temp_ll)
        self.show_map()

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

