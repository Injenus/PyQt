from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys


class Window(QMainWindow):  #create class
    def __init__(self):     #create констурктор//настройка класса
        super(Window, self).__init__()


def add_label():    #обработчик нажатия кнопки
    print("add")


def application():
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle("Простая прогрмма")
    window.setGeometry(300, 250, 350, 200)

    main_text = QtWidgets.QLabel(window)
    main_text.setText("Это базовая надпись")
    main_text.move(100, 100)
    main_text.adjustSize()

    btn=QtWidgets.QPushButton(window)
    btn.move(70, 150)
    btn.setText("Нажми на меня")
    btn.setFixedWidth(200)
    btn.clicked.connect(add_label)

    window.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    application()