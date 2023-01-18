import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MYGUI")
        self.resize(900,800)
        
        #labels is created
        self.lbl_num1 = QLabel("Number 1: ",self)
        self.lbl_num1.move(100,100)
        self.lbl_num1.resize(100,50) 

        self.lbl_num2 = QLabel("Number 2: ",self)
        self.lbl_num2.move(100,250)
        self.lbl_num2.resize(100,50)

        self.lbl_res = QLabel("Result: ",self)
        self.lbl_res.move(100,400)
        self.lbl_res.resize(100,50)

        #text box to get the input is created
        self.edt_box1 = QLineEdit("", self)
        self.edt_box1.setPlaceholderText("")
        self.edt_box1.move(200,100)
        self.edt_box1.resize(200,50)

        self.edt_box2 = QLineEdit("", self)
        self.edt_box2.setPlaceholderText("")
        self.edt_box2.move(200,250)
        self.edt_box2.resize(200,50)

        #text box to display the output is created
        self.edt_boxres = QLineEdit("", self)
        self.edt_boxres.setPlaceholderText("")
        self.edt_boxres.move(200,400)
        self.edt_boxres.resize(200,50)

        #Button is created which gets the input value from user 
        self.btn_get_input1 = QPushButton("ENTER THE NUMBER", self)
        self.btn_get_input1.move(450,100)
        self.btn_get_input1.resize(200,50)
        self.btn_get_input1.clicked.connect(self.num1_clk)

        self.btn_get_input2 = QPushButton("ENTER THE NUMBER", self)
        self.btn_get_input2.move(450,250)
        self.btn_get_input2.resize(200,50)
        self.btn_get_input2.clicked.connect(self.num2_clk)

        #Button is created which when clicked performs the respective operations
        self.btn_add = QPushButton("+",self)
        self.btn_add.move(50,500)
        self.btn_add.resize(200,50)
        self.btn_add.clicked.connect(self.btn_clicked_add)

        self.btn_sub = QPushButton("-",self)
        self.btn_sub.move(250,500)
        self.btn_sub.resize(200,50)
        self.btn_sub.clicked.connect(self.btn_clicked_sub)

        self.btn_mul = QPushButton("*",self)
        self.btn_mul.move(450,500)
        self.btn_mul.resize(200,50)
        self.btn_mul.clicked.connect(self.btn_clicked_mul)

        self.btn_div = QPushButton("/",self)
        self.btn_div.move(650,500)
        self.btn_div.resize(200,50)
        self.btn_div.clicked.connect(self.btn_clicked_div)

        self.btn_clr = QPushButton("clear",self)
        self.btn_clr.move(350,600)
        self.btn_clr.resize(200,50)
        self.btn_clr.clicked.connect(self.btn_clicked_clr)

    #the value entered when clicking the "ENTER THE NUMBER" button is placed the the respective textbox
    def num1_clk(self):

        n1,tf = QInputDialog.getInt(self,"Input","Enter number 1:")
        self.edt_box1.setText(str(n1))

    def num2_clk(self):
       
        n2,tf = QInputDialog.getInt(self,"Input","Enter number 2:")
        self.edt_box2.setText(str(n2))

    #these slots get called when signals are emitted
    def btn_clicked_add(self):

        a = self.edt_box1.text()
        b = self.edt_box2.text()
        c = int(a) + int(b)
        self.edt_boxres.setText(str(c))

    def btn_clicked_sub(self):

        a = self.edt_box1.text()
        b = self.edt_box2.text()
        c = int(a) - int(b)
        self.edt_boxres.setText(str(c))

    def btn_clicked_mul(self):

        a = self.edt_box1.text()
        b = self.edt_box2.text()
        c = int(a) * int(b)
        self.edt_boxres.setText(str(c))

    def btn_clicked_div(self):

        a = self.edt_box1.text()
        b = self.edt_box2.text()
        c = int(a) / int(b)
        self.edt_boxres.setText(str(c))

    def btn_clicked_clr(self):

        a = self.edt_box1.clear()
        b = self.edt_box2.clear()
        c = self.edt_boxres.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = Window()
    dlg.show()
    app.exec_()