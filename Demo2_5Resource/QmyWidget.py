from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys

from human import human
from ui_Widget import Ui_Widget

class QmyWidget(QWidget):
    def __init__(self,parent=None):
        super(QmyWidget, self).__init__(parent)
        self.setWindowIcon(QIcon(":/icons/images/app.ico"))
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.boy = human('Boy',16)
        self.boy.nameChanged.connect(self.do_nameChanged)
        self.boy.ageChanged.connect(self.do_ageChanged_int)
        self.boy.ageChanged[str].connect(self.do_ageChanged_str)


    def on_sliderSetAge_valueChanged(self,value):
        self.boy.setAge(value)

    def on_btnSetName_clicked(self):
        self.boy.setName(self.ui.editNameInput.text())



    def do_nameChanged(self,name):
        self.ui.editNameHello.setText('Hello '+name)
    def do_ageChanged_int(self,age):
        self.ui.editAgeInt.setText(str(age))
    @pyqtSlot(str)
    def do_ageChanged_str(self,info):
        self.ui.editAgeStr.setText(info)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())

