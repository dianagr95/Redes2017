# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Error.ui'
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

class Ui_Error(object):
    def setupUi(self, Error):
        Error.setObjectName(_fromUtf8("Error"))
        Error.resize(400, 178)
        Error.setMaximumSize(QtCore.QSize(400, 178))
        self.centralwidget = QtGui.QWidget(Error)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 20, 68, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(47, 50, 281, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 90, 99, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        Error.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Error)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Error.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Error)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Error.setStatusBar(self.statusbar)

        self.retranslateUi(Error)
        QtCore.QMetaObject.connectSlotsByName(Error)

    def retranslateUi(self, Error):
        Error.setWindowTitle(_translate("Error", "MainWindow", None))
        self.label.setText(_translate("Error", "Error", None))
        self.label_2.setText(_translate("Error", "El usuario o la contraseña no coinciden", None))
        self.pushButton.setText(_translate("Error", "Aceptar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Error = QtGui.QMainWindow()
    ui = Ui_Error()
    ui.setupUi(Error)
    Error.show()
    sys.exit(app.exec_())

