from youtube import Download_YT, showDialog
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QProgressBar
from PyQt5.QtGui import QIcon
import sys

class Interface:
    def __init__(self):
        app = QtWidgets.QApplication([])
        app.setApplicationDisplayName('Go Dmp43')
        app.setWindowIcon(QIcon('yasu.ico'))
        app.setStyleSheet("QMainWindow{background: black;}")

        #self.yt = Download_YT()
        self.dig =uic.loadUi("interface_yt.ui")

        self.dig.lineEdit_1.setPlaceholderText("url o link de youtube")
        self.dig.lineEdit_1.setStyleSheet('font: 75 11pt "Arial";')

        items = ['mp4-720p', 'mp4-480p', 'mp4-360p','mp3']
        for i in items:
            self.dig.comboBox.addItem(i)
        self.dig.comboBox.setStyleSheet('font: 75 11pt "Arial";')

        self.dig.button_1.clicked.connect(self.go)

        self.dig.progressBar.setVisible(False)
        self.dig.progressBar.setMaximum(0)
        self.dig.progressBar.setMinimum(0)

        self.dig.show()
        app.exec()

    def go(self):
        try:
            self.option = str(self.dig.comboBox.currentText())
            self.dig.button_1.setEnabled(False)
            self.dig.progressBar.setVisible(True)
            if self.dig.checkBox.isChecked():
                self.several()
            else:
                self.one()
        except:
            showDialog()

    def one(self):
        if self.option == 'mp3':
            self.yt = Download_YT(url=self.dig.lineEdit_1.text(), state=3)
        else:
            self.yt = Download_YT(url=self.dig.lineEdit_1.text(), resolution= self.option[4:], state=1)

        self.yt.finished.connect(self.finish)
        self.yt.start()   

    def several(self):
        if self.option == 'mp3':
            self.yt = Download_YT(url=self.dig.lineEdit_1.text(), state=4)
        else:
            self.yt = Download_YT(url=self.dig.lineEdit_1.text(), resolution= self.option[4:], state=2)
            
        self.yt.finished.connect(self.finish)
        self.yt.start()

    def finish(self):
        self.dig.progressBar.setVisible(False)
        self.dig.button_1.setEnabled(True)
        self.dig.lineEdit_1.clear()
        del self.yt

if __name__ == '__main__':
    try:
        Yt = Interface()
    except:
        showDialog(text=' Hubo un error con la app, intentelo de nuevo más tarde.')
        sys.exit()
    