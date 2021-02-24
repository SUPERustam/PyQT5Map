import sys
import json

import requests
from PyQt5.QtWidgets import QApplication, QWidget, QShortcut
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap, QKeySequence

from config import API_KEY, API_KEY_FOR_ORGANIZATIONS


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(743, 566)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        # labels
        self.ERROR = QtWidgets.QLineEdit(Form)
        self.ERROR.setObjectName("ERROR")
        self.gridLayout.addWidget(self.ERROR, 10, 1, 1, 1)
        self.ERROR.setEnabled(False)
        self.ERROR.hide()

        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 7, 0, 1, 1)

        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 10, 0, 1, 1)
        self.label_6.setText('Ошибка')
        self.label_6.hide()

        # Comboboxes
        self.Post_Index = QtWidgets.QComboBox(Form)
        self.Post_Index.setObjectName("Post_Index")
        self.gridLayout.addWidget(self.Post_Index, 7, 1, 1, 1)

        self.Type_Of_Map = QtWidgets.QComboBox(Form)
        self.Type_Of_Map.setObjectName("Type_Of_Map")
        self.gridLayout.addWidget(self.Type_Of_Map, 3, 1, 1, 1)

        # buttons
        self.Show_Button = QtWidgets.QPushButton(Form)
        self.Show_Button.setObjectName("Show_Button")
        self.gridLayout.addWidget(self.Show_Button, 1, 0, 1, 1)

        self.Search_Button = QtWidgets.QPushButton(Form)
        self.Search_Button.setObjectName("Search_Button")
        self.gridLayout.addWidget(self.Search_Button, 4, 0, 1, 1)

        # not functional button Save_Point_button, just "pass" this button
        self.Save_Point_button = QtWidgets.QPushButton(Form)
        self.Save_Point_button.setObjectName("Save_Point_button")
        self.gridLayout.addWidget(self.Save_Point_button, 5, 0, 1, 1)
        self.Save_Point_button.setEnabled(False)
        self.Save_Point_button.hide()

        self.Delete_Point_Button = QtWidgets.QPushButton(Form)
        self.Delete_Point_Button.setObjectName("Delete_Point_Button")
        self.gridLayout.addWidget(self.Delete_Point_Button, 8, 1, 1, 1)

        # boxes
        self.x = QtWidgets.QLineEdit(Form)
        self.x.setObjectName("x")
        self.gridLayout.addWidget(self.x, 0, 1, 1, 1)

        self.y = QtWidgets.QLineEdit(Form)
        self.y.setObjectName("y")
        self.gridLayout.addWidget(self.y, 1, 1, 1, 1)

        self.size = QtWidgets.QLineEdit(Form)
        self.size.setObjectName("size")
        self.gridLayout.addWidget(self.size, 2, 1, 1, 1)

        self.search_line = QtWidgets.QLineEdit(Form)
        self.search_line.setObjectName("search_line")
        self.gridLayout.addWidget(self.search_line, 4, 1, 1, 1)

        self.address = QtWidgets.QLineEdit(Form)
        self.address.setObjectName("address")
        self.gridLayout.addWidget(self.address, 6, 1, 1, 1)
        self.address.setEnabled(False)

        # other settings
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
        self.label_5.setText(_translate("Form", "Приписывание почтового"
                                                " индекса к полному адресу объекта"))
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

        self.Type_Of_Map.activated.connect(self.ftype_of_map)
        self.Post_Index.activated.connect(self.post_change)
        self.Show_Button.clicked.connect(self.shower)
        self.Search_Button.clicked.connect(self.search_words)
        self.Delete_Point_Button.clicked.connect(self.clear)

        # hot keys
        self.go_button = QShortcut(QKeySequence("return"), self)
        self.resolution_up = QShortcut(QKeySequence("PgUp"), self)
        self.resolution_down = QShortcut(QKeySequence("PgDown"), self)
        self.map_left = QShortcut(QKeySequence('Left'), self)
        self.map_right = QShortcut(QKeySequence("Right"), self)
        self.map_down = QShortcut(QKeySequence("Down"), self)
        self.map_up = QShortcut(QKeySequence("Up"), self)
        self.go_button.activated.connect(self.search_words)
        self.resolution_up.activated.connect(self.fresolution_up)
        self.resolution_down.activated.connect(self.fresolution_down)
        self.map_left.activated.connect(self.fmap_left)
        self.map_right.activated.connect(self.fmap_right)
        self.map_down.activated.connect(self.fmap_down)
        self.map_up.activated.connect(self.fmap_up)

        self.params_maps = {
            'll': '',  # coordinate of center map
            'size': '550,450',
            'l': 'map',  # type of map: sat/sat,skl/map
            'z': '8',  # quality of map
            'spn': '0.005,0.005',  # length of map
            'pt': ''  # tag on map
        }

    def fresolution_up(self):
        x = float(self.params_maps["spn"].split(',')[0])
        if x < 1.0:
            self.params_maps["spn"] = f'{2 * x},{2 * x}'
        self.show_map()

    def fresolution_down(self):
        x = float(self.params_maps["spn"].split(',')[0])
        if x > 0.0006:
            self.params_maps["spn"] = f'{x / 2},{x / 2}'
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

    def ftype_of_map(self):
        if self.Type_Of_Map.currentText() == 'спутник':
            self.params_maps['l'] = 'sat'
        elif self.Type_Of_Map.currentText() == 'гибрид':
            self.params_maps['l'] = 'sat,skl'
        else:
            self.params_maps['l'] = 'map'
        self.show_map()

    def shower(self):
        self.params_maps['ll'] = ','.join([self.x.text(), self.y.text()])
        if self.size.text():
            self.params_maps['spn'] = f'{self.size.text()},{self.size.text()}'
        self.show_map()

    def post_change(self):
        if self.Post_Index.currentText() == 'Включено':
            self.address.show()
        else:
            self.address.hide()

    def find_business(self):  # todo:
        search_params = {
            "apikey": API_KEY_FOR_ORGANIZATIONS,
            "lang": "ru_RU",
            "ll": self.params_maps["ll"],
            "spn": self.params_maps["spn"],
            "type": "biz",
            "text": self.params_maps["ll"],
        }
        try:
            response = requests.get("https://search-maps.yandex.ru/v1/", params=search_params)
            json_response = response.json()
            return json_response["features"][0] if json_response["features"] else None
        except KeyError:
            self.ERROR.setText('Connection failed or not found')
            self.ERROR.show()
            self.label_6.show()
        except IndexError:
            self.ERROR.setText('Connection failed or not found')
            self.ERROR.show()
            self.label_6.show()
        except requests.exceptions.ConnectionError:
            self.ERROR.setText('Connection failed or not found')
            self.ERROR.show()
            self.label_6.show()
        except json.decoder.JSONDecodeError:
            self.ERROR.setText('Connection failed or not found')
            self.ERROR.show()
            self.label_6.show()

    def show_map(self):
        try:
            response = requests.get("https://static-maps.yandex.ru/1.x/",
                                    params=self.params_maps)
            with open("data/map.png", "wb") as file:
                file.write(response.content)
        except requests.exceptions.ConnectionError:
            self.ERROR.setText('Connection failed')
            self.ERROR.show()
            self.label_6.show()
        else:
            self.ERROR.hide()
            self.label_6.hide()
            self.pixmap = QPixmap('data/map.png')
            self.label.setPixmap(self.pixmap)

    def search_words(self, post=True):
        try:
            local_params = {
                'apikey': API_KEY,
                'format': 'json',
                'geocode': self.search_line.text()
            }
            response = requests.get("https://geocode-maps.yandex.ru/1.x", params=local_params)
            local_json_response = response.json()
            self.params_maps['ll'] = local_json_response["response"]["GeoObjectCollection"][
                "featureMember"][0]["GeoObject"]['Point']['pos'].replace(' ', ',')
            self.params_maps['pt'] = f'{self.params_maps["ll"]},flag'

            try:
                self.address.setText(local_json_response["response"]["GeoObjectCollection"][
                                         "featureMember"][0]["GeoObject"]["metaDataProperty"][
                                         "GeocoderMetaData"]["Address"]["postal_code"])
            except KeyError:
                pass

            adr = local_json_response["response"]["GeoObjectCollection"][
                "featureMember"][0]["GeoObject"]["metaDataProperty"]["GeocoderMetaData"][
                "Address"]["formatted"]
            self.label_3.setText(f'Адрес: {adr}')
        except KeyError:
            self.ERROR.setText('Connection failed or not found')
            self.ERROR.show()
            self.label_6.show()
        except IndexError:
            self.ERROR.setText('Connection failed or not found')
            self.ERROR.show()
            self.label_6.show()
        except requests.exceptions.ConnectionError:
            self.ERROR.setText('Connection failed or not found')
            self.ERROR.show()
            self.label_6.show()
        except json.decoder.JSONDecodeError:
            self.ERROR.setText('Connection failed or not found')
            self.ERROR.show()
            self.label_6.show()
        else:
            text = self.size.text().strip().replace(',', '.').replace(' ', '.')
            if text:
                if 1.0 > float(text) > 0.0006:
                    self.params_maps['spn'] = f'{text},{text}'
                    self.ERROR.hide()
                    self.label_6.hide()
                else:
                    self.ERROR.setText('Value error')
                    self.ERROR.show()
                    self.label_6.show()

            self.x.setText(self.params_maps['ll'].split(',')[0])
            self.y.setText(self.params_maps['ll'].split(',')[1])
            self.show_map()

    def clear(self):
        self.params_maps['ll'], self.params_maps['pt'] = '', ''
        self.x.setText('')
        self.y.setText('')
        self.search_line.setText('')
        self.address.setText('')
        self.show_map()
        self.ERROR.hide()
        self.label_6.hide()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Front_Widget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
