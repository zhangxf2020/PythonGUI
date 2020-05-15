from PyQt5.Qt import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.UI_test()


    def UI_test(self):
        cb = QComboBox(self)
        model = QStandardItemModel()        #������׼������ͼģ��
        item1 = QStandardItem('item1')
        item2 = QStandardItem('item2')
        item2_1 = QStandardItem('item2_1')
        item2.appendRow(item2_1)        #��item2_1��Ϊitem2�����б�
        model.appendRow(item1)
        model.appendRow(item2)
        cb.setModel(model)
        cb.setView(QTreeView(cb))  #��ͼ����
        pass
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())