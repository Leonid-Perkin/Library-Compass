from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QFont, QIcon
import sys


class BookInfo(QMainWindow):
    def __init__(self):
        super(BookInfo, self).__init__()
        self.setWindowTitle("Информация о книге")
        self.setWindowIcon(QIcon("istockphoto-1366075832-612x612.jpg"))

        self.label = QLabel()
        self.label2 = QLabel()
        self.label3 = QLabel()
        self.label4 = QLabel()

        font = QFont('Arial', 12)
        self.label.setFont(font)
        self.label2.setFont(font)
        self.label3.setFont(font)
        font.setBold(True)
        self.label4.setFont(font)
        self.label4.setStyleSheet("color: red;")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.label2)
        layout.addWidget(self.label3)
        layout.addWidget(self.label4)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BookInfo()
    window.show()
    app.exec()
