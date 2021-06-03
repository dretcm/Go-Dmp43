# Alexander Carpio Mamani

import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication

class Dialogs(QWidget):
        def __init__(self):
                super().__init__()

        @staticmethod
        def dialog(title='Error!',
                   text = '''
                    POSIBLES ERRORES:
                    \n* Ingreso mal el url o link de YT.
                    \n* Hubo un error a la hora de descargar o convertir un archivo.
                    \n* Cierre la app o intentelo de nuevo.
                    ''',
                   icon=QMessageBox.Warning):
                
                msgBox = QMessageBox()
                msgBox.setIcon(icon)
                msgBox.setText(text)
                msgBox.setWindowTitle(title)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec()
                
if __name__=='__main__':
        app = QApplication(sys.argv)
        aux = Dialogs.dialog()
        sys.exit(app.exec_())
