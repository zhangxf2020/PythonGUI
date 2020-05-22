# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QWFormDoc.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(635, 346)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(90, 50, 341, 211))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.actOpen = QtWidgets.QAction(Form)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/122.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actOpen.setIcon(icon)
        self.actOpen.setObjectName("actOpen")
        self.actCut = QtWidgets.QAction(Form)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/200.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actCut.setIcon(icon1)
        self.actCut.setObjectName("actCut")
        self.actCopy = QtWidgets.QAction(Form)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/images/202.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actCopy.setIcon(icon2)
        self.actCopy.setObjectName("actCopy")
        self.actPaste = QtWidgets.QAction(Form)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/images/204.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actPaste.setIcon(icon3)
        self.actPaste.setObjectName("actPaste")
        self.actFont = QtWidgets.QAction(Form)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/images/506.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actFont.setIcon(icon4)
        self.actFont.setObjectName("actFont")
        self.actClose = QtWidgets.QAction(Form)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/images/132.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actClose.setIcon(icon5)
        self.actClose.setObjectName("actClose")
        self.actUndo = QtWidgets.QAction(Form)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/images/206.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actUndo.setIcon(icon6)
        self.actUndo.setObjectName("actUndo")
        self.actRedo = QtWidgets.QAction(Form)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/images/208.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actRedo.setIcon(icon7)
        self.actRedo.setObjectName("actRedo")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "new document"))
        self.actOpen.setText(_translate("Form", "打开"))
        self.actCut.setText(_translate("Form", "剪切"))
        self.actCut.setShortcut(_translate("Form", "Ctrl+X"))
        self.actCopy.setText(_translate("Form", "复制"))
        self.actCopy.setShortcut(_translate("Form", "Ctrl+C"))
        self.actPaste.setText(_translate("Form", "粘贴"))
        self.actPaste.setShortcut(_translate("Form", "Ctrl+V"))
        self.actFont.setText(_translate("Form", "字体"))
        self.actClose.setText(_translate("Form", "关闭"))
        self.actUndo.setText(_translate("Form", "撤销"))
        self.actUndo.setShortcut(_translate("Form", "Ctrl+Z"))
        self.actRedo.setText(_translate("Form", "重做"))
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
