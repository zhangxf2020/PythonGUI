from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtCore import QTime,QDate,QDateTime
import sys

from ui_Widget import Ui_Widget

class QmyWidget(QWidget):
    def __init__(self):
        super().__init__(parent = None)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        print(dir(self.ui))
        self.ui.calendarWidget.selectionChanged.connect(lambda :print(self.ui.calendarWidget.selectedDate().toString('yyyy-MM-dd')))

    def on_calendarWidget_selectionChanged(self):
        self.ui.editCalender.setText(self.ui.calendarWidget.selectedDate().toString('yyyy年MM月dd日'))

    def on_btnSetTime_clicked(self):
        timestr = self.ui.editTime.text()
        time = QTime.fromString(timestr,'hh:mm:ss') #fromstring 将字符串格式时间转换为Qtime对象
        self.ui.timeEdit.setTime(time)
    def on_btnSetDate_clicked(self):
        date = self.ui.editDate.text()
        qdate = QDate.fromString(date,'yyyy-MM-dd')#fromstring 将字符串格式时间转换为Qdate对象
        self.ui.dateEdit.setDate(qdate)

    def on_btnSetDateTime_clicked(self):
        datetimeStr = self.ui.editDateTime.text()
        datetime = QDateTime.fromString(datetimeStr,'yyyy-MM-dd hh:mm:ss')#fromstring 将字符串格式时间转换为Qdatetime对象
        self.ui.dateTimeEdit.setDateTime(datetime)
    def on_btnGetTime_clicked(self):
        curDateTime = QDateTime.currentDateTime() #获取当前日期时间并返回一个datetime对象

        self.ui.timeEdit.setTime(curDateTime.time())
        print(curDateTime.time())
        self.ui.editTime.setText(curDateTime.time().toString('hh:mm:ss'))#tostring 将Qtime对象转换为字符串格式

        self.ui.dateEdit.setDate(curDateTime.date())
        self.ui.editDate.setText(curDateTime.date().toString('yyyy-MM-dd'))#tostring 将Qdate对象转换为字符串格式

        self.ui.dateTimeEdit.setDateTime(curDateTime)
        self.ui.editDateTime.setText(curDateTime.toString('yyyy-MM-dd hh:mm:ss'))#tostring 将Qdatetime对象转换为字符串格式


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())