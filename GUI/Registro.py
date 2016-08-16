# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Registro.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

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

class Ui_Registro(object):
    def setupUi(self, Registro):
        Registro.setObjectName(_fromUtf8("Registro"))
        Registro.resize(510, 328)
        Registro.setMaximumSize(QtCore.QSize(510, 328))
        self.centralwidget = QtGui.QWidget(Registro)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 180, 99, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 121, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 121, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 50, 211, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 130, 211, 27))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        Registro.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Registro)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 510, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Registro.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Registro)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Registro.setStatusBar(self.statusbar)

        self.retranslateUi(Registro)
        QtCore.QMetaObject.connectSlotsByName(Registro)

    def retranslateUi(self, Registro):
        Registro.setWindowTitle(_translate("Registro", "MainWindow", None))
        self.pushButton.setText(_translate("Registro", "Registrar", None))
        self.label.setText(_translate("Registro", "Nuevo usuario", None))
        self.label_2.setText(_translate("Registro", "Nueva contraseña", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Registro = QtGui.QMainWindow()
    ui = Ui_Registro()
    ui.setupUi(Registro)
    Registro.show()
    sys.exit(app.exec_())

