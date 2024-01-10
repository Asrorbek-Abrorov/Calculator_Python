import sys
from os import system

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

system("clear")


class Dastur(QMainWindow):
    def __init__(forma):
        super().__init__()
        QMainWindow.__init__(forma)
        forma.label = None
        forma.setWindowTitle("Iphone 15 Pro Max")
        forma.setGeometry(1455, 30, 360, 670)
        forma.UiComponents()
        forma.show()

        forma.setStyleSheet("""background-color: black;
                            color: azure;
                            font-size: 20pt;
                            """)

    def UiComponents(forma):

        forma.label = QLabel(forma)

        forma.label.setGeometry(5, 180, 325, 70)

        forma.label.setWordWrap(True)

        forma.label.setStyleSheet("""
                                  background : black;
                                  font-size: 60px""")

        forma.label.setAlignment(Qt.AlignRight)

        ac = QPushButton("AC", forma)
        ac.setGeometry(25, 260, 70, 70)
        ac.setStyleSheet("""background-color : rgb(147, 145, 141);
                        color: azure;
                        border-radius : 35px;""")

        ishora = QPushButton("+/-", forma)
        ishora.setGeometry(105, 260, 70, 70)
        ishora.setStyleSheet("""background-color : rgb(147, 145, 141);
                        color: azure;
                        border-radius : 35px;""")

        foiz = QPushButton("%", forma)
        foiz.setGeometry(185, 260, 70, 70)
        foiz.setStyleSheet("""background-color : rgb(147, 145, 141);
                            color: azure;
                            border-radius : 35px;""")

        bolish = QPushButton("/", forma)
        bolish.setGeometry(265, 260, 70, 70)
        bolish.setStyleSheet("""background-color : rgb(208, 137, 13);
                        color: azure;
                        border-radius : 35px;""")

        yetti = QPushButton("7", forma)
        yetti.setGeometry(25, 340, 70, 70)
        yetti.setStyleSheet("""background-color : rgb(58, 57, 55);
                        color: azure;
                        border-radius : 35px;""")

        sakiz = QPushButton("8", forma)
        sakiz.setGeometry(105, 340, 70, 70)
        sakiz.setStyleSheet("""background-color : rgb(58, 57, 55);
                        color: azure;
                        border-radius : 35px;""")

        toqqiz = QPushButton("9", forma)
        toqqiz.setGeometry(185, 340, 70, 70)
        toqqiz.setStyleSheet("""background-color : rgb(58, 57, 55);
                        color: azure;
                        border-radius : 35px;""")

        kopaytirma = QPushButton("x", forma)
        kopaytirma.setGeometry(265, 340, 70, 70)
        kopaytirma.setStyleSheet("""background-color : rgb(208, 137, 13);
                        color: azure;
                        border-radius : 35px;""")

        tort = QPushButton("4", forma)
        tort.setGeometry(25, 415, 70, 70)
        tort.setStyleSheet("""background-color : rgb(58, 57, 55);
                        color: azure;
                        border-radius : 35px;""")

        besh = QPushButton("5", forma)
        besh.setGeometry(105, 415, 70, 70)
        besh.setStyleSheet("""background-color : rgb(58, 57, 55);
                        color: azure;
                        border-radius : 35px;""")

        olti = QPushButton("6", forma)
        olti.setGeometry(185, 415, 70, 70)
        olti.setStyleSheet("""background-color : rgb(58, 57, 55);
                        color: azure;
                        border-radius : 35px;""")

        ayirma = QPushButton("-", forma)
        ayirma.setGeometry(265, 415, 70, 70)
        ayirma.setStyleSheet("""background-color : rgb(208, 137, 13);
                        color: azure;
                        border-radius : 35px;""")

        bir = QPushButton("1", forma)
        bir.setGeometry(25, 490, 70, 70)
        bir.setStyleSheet("""background-color : rgb(58, 57, 55);
                        color: azure;
                        border-radius : 35px;""")

        ikki = QPushButton("2", forma)
        ikki.setGeometry(105, 490, 70, 70)
        ikki.setStyleSheet("""background-color : rgb(58, 57, 55);
                        color: azure;
                        border-radius : 35px;""")

        uch = QPushButton("3", forma)
        uch.setGeometry(185, 490, 70, 70)
        uch.setStyleSheet("""background-color : rgb(58, 57, 55);
                        color: azure;
                        border-radius : 35px;""")

        qoshish = QPushButton("+", forma)
        qoshish.setGeometry(265, 490, 70, 70)
        qoshish.setStyleSheet("""background-color : rgb(208, 137, 13);
                        color: azure;
                        border-radius : 35px;""")

        nol = QPushButton("0          ", forma)
        nol.setGeometry(25, 565, 150, 70)
        nol.setStyleSheet("""background-color : rgb(58, 57, 55);
                        color: azure;
                        border-radius : 35px;""")

        nuqta = QPushButton(".", forma)
        nuqta.setGeometry(185, 565, 70, 70)
        nuqta.setStyleSheet("""background-color : rgb(58, 57, 55);
                        color: azure;
                        border-radius : 35px;""")

        teng = QPushButton("=", forma)
        teng.setGeometry(265, 565, 70, 70)
        teng.setStyleSheet("""background-color : rgb(208, 137, 13);
                        color: azure;
                        border-radius : 35px;""")

        ayirma.clicked.connect(forma.action_ayirish)
        teng.clicked.connect(forma.action_teng)
        bolish.clicked.connect(forma.action_bolish)
        kopaytirma.clicked.connect(forma.action_kopaytirish)
        qoshish.clicked.connect(forma.action_qoshish)
        ac.clicked.connect(forma.action_ac)
        ishora.clicked.connect(forma.action_belgi)
        foiz.clicked.connect(forma.action_foiz)
        nuqta.clicked.connect(forma.action_nuqta)
        nol.clicked.connect(forma.action0)
        bir.clicked.connect(forma.action1)
        ikki.clicked.connect(forma.action2)
        uch.clicked.connect(forma.action3)
        tort.clicked.connect(forma.action4)
        besh.clicked.connect(forma.action5)
        olti.clicked.connect(forma.action6)
        yetti.clicked.connect(forma.action7)
        sakiz.clicked.connect(forma.action8)
        toqqiz.clicked.connect(forma.action9)

    def action_teng(forma):
        tenglik = forma.label.text()

        try:
            ans = eval(tenglik)

            forma.label.setText(str(ans))

        except:
            forma.label.setText("Wrong Input")

    def action_qoshish(forma):
        text = forma.label.text()
        forma.label.setText(text + " + ")

    def action_ayirish(forma):
        text = forma.label.text()
        forma.label.setText(text + " - ")

    def action_bolish(forma):
        text = forma.label.text()
        forma.label.setText(text + " / ")

    def action_kopaytirish(forma):
        text = forma.label.text()
        forma.label.setText(text + " * ")

    def action_foiz(forma):
        text = forma.label.text()
        forma.label.setText(text + " //100 ")

    def action_belgi(forma):
        text = forma.label.text()
        forma.label.setText(text + " +/- ")

    def action_nuqta(forma):
        text = forma.label.text()
        forma.label.setText(text + ".")

    def action0(forma):
        text = forma.label.text()
        forma.label.setText(text + "0")

    def action1(forma):
        text = forma.label.text()
        forma.label.setText(text + "1")

    def action2(forma):
        text = forma.label.text()
        forma.label.setText(text + "2")

    def action3(forma):
        text = forma.label.text()
        forma.label.setText(text + "3")

    def action4(forma):
        text = forma.label.text()
        forma.label.setText(text + "4")

    def action5(forma):
        text = forma.label.text()
        forma.label.setText(text + "5")

    def action6(forma):
        text = forma.label.text()
        forma.label.setText(text + "6")

    def action7(forma):
        text = forma.label.text()
        forma.label.setText(text + "7")

    def action8(forma):
        text = forma.label.text()
        forma.label.setText(text + "8")

    def action9(forma):
        text = forma.label.text()
        forma.label.setText(text + "9")

    def action_ac(forma):
        forma.label.setText("")


app = QApplication([])
dastur = Dastur()
sys.exit(app.exec_())
