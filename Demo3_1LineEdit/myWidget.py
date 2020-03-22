from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtCore import pyqtSlot
import sys

from ui_Widget import Ui_Widget

class QmyWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

    def on_btnCalculate_clicked(self):
        count = int(self.ui.editCount.text())
        price = float(self.ui.editPrice.text())
        total = count * price
        self.ui.editTotal.setText('{:.2f}'.format(total))

    @pyqtSlot(int)
    def on_spinCount_valueChanged(self,count):
        price = self.ui.spinPrice.value()
        total = count * price
        self.ui.spinTotal.setValue(total)
    @pyqtSlot(float)
    def on_spinPrice_valueChanged(self,price):
        count = self.ui.spinCount.value()
        total = count * price
        self.ui.spinTotal.setValue(total)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())
