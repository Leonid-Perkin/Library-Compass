import random
import time
from datetime import date
import csv
import cv2
from paho.mqtt import client as mqtt_client
from csv import writer
from library import MainWindow
from main import BookInfo
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QIcon
import sys
import qrcode

broker = '192.168.129.204'
port = 1883
topic1 = 'python/book'
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'admin'
password = 'admin'


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %dn", rc)

    client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION1, 'python3')
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client, book):
    result = client.publish(topic1, book)


def qr_read():
    cap = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()
    while True:
        _, img = cap.read()
        data, bbox, _ = detector.detectAndDecode(img)
        if bbox is not None:
            bb_pts = bbox.astype(int).reshape(-1, 2)
            num_bb_pts = len(bb_pts)
            for i in range(num_bb_pts):
                cv2.line(img,
                         tuple(bb_pts[i]),
                         tuple(bb_pts[(i + 1) % num_bb_pts]),
                         color=(255, 0, 255), thickness=2)
                cv2.putText(img, data,
                            (bb_pts[0][0], bb_pts[0][1] - 10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.5, (0, 255, 0), 2)
            if data:
                print("data found:", data)
                return data


def add_book():
    data = input()
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"C:\\Users\\OKS4-ST16\\Pictures\\LibaryCompas\\book.png", 'PDF')


def issue_book():
    client = connect_mqtt()
    client.loop_start()
    book = qr_read()
    publish(client, book)
    client.disconnect()
    formatted_time = date.today()

    with open('book.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow([book, formatted_time, 'Out of stock'])


def return_book():
    client = connect_mqtt()
    client.loop_start()
    book = qr_read()
    publish(client, f'{book}-return')
    client.disconnect()
    formatted_time = date.today()

    with open('book.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow([book, formatted_time, 'In stock'])


def search_book():
    book = qr_read()
    with open('book.csv', 'r') as f_object:
        arr = list(csv.reader(f_object))
        for i in range(len(arr) - 1, -1, -1):
            if arr[i][0] == book:
                row = arr[i]
                break
    print(f"Взяли: {row[1]}")
    print(f"Наличие: {row[2]}")
    issue = date.fromisoformat(row[1])
    if (date.today() - issue).days > 30:
        print("!!! Книга просрочена !!!")


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(lambda: add_book())
        self.ui.pushButton_2.clicked.connect(lambda: issue_book())
        self.ui.pushButton_3.clicked.connect(lambda: return_book())
        self.ui.pushButton_4.clicked.connect(lambda: self.book_info())

    def book_info(self):
        book = qr_read()
        with open('book.csv', 'r') as f_object:
            arr = list(csv.reader(f_object))
            for i in range(len(arr) - 1, -1, -1):
                if arr[i][0] == book:
                    row = arr[i]
                    break
        print(row)
        issue = date.fromisoformat(row[1])
        self.NewWindow = BookInfo()
        print(1)
        if row[2] == "Out of stock":
            if (date.today() - issue).days > 30:
                self.NewWindow.label4.setText("Книга просрочена")
            else:
                self.NewWindow.label4.setText(f"Срок пользования: {30 - (date.today() - issue).days}")
        print(1)
        self.NewWindow.label.setText(f"Книга: {row[0]}")
        self.NewWindow.label2.setText(f"Взяли: {row[1]}")
        self.NewWindow.label3.setText(f"Наличие: {row[2]}")
        self.NewWindow.show()



def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.setWindowIcon(QIcon("istockphoto-1366075832-612x612.jpg"))
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
