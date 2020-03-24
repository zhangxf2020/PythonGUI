from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys

from ui_Widget import Ui_Widget

class QmyWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        print(dir(self.ui))

    def on_btnIniItems_clicked(self):
        icon = QIcon(':/icons/images/aim.ico')
        self.ui.comboBox.clear()
        provinces = ['山东','河北','河南','湖北','湖南','广东']
        #单个添加数据可以添加图标
        for i in provinces:
            self.ui.comboBox.addItem(icon,i)
        #统一添加数据不可以添加图标
        self.ui.comboBox.addItems(provinces)

    def on_btnClearItems_clicked(self):
        self.ui.comboBox.clear()
    @pyqtSlot(bool)
    def on_checkBox_toggled(self,checked):
        #设置下拉框是否可像lineEdit一样可编辑文本
        self.ui.comboBox.setEditable(checked)

    @pyqtSlot(str)
    def on_comboBox_currentIndexChanged(self,curText):
        self.ui.lineEdit.setText(curText)

    def on_btnIni2_clicked(self):
        icon = QIcon(':/icons/images/unit.ico')
        self.ui.comboBox_2.clear()
        provinces ={'北京':10,'上海':21,'天津':22,'徐州':516,'福州':591,'青岛':532}
        for i in provinces:
            self.ui.comboBox_2.addItem(icon,i,provinces[i]) #添加数据时,可以附带第三个参数,为用户的关联数据
    def on_comboBox_2_currentIndexChanged(self,curText):
        zone = self.ui.comboBox_2.currentData()#获取当前选择项的关联数据
        if zone != None:
            self.ui.lineEdit.setText('{} 区号:{}'.format(curText,zone))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())