import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MYGUI")
        self.resize(500,500)
        self.lbl = QLabel("Set your password:",self)
        #to set the label

        self.lbl.move(40,35)
        self.edt_name = QLineEdit("",self)
        self.edt_name.setEchoMode(QLineEdit.Password)
        self.edt_name.move(50,55)
        #to create a textbox that takes in input as ENCRYPTED password

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = Window()
    dlg.show()
    app.exec_()