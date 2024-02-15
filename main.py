import random
import time
import csv
import cv2
from paho.mqtt import client as mqtt_client
from tkinter import *
from tkinter import ttk
import tkinter
import time
from csv import writer
broker = '192.168.0.221'
port = 1883
topic1 = "python/book"

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


def publish(client,book):
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
                        tuple(bb_pts[(i+1) % num_bb_pts]),
                        color=(255, 0, 255), thickness=2)
            cv2.putText(img, data,
                        (bb_pts[0][0], bb_pts[0][1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0, 255, 0), 2)
            if data:
                print("data found: ", data)
                return(data)


def add_book():
        a = qr_read()
        current_time = time.time()
        local_time = time.localtime(current_time)

        client = connect_mqtt()
        client.loop_start()
        publish(client,a)
        time.sleep(2)
        publish(client,'na')
        client.disconnect()
        formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
        print(formatted_time)

        with open("book.csv", "a", newline="") as f_object:
            writer_object = writer(f_object)
            writer_object.writerow([a,formatted_time,'In stock'])
            f_object.close()

def print_bd():
    root = tkinter.Tk()
    with open("book.csv", newline="") as file:
        reader = csv.reader(file)
        for r, col in enumerate(reader):
            for c, row in enumerate(col):
                label = tkinter.Label(
                    root, width=20, height=5, text=row, relief=tkinter.RIDGE
                )
                label.grid(row=r, column=c)

    root.mainloop()

def return_book():
    client = connect_mqtt()
    client.loop_start()
    book = qr_read()
    publish(client,book)
    time.sleep(2)
    publish(client,'na')
    client.disconnect()
    current_time = time.time()
    local_time = time.localtime(current_time)
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    print(formatted_time)
    with open("book.csv", "a", newline="") as f_object:
        writer_object = writer(f_object)
        writer_object.writerow([book,formatted_time,'Out of stock'])
        f_object.close()
def main():
    window = Tk()
    window.geometry('600x400+200+100')
    window.title("Библиотечный компас")
    btn = ttk.Button(text="Добавить книгу", command=add_book)
    btn.pack()
    btn1 = ttk.Button(text="Выдать книгу", command=return_book)
    btn1.pack()
    btn2 = ttk.Button(text="Чтение базы книг", command=print_bd)
    btn2.pack()
    window.mainloop()


if __name__ == '__main__':
    main()