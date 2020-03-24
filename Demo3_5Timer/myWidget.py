from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtCore import QTimer,QTime
import sys

from ui_Widget import Ui_Widget

class QmyWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        print(dir(self.ui))
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.start()
        self.timer.timeout.connect(self.do_timer_timeout)
        self.counttime = QTime() #创建当前时间对象

    def do_timer_timeout(self):
        self.datetime = QTime.currentTime()
        self.ui.LCDHour.display(self.datetime.hour())
        self.ui.LCDMin.display(self.datetime.minute())
        self.ui.LCDSec.display(self.datetime.second())

    def on_btnSetIntv_clicked(self):
        self.timer.setInterval(self.ui.spinBoxIntv.value())


    def on_btnStart_clicked(self):
        self.timestart = QTime.currentTime()
        self.ui.btnStart.setEnabled(False)
        self.ui.btnStop.setEnabled(True)
        self.ui.btnSetIntv.setEnabled(False)
        self.counttime.start() #点击开始后，时间对象开始计时
        self.ui.LabElapsedTime.setText('流逝的时间')

    def on_btnStop_clicked(self):
        self.timeend = QTime.currentTime()
        self.ui.btnStart.setEnabled(True)
        self.ui.btnStop.setEnabled(False)
        self.ui.btnSetIntv.setEnabled(True)
        tmMs = self.counttime.elapsed() #点击结束按钮后，此方法可返回计时的时间，返回毫秒

        Ms = tmMs % 1000
        sec = tmMs // 1000
        self.ui.LabElapsedTime.setText('流逝的时间:  {}秒 , {}毫秒'.format(sec,Ms))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())