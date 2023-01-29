import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MYGUI")
        self.resize(500,210)

        #creating a textbox
        self.edt_box = QLineEdit("", self)
        self.edt_box.setPlaceholderText("")
        self.edt_box.move(0,0)
        self.edt_box.resize(500,50) 
       
        #creating buttons 
        self.btn_sev = QPushButton("7",self)
        self.btn_sev.move(0,60)
        self.btn_sev.clicked.connect(self.btn_clicked_sev)

        self.btn_eig = QPushButton("8",self)
        self.btn_eig.move(100,60)
        self.btn_eig.clicked.connect(self.btn_clicked_eig)

        self.btn_nin = QPushButton("9",self)
        self.btn_nin.move(200,60)
        self.btn_nin.clicked.connect(self.btn_clicked_nin)

        self.btn_div = QPushButton("/",self)
        self.btn_div.move(300,60)
        self.btn_div.clicked.connect(self.btn_clicked_div)

        self.btn_clr = QPushButton("clr",self)
        self.btn_clr.move(400,60)
        self.btn_clr.clicked.connect(self.btn_clicked_clr)

        self.btn_for = QPushButton("4",self)
        self.btn_for.move(0,100)
        self.btn_for.clicked.connect(self.btn_clicked_for)

        self.btn_fiv = QPushButton("5",self)
        self.btn_fiv.move(100,100)
        self.btn_fiv.clicked.connect(self.btn_clicked_fiv)

        self.btn_six = QPushButton("6",self)
        self.btn_six.move(200,100)
        self.btn_six.clicked.connect(self.btn_clicked_six)

        self.btn_mul = QPushButton("*",self)
        self.btn_mul.move(300,100)
        self.btn_mul.clicked.connect(self.btn_clicked_mul)

        self.btn_sq = QPushButton("^",self)
        self.btn_sq.move(400,100)
        self.btn_sq.clicked.connect(self.btn_clicked_sq)
       
        self.btn_one = QPushButton("1",self)
        self.btn_one.move(0,140)
        self.btn_one.clicked.connect(self.btn_clicked_one)

        self.btn_two = QPushButton("2",self)
        self.btn_two.move(100,140)
        self.btn_two.clicked.connect(self.btn_clicked_two)

        self.btn_three = QPushButton("3",self)
        self.btn_three.move(200,140)
        self.btn_three.clicked.connect(self.btn_clicked_three)

        self.btn_sub = QPushButton("-",self)
        self.btn_sub.move(300,140)
        self.btn_sub.clicked.connect(self.btn_clicked_sub)

        self.btn_mod = QPushButton("%",self)
        self.btn_mod.move(400,140)
        self.btn_mod.clicked.connect(self.btn_clicked_mod)

        self.btn_zero = QPushButton("0",self)
        self.btn_zero.move(0,180)
        self.btn_zero.clicked.connect(self.btn_clicked_zero)

        self.btn_dot = QPushButton(".",self)
        self.btn_dot.move(100,180)
        self.btn_dot.clicked.connect(self.btn_clicked_dot)

        self.btn_eq = QPushButton("=",self)
        self.btn_eq.move(200,180)
        self.btn_eq.clicked.connect(self.btn_clicked_eq)

        self.btn_add = QPushButton("+",self)
        self.btn_add.move(300,180)
        self.btn_add.clicked.connect(self.btn_clicked_add)

        self.btn_flr = QPushButton("//",self)
        self.btn_flr.move(400,180)
        self.btn_flr.clicked.connect(self.btn_clicked_flr)

    
    #the functionality of each button is written
    def btn_clicked_sev(self):
        a = self.edt_box.text()
        self.edt_box.setText(a + "7")

    def btn_clicked_eig(self):
        a = self.edt_box.text()
        self.edt_box.setText(a + "8")

    def btn_clicked_nin(self):
        a = self.edt_box.text()
        self.edt_box.setText(a + "9")

    def btn_clicked_div(self):
        a = self.edt_box.text()
        self.edt_box.setText(a + "/")

    def btn_clicked_clr(self):
        a = self.edt_box.clear()

    def btn_clicked_for(self):
        a = self.edt_box.text()
        self.edt_box.setText(a + "4")

    def btn_clicked_fiv(self):
        a = self.edt_box.text()
        self.edt_box.setText(a + "5")

    def btn_clicked_six(self):
        a = self.edt_box.text()
        self.edt_box.setText(a + "6")

    def btn_clicked_mul(self):
        a = self.edt_box.text()
        self.edt_box.setText(a + "*")

    def btn_clicked_sq(self):
        a = self.edt_box.text()
        self.edt_box.setText(a + "**")

    def btn_clicked_one(self):
        a = self.edt_box.text()
        self.edt_box.setText(a + "1")

    def btn_clicked_two(self):
        a = self.edt_box.text()
        self.edt_box.setText(a + "2")

    def btn_clicked_three(self):
        a = self.edt_box.text()
        self.edt_box.setText(a + "3")

    def btn_clicked_sub(self):
        a = self.edt_box.text()
        self.edt_box.setText(a + "-")

    def btn_clicked_mod(self):
        a = self.edt_box.text()
        self.edt_box.setText(a + "%")

    def btn_clicked_zero(self):
        a = self.edt_box.text()
        self.edt_box.setText(a + "0")

    def btn_clicked_dot(self):
        a = self.edt_box.text()
        self.edt_box.setText(a + ".")

    def btn_clicked_eq(self):
        a = eval(self.edt_box.text())
        self.edt_box.setText(str(a))

    def btn_clicked_add(self):
        a = self.edt_box.text()
        self.edt_box.setText(a + "+")

    def btn_clicked_flr(self):
        a = self.edt_box.text()
        self.edt_box.setText(a + "//")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = Window()
    dlg.show()
    app.exec_()
