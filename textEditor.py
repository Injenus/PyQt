from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QFileDialog

import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.setWindowTitle('Text editor')
        self.setGeometry(900,250,500,400)

        self.textEdit = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.textEdit)

        self.createMenuBar()

    def createMenuBar(self):
        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)

        fileMenu = QMenu('&File', self)
        self.menuBar.addMenu(fileMenu)

        fileMenu.addAction('Open', self.actionClicked)
        fileMenu.addAction('Save', self.actionClicked)

    @QtCore.pyqtSlot()
    def actionClicked(self):
        action = self.sender()  #получаем инфу об объекте, на который нажали
        if action.text() == 'Open':
            fname = QFileDialog.getOpenFileName(self)[0]    #выбираем всегда первый файл из всей выборки

            try:
                f = open(fname, 'r')
                with f:
                    data = f.read()
                    self.textEdit.setText(data)
                f.close()
            except FileNotFoundError:
                print('No file selected')

        elif action.text() == 'Save':
            fname = QFileDialog.getSaveFileName(self)[0]

            try:
                f = open(fname, 'w')
                text = self.textEdit.toPlainText()
                f.write(text)
                f.close()
            except FileNotFoundError:
                print('No file selected')


def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    application()