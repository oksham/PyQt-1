import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("myfirst")
        self.resize(1200,700)
        
        self.btn_submit = QPushButton("Disable label",self)
        self.btn_submit.move(400,200)
        self.btn_submit.resize(300,100)
        self.btn_submit.clicked.connect(self.btn_eclicked)
        self.lbl_name = QLabel("YOU CAN SEE ME NOW ",self)
        self.lbl_name.move(250,450)
        self.lbl_name.setFont(QFont('Arial', 40))

    def btn_eclicked(self):
        self.lbl_name.setEnabled(False)
        self.btn_submit.setText("Enable label")
        self.btn_submit.clicked.connect(self.btn_dclicked)
    
    def btn_dclicked(self):
        self.lbl_name.setEnabled(True)
        self.btn_submit.setText("Disable label")
        self.btn_submit.clicked.connect(self.btn_eclicked)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = Window()
    dlg.show()
    app.exec_()
