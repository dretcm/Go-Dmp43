from youtube import Download_YT
from dialogs import Dialogs
from PyQt5.QtWidgets import (QWidget, QApplication, QLineEdit, QLabel,QPushButton, QComboBox, QFileDialog, QProgressBar, QCheckBox)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QThread
import sys

class Interface(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.folder = ""

        self.initUI()
                
        self.setWindowTitle('Go Dmp43')
        self.setWindowIcon(QIcon('yasu.ico'))
        self.resize(400,220)

        self.show()
        
    def initUI(self):

        bg = QLabel('',self)
        bg.setGeometry(0, 0, 400, 220)
        bg.setStyleSheet("background: black;")

        bg_label =QLabel('',self)
        bg_label.setGeometry(125, 10, 150, 40)
        bg_label.setStyleSheet("background: white;")
        
        label = QLabel('Go Dmp43',self)
        label.setGeometry(130, 10, 200, 40)
        label.setStyleSheet('font: 75 20pt "Arial";')
        
        self.entry = QLineEdit(self)
        self.entry.setPlaceholderText("url o link de youtube")
        self.entry.setStyleSheet('font: 75 11pt "Arial";')
        self.entry.setGeometry(20, 60, 360, 30)

        self.box = QComboBox(self)
        items = ['mp4-1080p','mp4-720p', 'mp4-480p', 'mp4-360p','mp3']
        for i in items:
            self.box.addItem(i)
        self.box.setStyleSheet('font: 75 11pt "Arial";')
        self.box.setGeometry(20, 100, 100, 30)
        
        self.button = QPushButton('Go', self)
        self.button.clicked.connect(self.go)
        self.button.setGeometry(100, 150, 200, 40)
        self.button.setStyleSheet('font: 75 18pt "Arial";')
        
        self.bar = QProgressBar(self)
        self.bar.setGeometry(50, 150, 300, 40)
        self.bar.setVisible(False)
        self.bar.setMaximum(0)
        self.bar.setMinimum(0)

        bg_check =QLabel('',self)
        bg_check.setGeometry(270, 100, 100, 30)
        bg_check.setStyleSheet("background: white;")
        
        self.check = QCheckBox('Playlist ? ', self)
        self.check.setGeometry(280, 100, 100, 30)
        self.check.setStyleSheet('font: 75 11pt "Arial";')

    def go(self):
        try:
            self.folder = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
            self.option = str(self.box.currentText())
            self.button.setEnabled(False)
            self.bar.setVisible(True)
            
            if self.check.isChecked():
                self.several()
            else:
                self.one()
        except Exception as e:
            Dialogs.dialog()
            print(e)

    def one(self):
        if self.option == 'mp3':
            self.yt = Download_YT(url=self.entry.text(), state=3)
        else:
            self.yt = Download_YT(url=self.entry.text(), resolution= self.option[4:], state=1)

        self.thread_process()

    def several(self):
        if self.option == 'mp3':
            self.yt = Download_YT(url=self.entry.text(), state=4)
        else:
            self.yt = Download_YT(url=self.entry.text(), resolution= self.option[4:], state=2)

        self.thread_process()
        
    def thread_process(self):
        self.yt.set_path(self.folder)
        self.yt.finished.connect(self.finish)
        self.yt.start()
        
    def finish(self):
        self.bar.setVisible(False)
        self.button.setEnabled(True)
        self.entry.clear()
        del self.yt

if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        Yt = Interface()
        sys.exit(app.exec_())
    except Exception as e:
        Dialogs.dialog(text=' Hubo un error con la app, intentelo de nuevo más tarde.')
        print(e)
        sys.exit()
    
