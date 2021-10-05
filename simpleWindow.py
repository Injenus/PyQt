from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys


class Window(QMainWindow):  #create class
    def __init__(self):     #create констурктор//настройка класса
        super(Window, self).__init__()

        self.setWindowTitle("Простая прогрмма")
        self.setGeometry(300, 250, 350, 200)

        self.new_text = QtWidgets.QLabel(self)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Это базовая надпись")
        self.main_text.move(100, 100)
        self.main_text.adjustSize()

        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(70, 150)
        self.btn.setText("Нажми на меня")
        self.btn.setFixedWidth(200)
        self.btn.clicked.connect(self.add_label)


    def add_label(self):    #обработчик нажатия кнопки
        #self.new_text.SetText("Вторая надпись")
        #self.new_text.move(100, 50)
        #self.new_text.adjustSize()
        print('dgf')

def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    application()