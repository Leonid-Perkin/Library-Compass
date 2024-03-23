from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from PyQt6.QtGui import QIcon
import csv


class MyWindow(QMainWindow):
    from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
    import csv

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Чтение базы данных")
        self.setWindowIcon(QIcon("istockphoto-1366075832-612x612.jpg"))

        self.tableWidget = QTableWidget(self)
        self.setCentralWidget(self.tableWidget)

        with open('book.csv', 'r') as file:
            csv_data = list(csv.reader(file))

        self.tableWidget.setRowCount(len(csv_data))
        self.tableWidget.setColumnCount(3)

        for row_num, row_data in enumerate(csv_data):
            for col_num, cell_data in enumerate(row_data):
                item = QTableWidgetItem(cell_data)
                self.tableWidget.setItem(row_num, col_num, item)

        self.tableWidget.setHorizontalHeaderLabels(["Book", "Date", "Stock"])
