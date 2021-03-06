# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Widget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(771, 336)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(Widget)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.btnSetDate = QtWidgets.QPushButton(self.groupBox)
        self.btnSetDate.setObjectName("btnSetDate")
        self.gridLayout.addWidget(self.btnSetDate, 4, 2, 1, 1)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.groupBox)
        self.dateTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 10, 9), QtCore.QTime(14, 25, 0)))
        self.dateTimeEdit.setCalendarPopup(False)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout.addWidget(self.dateTimeEdit, 5, 1, 1, 1)
        self.editDate = QtWidgets.QLineEdit(self.groupBox)
        self.editDate.setObjectName("editDate")
        self.gridLayout.addWidget(self.editDate, 3, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.btnSetDateTime = QtWidgets.QPushButton(self.groupBox)
        self.btnSetDateTime.setObjectName("btnSetDateTime")
        self.gridLayout.addWidget(self.btnSetDateTime, 6, 2, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QtCore.QDate(2020, 3, 24))
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.editDateTime = QtWidgets.QLineEdit(self.groupBox)
        self.editDateTime.setObjectName("editDateTime")
        self.gridLayout.addWidget(self.editDateTime, 5, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.editTime = QtWidgets.QLineEdit(self.groupBox)
        self.editTime.setObjectName("editTime")
        self.gridLayout.addWidget(self.editTime, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        self.btnSetTime = QtWidgets.QPushButton(self.groupBox)
        self.btnSetTime.setObjectName("btnSetTime")
        self.gridLayout.addWidget(self.btnSetTime, 2, 2, 1, 1)
        self.timeEdit = QtWidgets.QTimeEdit(self.groupBox)
        self.timeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(15, 30, 55)))
        self.timeEdit.setCalendarPopup(True)
        self.timeEdit.setObjectName("timeEdit")
        self.gridLayout.addWidget(self.timeEdit, 1, 1, 1, 1)
        self.btnGetTime = QtWidgets.QPushButton(self.groupBox)
        self.btnGetTime.setObjectName("btnGetTime")
        self.gridLayout.addWidget(self.btnGetTime, 0, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 5)
        self.gridLayout.setColumnStretch(2, 4)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Widget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.editCalender = QtWidgets.QLineEdit(self.groupBox_2)
        self.editCalender.setReadOnly(True)
        self.editCalender.setObjectName("editCalender")
        self.gridLayout_2.addWidget(self.editCalender, 0, 1, 1, 1)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.groupBox_2)
        self.calendarWidget.setTabletTracking(False)
        self.calendarWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.calendarWidget.setFirstDayOfWeek(QtCore.Qt.Monday)
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setSelectionMode(QtWidgets.QCalendarWidget.SingleSelection)
        self.calendarWidget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.ISOWeekNumbers)
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout_2.addWidget(self.calendarWidget, 1, 0, 1, 2)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 4)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Demo3_4日期时间"))
        self.groupBox.setTitle(_translate("Widget", "日期时间"))
        self.btnSetDate.setText(_translate("Widget", "设置日期"))
        self.dateTimeEdit.setDisplayFormat(_translate("Widget", "yyyy-MM-dd HH:mm:ss"))
        self.editDate.setInputMask(_translate("Widget", "9999-99-99"))
        self.label_3.setText(_translate("Widget", "日  期"))
        self.btnSetDateTime.setText(_translate("Widget", "设置日期时间"))
        self.dateEdit.setDisplayFormat(_translate("Widget", "yyyy年MM月dd日"))
        self.label_4.setText(_translate("Widget", "日期时间"))
        self.editDateTime.setInputMask(_translate("Widget", "9999-99-99 99:99:99"))
        self.label_2.setText(_translate("Widget", "时  间"))
        self.editTime.setInputMask(_translate("Widget", "99:99:99;_"))
        self.label.setText(_translate("Widget", "字符串显示"))
        self.btnSetTime.setText(_translate("Widget", "设置时间"))
        self.timeEdit.setDisplayFormat(_translate("Widget", "HH:mm:ss"))
        self.btnGetTime.setText(_translate("Widget", "读取当前日期时间"))
        self.groupBox_2.setTitle(_translate("Widget", "日历选择"))
        self.label_5.setText(_translate("Widget", "选择的日期:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())

