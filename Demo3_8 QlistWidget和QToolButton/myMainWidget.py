from PyQt5.QtWidgets import QMainWindow,QApplication,QMenu,QToolButton,QListWidgetItem,QAction
from PyQt5.QtCore import Qt,pyqtSlot
from PyQt5.QtGui import QIcon,QCursor

import sys
from ui_MainWidget import Ui_MainWindow

class QmyMainWidget(QMainWindow):
    '''行为动作,QAction必须显示的使用@pyqtSlot(),否则会执行两遍'''
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setCentralWidget(self.ui.splitter)

        self.__setActionsForButton()
        self.__createSelectionPopMenu()
        self.__FlagEditable = (Qt.ItemIsSelectable | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled | Qt.ItemIsEditable)
        self.__FlagNotEditable = (Qt.ItemIsSelectable | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)

    def __setActionsForButton(self):
        self.ui.btnList_Ini.setDefaultAction(self.ui.act_InitializationList)
        self.ui.btnList_Clear.setDefaultAction(self.ui.act_ClearList)
        self.ui.btnList_Insert.setDefaultAction(self.ui.act_Insert)
        self.ui.btnList_Append.setDefaultAction(self.ui.act_AddItem)
        self.ui.btnList_Delete.setDefaultAction(self.ui.act_DelCurrentItem)

        self.ui.btnSel_ALL.setDefaultAction(self.ui.act_AllSelect)
        self.ui.btnSel_None.setDefaultAction(self.ui.act_AllUnselect)
        self.ui.btnSel_Invs.setDefaultAction(self.ui.act_ReverseElection)

    def __createSelectionPopMenu(self):
        menuSelection = QMenu(self)
        menuSelection.addActions([self.ui.act_AllSelect,self.ui.act_AllUnselect,self.ui.act_ReverseElection])

        self.ui.btnSelectItem.setPopupMode(QToolButton.MenuButtonPopup)#添加工具按钮下拉箭头样式(在右侧)
        self.ui.btnSelectItem.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.ui.btnSelectItem.setDefaultAction(self.ui.act_Itemselection)#关联行为后,按钮文字都会与行为显示一致
        self.ui.btnSelectItem.setMenu(menuSelection)

        toolBtn = QToolButton(self)
        toolBtn.setPopupMode(QToolButton.InstantPopup) #添加工具按钮下拉箭头样式(在下方)
        toolBtn.setDefaultAction(self.ui.act_Itemselection)
        toolBtn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolBtn.setMenu(menuSelection)
        self.ui.mainToolBar.addWidget(toolBtn)

        self.ui.mainToolBar.addSeparator()
        self.ui.mainToolBar.addAction(self.ui.act_Exit)

    #listwidget设置初始化项
    @pyqtSlot()
    def on_act_InitializationList_triggered(self):
        icon = QIcon(r':/icons/images/724.bmp')
        editable = self.ui.chkBoxList_Editable.isChecked()
        if editable:
            Flag = self.__FlagEditable
        else:
            Flag = self.__FlagNotEditable
        self.ui.listWidget.clear()
        for i in range(10):
            itemStr = 'Item {}'.format(i)
            aItem = QListWidgetItem()
            aItem.setText(itemStr)
            aItem.setIcon(icon)
            aItem.setCheckState(Qt.Checked)
            aItem.setFlags(Flag)
            self.ui.listWidget.addItem(aItem)
    #listwidget设置清除项
    @pyqtSlot()
    def on_act_ClearList_triggered(self):
        self.ui.listWidget.clear()


    #listwidget 设置插入项
    @pyqtSlot()
    def on_act_Insert_triggered(self):
        icon = QIcon(":/icons/images/728.bmp")
        editable = self.ui.chkBoxList_Editable.isChecked()

        if (editable == True):
            Flag = self.__FlagEditable  # 可编辑
        else:
            Flag = self.__FlagNotEditable  # 不可编辑

        aItem = QListWidgetItem()
        aItem.setText("Inserted Item")
        aItem.setIcon(icon)
        aItem.setCheckState(Qt.Checked)
        aItem.setFlags(Flag)  # 项的flags
        curRow = self.ui.listWidget.currentRow()  # 当前行
        self.ui.listWidget.insertItem(curRow, aItem)

    # listwidget 设置添加项
    @pyqtSlot()
    def on_act_AddItem_triggered(self):
        icon = QIcon(":/icons/images/718.bmp")
        editable = self.ui.chkBoxList_Editable.isChecked()
        if (editable == True):
            Flag = self.__FlagEditable  # 可编辑
        else:
            Flag = self.__FlagNotEditable  # 不可编辑
        aItem = QListWidgetItem()
        aItem.setText("Add Item")
        aItem.setIcon(icon)
        aItem.setCheckState(Qt.Checked)
        aItem.setFlags(Flag)  # 项的flags
        self.ui.listWidget.addItem(aItem)

    # listwidget 设置清除当前项
    @pyqtSlot()
    def on_act_DelCurrentItem_triggered(self):
        curRow = self.ui.listWidget.currentRow()  # 当前行
        self.ui.listWidget.takeItem(curRow)#删除当前行,这里参数为行号

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~我是分割线~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    '''全选/全不选/反选行为指令'''
    @pyqtSlot()
    def on_act_AllSelect_triggered(self):
        for i in range(self.ui.listWidget.count()):
            aItem = self.ui.listWidget.item(i)
            aItem.setCheckState(Qt.Checked)

    @pyqtSlot()
    def on_act_AllUnselect_triggered(self):
        for i in range(self.ui.listWidget.count()):
            aItem = self.ui.listWidget.item(i)
            aItem.setCheckState(Qt.Unchecked)

    @pyqtSlot()
    def on_act_ReverseElection_triggered(self):
        for i in range(self.ui.listWidget.count()):
            aItem = self.ui.listWidget.item(i)
            if aItem.checkState() == Qt.Unchecked:
                aItem.setCheckState(Qt.Checked)
            else:
                aItem.setCheckState(Qt.Unchecked)

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~我是分割线~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    '''为QlistWidget进行判断当前项和前一项'''
    def on_listWidget_currentItemChanged(self,current,previous):
        #注意,这里的前一项是指上一回点击的那个item,不是列表里顺序排列的前一项
        if current != None:
            if previous ==None:
                self.ui.editCurItemText.setText('当前项名称:{}; 没有前一项'.format(current.text()))
            else:
                self.ui.editCurItemText.setText('当前项名称:{}; 前一项名称:{}'.format(current.text(),previous.text()))

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~我是分割线~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    '''为QlistWidget添加右键快捷菜单'''
    def on_listWidget_customContextMenuRequested(self, pos):  ##右键快捷菜单
        #这里有个坑,一定要使用代码或QT设计师,将该窗口的鼠标右键菜单打开
        self.ui.listWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        menuList = QMenu(self)  # 创建菜单

        menuList.addAction(self.ui.act_InitializationList)
        menuList.addAction(self.ui.act_ClearList)

        menuList.addAction(self.ui.act_Insert)
        menuList.addAction(self.ui.act_AddItem)
        menuList.addAction(self.ui.act_DelCurrentItem)
        menuList.addSeparator()

        menuList.addAction(self.ui.act_AllSelect)
        menuList.addAction(self.ui.act_AllUnselect)
        menuList.addAction(self.ui.act_ReverseElection)

        menuList.exec(QCursor.pos())  # 显示菜单
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~我是分割线~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    '''处理多选框事件'''
    @pyqtSlot(bool)
    def on_chkBoxList_Editable_toggled(self,checked):
        for i in range(self.ui.listWidget.count()):
            aItem = self.ui.listWidget.item(i)
            if checked:
                aItem.setFlags(self.__FlagEditable)
            else:
                aItem.setFlags(self.__FlagNotEditable)






if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QmyMainWidget()
    form.show()
    sys.exit(app.exec_())