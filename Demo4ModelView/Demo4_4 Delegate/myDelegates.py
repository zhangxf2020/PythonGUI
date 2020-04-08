#coding:utf-8
from PyQt5.QtWidgets import QStyledItemDelegate, QDoubleSpinBox, QComboBox
from PyQt5.QtCore import Qt



class QmyFloatSpinDelegate(QStyledItemDelegate):
    def __init__(self, minV=0, maxV=1000, digi=2, parent=None):
        super(QmyFloatSpinDelegate, self).__init__(parent)
        self.__min = minV
        self.__max = maxV
        self.__decimals = digi

##=============================基于QdoubleSpinBox的代理组件=============================
    def createEditor(self, parent, option, index):#创建组件
        editor = QDoubleSpinBox(parent)
        editor.setFrame(False)
        editor.setRange(self.__min, self.__max)
        editor.setDecimals(self.__decimals) #设置小数位数
        return editor

    def setEditorData(self, editor, index):#设置组件与模型相关联,index:QModelIndex
        model = index.model()  # 关联的数据模型
        text = model.data(index, Qt.EditRole)  # 取出单元格文字
        ##      value = float(index.model().data(index, Qt.EditRole))
        editor.setValue(float(text)) #将取出的单元格文字显示在组件上

    def setModelData(self, editor, model, index):#将组件上的文字保存在单元格上
        value = editor.value()#取出组件内容
        model.setData(index, value, Qt.EditRole)#设置模型文字(对应的索引,设置的值,类型)

    def updateEditorGeometry(self, editor, option, index):#设置组件大小,适应单元格
        editor.setGeometry(option.rect)
##=============================基于QComboBox的代理组件=============================
class QmyComoBoxDelegate(QStyledItemDelegate):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.__itemList = []
        self.__isEditable = False

    def setItems(self,itemList, isEditable = False):
        self.__itemList = itemList
        self.__isEditable = isEditable

    def createEditor(self, parent, option, index):
        editor = QComboBox(parent)
        editor.setFrame(False)
        editor.setEditable(self.__isEditable)
        editor.addItems(self.__itemList)
        return editor
    def setEditorData(self, editor, index):
        model = index.model()
        text = model.data(index,Qt.EditRole)
        editor.setCurrentText(text)
    def setModelData(self, editor, model, index) :
        text = editor.currentText()
        model.setData(index,text,Qt.EditRole)
    def updateEditorGeometry(self, editor, option, index) :
        editor.setGeometry(option.rect)




