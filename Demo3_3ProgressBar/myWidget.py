from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtCore import pyqtSlot
import sys
from ui_Widget import Ui_Widget

class QmyWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        print(dir(self.ui))
        self.ui.slider.valueChanged.connect(self.valueChange)
        self.ui.scrollBar.valueChanged.connect(self.valueChange)

    def valueChange(self,value):
        self.ui.progressBar.setValue(value)
    def on_scrollBar_valueChanged(self,value):
        self.ui.progressBar.setValue(value)
    def on_chkBox_Visible_toggled(self,checked):
        self.ui.progressBar.setTextVisible(checked)
    def on_chkBox_Inverted_toggled(self,checked):
        self.ui.progressBar.setInvertedAppearance(checked)
    def on_radio_Percent_toggled(self):
        self.ui.progressBar.setFormat('%p%')#进度条文字显示格式,%p%代表百分比,%v代表数值
    def on_radio_Value_toggled(self):
        self.ui.progressBar.setFormat('%v')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())