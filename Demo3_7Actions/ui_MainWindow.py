# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(723, 442)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 10, 541, 341))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 723, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_E = QtWidgets.QMenu(self.menubar)
        self.menu_E.setObjectName("menu_E")
        self.menu_M = QtWidgets.QMenu(self.menubar)
        self.menu_M.setObjectName("menu_M")
        self.menu_2 = QtWidgets.QMenu(self.menu_M)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setMovable(True)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolBar.setFloatable(True)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actFile_New = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/100.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actFile_New.setIcon(icon)
        self.actFile_New.setObjectName("actFile_New")
        self.actFile_Open = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/001.GIF"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actFile_Open.setIcon(icon1)
        self.actFile_Open.setObjectName("actFile_Open")
        self.actFile_Save = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/images/104.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actFile_Save.setIcon(icon2)
        self.actFile_Save.setObjectName("actFile_Save")
        self.actClose = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/images/132.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actClose.setIcon(icon3)
        self.actClose.setObjectName("actClose")
        self.actEdit_Cut = QtWidgets.QAction(MainWindow)
        self.actEdit_Cut.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/images/200.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actEdit_Cut.setIcon(icon4)
        self.actEdit_Cut.setObjectName("actEdit_Cut")
        self.actEdit_Copy = QtWidgets.QAction(MainWindow)
        self.actEdit_Copy.setEnabled(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/images/202.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actEdit_Copy.setIcon(icon5)
        self.actEdit_Copy.setObjectName("actEdit_Copy")
        self.actEdit_Paste = QtWidgets.QAction(MainWindow)
        self.actEdit_Paste.setEnabled(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/images/204.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actEdit_Paste.setIcon(icon6)
        self.actEdit_Paste.setObjectName("actEdit_Paste")
        self.actEdit_Undo = QtWidgets.QAction(MainWindow)
        self.actEdit_Undo.setEnabled(False)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/images/206.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actEdit_Undo.setIcon(icon7)
        self.actEdit_Undo.setObjectName("actEdit_Undo")
        self.actEdit_Redo = QtWidgets.QAction(MainWindow)
        self.actEdit_Redo.setEnabled(False)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/images/208.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actEdit_Redo.setIcon(icon8)
        self.actEdit_Redo.setObjectName("actEdit_Redo")
        self.actEdit_SelectAll = QtWidgets.QAction(MainWindow)
        self.actEdit_SelectAll.setObjectName("actEdit_SelectAll")
        self.actEdit_Clear = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/images/212.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actEdit_Clear.setIcon(icon9)
        self.actEdit_Clear.setObjectName("actEdit_Clear")
        self.actFont_Bold = QtWidgets.QAction(MainWindow)
        self.actFont_Bold.setCheckable(True)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/images/500.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actFont_Bold.setIcon(icon10)
        self.actFont_Bold.setObjectName("actFont_Bold")
        self.actFont_Italic = QtWidgets.QAction(MainWindow)
        self.actFont_Italic.setCheckable(True)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/images/502.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actFont_Italic.setIcon(icon11)
        self.actFont_Italic.setObjectName("actFont_Italic")
        self.actFont_UnderLine = QtWidgets.QAction(MainWindow)
        self.actFont_UnderLine.setCheckable(True)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/images/504.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actFont_UnderLine.setIcon(icon12)
        self.actFont_UnderLine.setObjectName("actFont_UnderLine")
        self.actSys_ToggleText = QtWidgets.QAction(MainWindow)
        self.actSys_ToggleText.setCheckable(True)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons/images/322.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actSys_ToggleText.setIcon(icon13)
        self.actSys_ToggleText.setObjectName("actSys_ToggleText")
        self.actLang_CN = QtWidgets.QAction(MainWindow)
        self.actLang_CN.setCheckable(True)
        self.actLang_CN.setChecked(True)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icons/images/CN.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actLang_CN.setIcon(icon14)
        self.actLang_CN.setIconVisibleInMenu(True)
        self.actLang_CN.setObjectName("actLang_CN")
        self.actLang_EN = QtWidgets.QAction(MainWindow)
        self.actLang_EN.setCheckable(True)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/icons/images/timg2.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actLang_EN.setIcon(icon15)
        self.actLang_EN.setObjectName("actLang_EN")
        self.menu.addAction(self.actFile_New)
        self.menu.addAction(self.actFile_Open)
        self.menu.addAction(self.actFile_Save)
        self.menu.addSeparator()
        self.menu.addAction(self.actClose)
        self.menu_E.addAction(self.actEdit_Cut)
        self.menu_E.addAction(self.actEdit_Copy)
        self.menu_E.addAction(self.actEdit_Paste)
        self.menu_E.addSeparator()
        self.menu_E.addAction(self.actEdit_Undo)
        self.menu_E.addAction(self.actEdit_Redo)
        self.menu_E.addSeparator()
        self.menu_E.addAction(self.actEdit_SelectAll)
        self.menu_E.addAction(self.actEdit_Clear)
        self.menu_2.addAction(self.actLang_CN)
        self.menu_2.addAction(self.actLang_EN)
        self.menu_M.addAction(self.actFont_Bold)
        self.menu_M.addAction(self.actFont_Italic)
        self.menu_M.addAction(self.actFont_UnderLine)
        self.menu_M.addSeparator()
        self.menu_M.addAction(self.actSys_ToggleText)
        self.menu_M.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_E.menuAction())
        self.menubar.addAction(self.menu_M.menuAction())
        self.toolBar.addAction(self.actFile_New)
        self.toolBar.addAction(self.actFile_Open)
        self.toolBar.addAction(self.actFile_Save)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actEdit_Cut)
        self.toolBar.addAction(self.actEdit_Copy)
        self.toolBar.addAction(self.actEdit_Paste)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actEdit_Undo)
        self.toolBar.addAction(self.actEdit_Redo)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actFont_Bold)
        self.toolBar.addAction(self.actFont_Italic)
        self.toolBar.addAction(self.actFont_UnderLine)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actLang_CN)
        self.toolBar.addAction(self.actLang_EN)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Demo3_7 QAction,QMainWindow,QPlainTextEdit"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "from PyQt5.QtWidgets import QWidget,QApplication\n"
