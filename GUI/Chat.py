# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Chat.ui'
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

class Ui_Chat(object):
    def setupUi(self, Chat):
        Chat.setObjectName(_fromUtf8("Chat"))
        Chat.resize(535, 430)
        self.centralwidget = QtGui.QWidget(Chat)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(420, 330, 99, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(40, 280, 361, 78))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(49, 50, 371, 201))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 369, 199))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        Chat.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Chat)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 535, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Chat.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Chat)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Chat.setStatusBar(self.statusbar)

        self.retranslateUi(Chat)
        QtCore.QMetaObject.connectSlotsByName(Chat)

    def retranslateUi(self, Chat):
        Chat.setWindowTitle(_translate("Chat", "Chat", None))
        self.pushButton.setText(_translate("Chat", "Enviar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Chat = QtGui.QMainWindow()
    ui = Ui_Chat()
    ui.setupUi(Chat)
    Chat.show()
    sys.exit(app.exec_())

