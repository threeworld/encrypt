# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import base64,sys
from PyQt5 import QtCore, QtGui, QtWidgets
from des import DES
from des import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(447, 354)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 461, 351))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(110, 170, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 170, 81, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(70, 50, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(12)
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(130, 50, 191, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setFont(font)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(70, 110, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setObjectName("label_2")
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(12)
        self.textEdit_2 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_2.setGeometry(QtCore.QRect(130, 110, 191, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setFont(font)
        self.textEdit_3 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_3.setGeometry(QtCore.QRect(30, 230, 391, 81))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_3.setFont(font)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(33, 201, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.pushButton.clicked.connect(self.encrypt)
        self.pushButton_2.clicked.connect(self.decrypt)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "DES加密/解密"))
        self.pushButton.setText(_translate("Form", "加密"))
        self.pushButton_2.setText(_translate("Form", "解密"))
        self.label.setText(_translate("Form", "明文："))
        self.label_2.setText(_translate("Form", "密钥："))
        self.label_3.setText(_translate("Form", "密文："))

    def encrypt(self):
        text = self.textEdit.toPlainText()
        key = self.textEdit_2.toPlainText()
        print(key)
        print(text)
        des = DES()
        encrypt_text = des.encrypt(key, text)
        print(base64.b64encode(encrypt_text))
        self.textEdit_3.setText(str(base64.b64encode(encrypt_text))[2:-2])

    def decrypt(self):
        key = self.textEdit_2.toPlainText()
        encrypt_text = self.textEdit_3.toPlainText()
        encrypt_text_ = base64.b64decode(encrypt_text.encode('utf-8'))
        des = DES()
        decrypt_text = des.decrypt(key, encrypt_text_)

if __name__=="__main__":

    app=QtWidgets.QApplication(sys.argv)
    widget=QtWidgets.QWidget()
    ui=Ui_Form()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