"from PyQt5.QtCore import QTime,QDate,QDateTime\n"
"import sys\n"
"\n"
"from ui_Widget import Ui_Widget\n"
"\n"
"class QmyWidget(QWidget):\n"
"    def __init__(self):\n"
"        super().__init__(parent = None)\n"
"        self.ui = Ui_Widget()\n"
"        self.ui.setupUi(self)\n"
"        print(dir(self.ui))\n"
"        self.ui.calendarWidget.selectionChanged.connect(lambda :print(self.ui.calendarWidget.selectedDate().toString(\'yyyy-MM-dd\')))\n"
"\n"
"    def on_calendarWidget_selectionChanged(self):\n"
"        self.ui.editCalender.setText(self.ui.calendarWidget.selectedDate().toString(\'yyyy年MM月dd日\'))\n"
"\n"
"    def on_btnSetTime_clicked(self):\n"
"        timestr = self.ui.editTime.text()\n"
"        time = QTime.fromString(timestr,\'hh:mm:ss\') #fromstring 将字符串格式时间转换为Qtime对象\n"
"        self.ui.timeEdit.setTime(time)\n"
"    def on_btnSetDate_clicked(self):\n"
"        date = self.ui.editDate.text()\n"
"        qdate = QDate.fromString(date,\'yyyy-MM-dd\')#fromstring 将字符串格式时间转换为Qdate对象\n"
"        self.ui.dateEdit.setDate(qdate)\n"
"\n"
"    def on_btnSetDateTime_clicked(self):\n"
"        datetimeStr = self.ui.editDateTime.text()\n"
"        datetime = QDateTime.fromString(datetimeStr,\'yyyy-MM-dd hh:mm:ss\')#fromstring 将字符串格式时间转换为Qdatetime对象\n"
"        self.ui.dateTimeEdit.setDateTime(datetime)\n"
"    def on_btnGetTime_clicked(self):\n"
"        curDateTime = QDateTime.currentDateTime() #获取当前日期时间并返回一个datetime对象\n"
"\n"
"        self.ui.timeEdit.setTime(curDateTime.time())\n"
"        print(curDateTime.time())\n"
"        self.ui.editTime.setText(curDateTime.time().toString(\'hh:mm:ss\'))#tostring 将Qtime对象转换为字符串格式\n"
"\n"
"        self.ui.dateEdit.setDate(curDateTime.date())\n"
"        self.ui.editDate.setText(curDateTime.date().toString(\'yyyy-MM-dd\'))#tostring 将Qdate对象转换为字符串格式\n"
"\n"
"        self.ui.dateTimeEdit.setDateTime(curDateTime)\n"
"        self.ui.editDateTime.setText(curDateTime.toString(\'yyyy-MM-dd hh:mm:ss\'))#tostring 将Qdatetime对象转换为字符串格式\n"
"\n"
"\n"
"if __name__ == \'__main__\':\n"
"    app = QApplication(sys.argv)\n"
"    form = QmyWidget()\n"
"    form.show()\n"
"    sys.exit(app.exec_())"))
        self.menu.setTitle(_translate("MainWindow", "文件(F)"))
        self.menu_E.setTitle(_translate("MainWindow", "编辑(E)"))
        self.menu_M.setTitle(_translate("MainWindow", "格式(M)"))
        self.menu_2.setTitle(_translate("MainWindow", "界面语言"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actFile_New.setText(_translate("MainWindow", "新建"))
        self.actFile_Open.setText(_translate("MainWindow", "打开"))
        self.actFile_Save.setText(_translate("MainWindow", "保存"))
        self.actClose.setText(_translate("MainWindow", "关闭"))
        self.actEdit_Cut.setText(_translate("MainWindow", "剪切"))
        self.actEdit_Copy.setText(_translate("MainWindow", "复制"))
        self.actEdit_Paste.setText(_translate("MainWindow", "粘贴"))
        self.actEdit_Undo.setText(_translate("MainWindow", "撤销"))
        self.actEdit_Redo.setText(_translate("MainWindow", "重做"))
        self.actEdit_SelectAll.setText(_translate("MainWindow", "全选"))
        self.actEdit_Clear.setText(_translate("MainWindow", "清空"))
        self.actFont_Bold.setText(_translate("MainWindow", "粗体"))
        self.actFont_Italic.setText(_translate("MainWindow", "斜体"))
        self.actFont_UnderLine.setText(_translate("MainWindow", "下划线"))
        self.actSys_ToggleText.setText(_translate("MainWindow", "显示按钮文字"))
        self.actLang_CN.setText(_translate("MainWindow", "汉语"))
        self.actLang_EN.setText(_translate("MainWindow", "英语"))
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
