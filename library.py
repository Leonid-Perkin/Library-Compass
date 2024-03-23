from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from print_bd import MyWindow


class MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(346, 241)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(15, 15, 316, 31))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(164, 164, 164);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(15, 60, 316, 31))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(164, 164, 164);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(15, 105, 316, 31))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(164, 164, 164);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(15, 150, 316, 31))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(164, 164, 164);\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(15, 195, 316, 31))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(164, 164, 164);\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.data_base)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Библиотечный Компас"))
        self.pushButton.setText(_translate("MainWindow", "Добавить книгу"))
        self.pushButton_2.setText(_translate("MainWindow", "Взять книгу"))
        self.pushButton_3.setText(_translate("MainWindow", "Вернуть книгу"))
        self.pushButton_4.setText(_translate("MainWindow", "Информация о книге"))
        self.pushButton_5.setText(_translate("MainWindow", "Чтение Базы Данных"))
    def data_base(self):
        self.new_window = MyWindow()
        self.new_window.show()
