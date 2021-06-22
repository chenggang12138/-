import sys

import numpy as np
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit, QInputDialog, QMainWindow, QTextEdit, QLabel


import qtp7 as p7
import qtp1 as p1
import qtp4 as p4

class compare(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.qbtna = QPushButton("输入明文值a",self)
        self.qbtna.resize(120, 40)
        self.qbtna.move(40, 30)
        self.lea = QLineEdit(self)
        self.lea.resize(120,40)
        self.lea.move(180, 30)


        self.qbtnb = QPushButton("输入明文值b", self)
        self.qbtnb.resize(120, 40)
        self.qbtnb.move(40, 70)
        self.leb = QLineEdit(self)
        self.leb.resize(120, 40)
        self.leb.move(180, 70)

        self.qbtnc = QPushButton("COMPARE:a<b", self)
        self.qbtnc.resize(120, 40)
        self.qbtnc.move(140, 170)
        self.lec = QLineEdit(self)
        self.lec.resize(50, 40)
        self.lec.move(300, 170)
        self.qbtnc.clicked.connect(self.onButtonClick)

        self.setGeometry(1050, 250, 450, 550)
        self.setWindowTitle('Compare encrypted data')
    def onButtonClick(self):
        self.a = self.lea.text()
        self.b = self.leb.text()
        int_a = int(self.a)
        int_b = int(self.b)
        c = p7.protocol7(int_a,int_b)
        #print(self.a,self.b,"asf",c)
        if c[0] == "1":
            self.lec.setText("1")
        else:
            self.lec.setText("0")

class  argmax(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.qbtna = QPushButton("输入明文值(逗号将数据隔开）", self)
        self.qbtna.resize(250, 40)
        self.qbtna.move(200, 30)

        self.lea = QLineEdit(self)
        self.lea.resize(500, 40)
        self.lea.move(100, 100)

        self.qbtnb = QPushButton("寻找", self)
        self.qbtnb.clicked.connect(self.onButtonClick)
        self.qbtnb.resize(120, 40)
        self.qbtnb.move(200, 200)

        self.leb = QLineEdit(self)
        self.leb.resize(50, 40)
        self.leb.move(400, 200)

        self.setGeometry(1050, 250, 750, 700)
        self.setWindowTitle('argmax over encrypted data')
    def onButtonClick(self):
        st = self.lea.text()
        k = len(st)
        t = []
        temp = ""
        print(k)
        j = 0
        st = str(st)
        for i in range(k):
            if st[i] != ',' and st[i] != '，':
                #print("dou")
                temp = str(temp) + str(st[i])
            else:
                t.append(temp)
                temp = ""
        t.append(temp)
        #print(t)
        int_t = [int(x) for x in t]
        l = int_t[0].bit_length()
        #print(int_t,l)
        max = p1.protocol1(int_t,l)
        self.leb.setText(str(max))

class hyperplane(QMainWindow):


    def __init__(self):
        super(hyperplane,self).__init__()
        self.initUI()


    def initUI(self):
        self.setObjectName("MainWindow")
        self.setStyleSheet("#MainWindow{border-image:url(picture.png);}")
        self.qbtna = QLabel("待分类数据X中的特征值个数:", self)
        self.qbtna.setFont(QFont("华文琥珀", 12, QFont.Bold))
        self.qbtna.setAlignment(Qt.AlignRight)
        self.qbtna.resize(280, 40)
        self.qbtna.move(90, 40)
        self.lea = QLineEdit(self)
        self.lea.resize(120, 40)
        self.lea.move(400, 30)
        self.lea.setFont(QFont("华文琥珀", 20, QFont.Bold))
        #self.lea.setStyleSheet("color:red")
        #self.lea.setStyleSheet("background-color:yellow")


        self.qbtnb = QLabel("    现有模型W中的类别个数:", self)
        self.qbtnb.setFont(QFont("华文琥珀", 12, QFont.Bold))
        self.qbtnb.setAlignment(Qt.AlignRight)

        self.qbtnb.resize(270, 40)
        self.qbtnb.move(100, 110)
        self.leb = QLineEdit(self)
        self.leb.resize(120, 40)
        self.leb.move(400, 100)
        self.leb.setFont(QFont("华文琥珀", 20, QFont.Bold))
        #self.leb.setStyleSheet("color:red")
        #self.leb.setStyleSheet("background-color:yellow")

        self.qbtnc = QLabel("分类结果:", self)
        self.qbtnc.setFont(QFont("华文琥珀", 12, QFont.Bold))
        self.qbtnc.setAlignment(Qt.AlignRight)
        self.qbtnc.resize(160, 40)
        self.qbtnc.move(210, 480)
        self.qbtng = QLabel("第", self)
        self.qbtng.setFont(QFont("华文琥珀", 12, QFont.Bold))
        self.qbtng.resize(30, 40)
        self.qbtng.move(400, 470)
        self.qbtnh = QLabel("类", self)
        self.qbtnh.setFont(QFont("华文琥珀", 12, QFont.Bold))
        self.qbtnh.resize(30, 40)
        self.qbtnh.move(500, 470)

        self.lec = QLineEdit(self)
        self.lec.resize(60, 40)
        self.lec.move(430, 470)
        self.lec.setFont(QFont("华文琥珀", 20, QFont.Bold))
        #self.lec.setStyleSheet("color:red")
        #self.lec.setStyleSheet("background-color:gray")
        #self.qbtnc.clicked.connect(self.onButtonClickc)
        """self.qbtnc.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:red;}''')"""

        self.qbtnd = QLabel("  随机产生的待分类数据X:", self)
        self.qbtnd.setFont(QFont("华文琥珀", 12, QFont.Bold))
        self.qbtnd.setAlignment(Qt.AlignRight)
        self.qbtnd.resize(270, 40)
        self.qbtnd.move(100, 250)
        self.led = QLineEdit(self)
        self.led.resize(320, 40)
        self.led.move(400, 240)
        self.led.setFont(QFont ("华文琥珀",20,QFont.Bold))
        #self.led.setStyleSheet("color:red")
        #self.led.setStyleSheet("background-color:gray")
        #self.qbtnd.clicked.connect(self.onButtonClickd)
        """self.qbtnd.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')"""

        self.qbtne = QLabel("随机产生的模型W:", self)
        self.qbtne.setFont(QFont("华文琥珀", 12, QFont.Bold))
        self.qbtne.setAlignment(Qt.AlignRight)
        self.qbtne.resize(270, 40)
        self.qbtne.move(100, 310)
        self.lee = QTextEdit(self)
        self.lee.resize(320, 120)
        self.lee.move(400, 300)
        self.lee.setFont(QFont("华文琥珀", 15, QFont.Bold))
        #self.lee.setStyleSheet("color:red")
        #self.lee.setStyleSheet("background-color:gray")
        #self.qbtne.clicked.connect(self.onButtonClicke)
        """self.qbtne.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')"""

        self.qbtnf = QPushButton("处理", self)
        self.qbtnf.setFont(QFont("华文琥珀", 12, QFont.Bold))
        self.qbtnf.resize(160, 40)
        self.qbtnf.move(300, 550)
        self.qbtnf.clicked.connect(self.onButtonClickf)


        self.setGeometry(1050, 250, 800, 600)
        self.setWindowTitle('Private hyperplane decision')

    """def onButtonClickd(self):
        sta = self.lea.text()
        self.int_sta =  int(sta)
        x = np.random.randint(256, size=self.int_sta)
        self.x1 = [int(i) for i in x]
        self.led.setText(str(self.x1))

    def onButtonClicke(self):
        stb = self.leb.text()
        self.int_stb = int(stb)
        self.w = [[0] * self.int_sta] * self.int_stb
        for i in range(self.int_stb):
            self.w[i] = np.random.randint(256, size=self.int_sta)
            self.w[i] = [int(j) for j in self.w[i]]
        self.lee.setPlainText(str(self.w))

    def onButtonClickc(self):
        i = p4.protocol4(self.x1,self.w)
        self.lec.setText(str(i))"""

    def onButtonClickf(self):
        sta = self.lea.text()
        self.int_sta = int(sta)
        x = np.random.randint(256, size=self.int_sta)
        self.x1 = [int(i) for i in x]
        self.led.setText(str(self.x1))

        stb = self.leb.text()
        self.int_stb = int(stb)
        self.w = [[0] * self.int_sta] * self.int_stb
        for i in range(self.int_stb):
            self.w[i] = np.random.randint(256, size=self.int_sta)
            self.w[i] = [int(j) for j in self.w[i]]
        self.lee.setPlainText(str(self.w))

        i = p4.protocol4(self.x1, self.w)
        self.lec.setText(str(i))










class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(180,40)
        qbtn.move(170, 450)

        self.qbtn1 = QPushButton('比较两个加密数据', self)
        #qbtn1.clicked.connect()
        self.qbtn1.resize(180, 40)
        self.qbtn1.move(170, 30)

        self.qbtn2 = QPushButton('求解加密数组最大值位置', self)
        self.qbtn2.resize(180, 40)
        self.qbtn2.move(170, 100)

        self.qbtn3 = QPushButton('超平面决策分类器', self)
        self.qbtn3.resize(180, 40)
        self.qbtn3.move(170, 170)

        self.setGeometry(250, 250, 550, 550)
        self.setWindowTitle('超平面决策分类器')
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    cp = compare()
    argmax = argmax()
    hy = hyperplane()

    ex.qbtn1.clicked.connect(cp.show)
    ex.qbtn2.clicked.connect(argmax.show)
    ex.qbtn3.clicked.connect(hy.show)
    sys.exit(app.exec_())