# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(517, 507)
        MainWindow.setMaximumSize(QtCore.QSize(517, 507))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 30, 451, 51))
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.btn1 = QtGui.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(30, 120, 71, 51))
        self.btn1.setObjectName(_fromUtf8("btn1"))
        self.btn2 = QtGui.QPushButton(self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(120, 120, 71, 51))
        self.btn2.setObjectName(_fromUtf8("btn2"))
        self.btn3 = QtGui.QPushButton(self.centralwidget)
        self.btn3.setGeometry(QtCore.QRect(220, 120, 71, 51))
        self.btn3.setObjectName(_fromUtf8("btn3"))
        self.btn4 = QtGui.QPushButton(self.centralwidget)
        self.btn4.setGeometry(QtCore.QRect(30, 200, 71, 51))
        self.btn4.setObjectName(_fromUtf8("btn4"))
        self.btn5 = QtGui.QPushButton(self.centralwidget)
        self.btn5.setGeometry(QtCore.QRect(120, 200, 71, 51))
        self.btn5.setObjectName(_fromUtf8("btn5"))
        self.btn6 = QtGui.QPushButton(self.centralwidget)
        self.btn6.setGeometry(QtCore.QRect(220, 200, 71, 51))
        self.btn6.setObjectName(_fromUtf8("btn6"))
        self.btn7 = QtGui.QPushButton(self.centralwidget)
        self.btn7.setGeometry(QtCore.QRect(30, 280, 71, 51))
        self.btn7.setObjectName(_fromUtf8("btn7"))
        self.btn8 = QtGui.QPushButton(self.centralwidget)
        self.btn8.setGeometry(QtCore.QRect(120, 280, 71, 51))
        self.btn8.setObjectName(_fromUtf8("btn8"))
        self.btn9 = QtGui.QPushButton(self.centralwidget)
        self.btn9.setGeometry(QtCore.QRect(220, 280, 71, 51))
        self.btn9.setObjectName(_fromUtf8("btn9"))
        self.btn0 = QtGui.QPushButton(self.centralwidget)
        self.btn0.setGeometry(QtCore.QRect(30, 360, 71, 51))
        self.btn0.setObjectName(_fromUtf8("btn0"))
        self.btnsum = QtGui.QPushButton(self.centralwidget)
        self.btnsum.setGeometry(QtCore.QRect(360, 120, 99, 41))
        self.btnsum.setObjectName(_fromUtf8("btnsum"))
        self.btnres = QtGui.QPushButton(self.centralwidget)
        self.btnres.setGeometry(QtCore.QRect(360, 170, 99, 41))
        self.btnres.setObjectName(_fromUtf8("btnres"))
        self.btnmul = QtGui.QPushButton(self.centralwidget)
        self.btnmul.setGeometry(QtCore.QRect(360, 220, 99, 41))
        self.btnmul.setObjectName(_fromUtf8("btnmul"))
        self.btndiv = QtGui.QPushButton(self.centralwidget)
        self.btndiv.setGeometry(QtCore.QRect(360, 270, 99, 41))
        self.btndiv.setObjectName(_fromUtf8("btndiv"))
        self.btnmod = QtGui.QPushButton(self.centralwidget)
        self.btnmod.setGeometry(QtCore.QRect(360, 320, 99, 41))
        self.btnmod.setObjectName(_fromUtf8("btnmod"))
        self.btnpot = QtGui.QPushButton(self.centralwidget)
        self.btnpot.setGeometry(QtCore.QRect(360, 370, 99, 41))
        self.btnpot.setObjectName(_fromUtf8("btnpot"))
        self.btnigual = QtGui.QPushButton(self.centralwidget)
        self.btnigual.setGeometry(QtCore.QRect(220, 360, 71, 51))
        self.btnigual.setObjectName(_fromUtf8("btnigual"))
        self.btnp = QtGui.QPushButton(self.centralwidget)
        self.btnp.setGeometry(QtCore.QRect(120, 360, 71, 51))
        self.btnp.setObjectName(_fromUtf8("btnp"))
        self.btnborrar = QtGui.QPushButton(self.centralwidget)
        self.btnborrar.setGeometry(QtCore.QRect(360, 420, 99, 41))
        self.btnborrar.setObjectName(_fromUtf8("btnborrar"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 517, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.btnborrar, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculadora", None))
        self.btn1.setText(_translate("MainWindow", "1", None))
        self.btn2.setText(_translate("MainWindow", "2", None))
        self.btn3.setText(_translate("MainWindow", "3", None))
        self.btn4.setText(_translate("MainWindow", "4", None))
        self.btn5.setText(_translate("MainWindow", "5", None))
        self.btn6.setText(_translate("MainWindow", "6", None))
        self.btn7.setText(_translate("MainWindow", "7", None))
        self.btn8.setText(_translate("MainWindow", "8", None))
        self.btn9.setText(_translate("MainWindow", "9", None))
        self.btn0.setText(_translate("MainWindow", "0", None))
        self.btnsum.setText(_translate("MainWindow", "+", None))
        self.btnres.setText(_translate("MainWindow", "-", None))
        self.btnmul.setText(_translate("MainWindow", "*", None))
        self.btndiv.setText(_translate("MainWindow", "/", None))
        self.btnmod.setText(_translate("MainWindow", "%", None))
        self.btnpot.setText(_translate("MainWindow", "^", None))
        self.btnigual.setText(_translate("MainWindow", "⁼", None))
        self.btnp.setText(_translate("MainWindow", ".", None))
        self.btnborrar.setText(_translate("MainWindow", "AC", None))
    def conectar(self, MainWindow):
        self.connect(self.btn0, QtCore.SIGNAL("clicked()"),lambda:self.aniadir('0'))
        self.connect(self.btn1, QtCore.SIGNAL("clicked()"),lambda:self.aniadir('1'))
        self.connect(self.btn2, QtCore.SIGNAL("clicked()"),lambda:self.aniadir('2'))
        self.connect(self.btn3, QtCore.SIGNAL("clicked()"),lambda:self.aniadir('3'))
        self.connect(self.btn4, QtCore.SIGNAL("clicked()"),lambda:self.aniadir('4'))
        self.connect(self.btn5, QtCore.SIGNAL("clicked()"),lambda:self.aniadir('5'))
        self.connect(self.btn6, QtCore.SIGNAL("clicked()"),lambda:self.aniadir('6'))
        self.connect(self.btn7, QtCore.SIGNAL("clicked()"),lambda:self.aniadir('7'))
        self.connect(self.btn8, QtCore.SIGNAL("clicked()"),lambda:self.aniadir('8'))
        self.connect(self.btn9, QtCore.SIGNAL("clicked()"),lambda:self.aniadir('9'))
        self.connect(self.btnsum, QtCore.SIGNAL("clicked()"),lambda:self.aniadir('+'))
        self.connect(self.btnres, QtCore.SIGNAL("clicked()"),lambda:self.aniadir('-'))
        self.connect(self.btnmul, QtCore.SIGNAL("clicked()"),lambda:self.aniadir('*'))
        self.connect(self.btndiv, QtCore.SIGNAL("clicked()"),lambda:self.aniadir('/'))
        self.connect(self.btnmod, QtCore.SIGNAL("clicked()"),lambda:self.aniadir('%'))
        self.connect(self.btnpot, QtCore.SIGNAL("clicked()"),lambda:self.aniadir('^'))
        self.connect(self.btnigual, QtCore.SIGNAL("clicked()"),self.evaluar)
        self.connect(self.btnp, QtCore.SIGNAL("clicked()"),lambda:self.aniadir('.'))

    def aniadir(self,que):
        actual = self.lneStack.text()
        self.lneStack.setText(actual + que)
        
    def evaluar(self):
        expr = self.lneStack.text()
        resultado = eval(str(expr))
        if type(resultado) in [float,int]:
            self.lneStack.setText(str(resultado))



if __name__ == "__main__":
    
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

