from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QDockWidget, QMenu, QTreeWidgetItem, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot, Qt, QDir, QFileInfo
from enum import Enum
import sys
from ui_MainWidget import Ui_MainWindow


class TreeItemType(Enum):
    itTopItem = 1001
    itGroupItem = 1002
    itImageItem = 1003


class TreeColNum(Enum):
    colItem = 0
    colItemType = 1


class QmyMainWidget(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setCentralWidget(self.ui.scrollArea)

        self.ui.dockWidget.setFeatures(QDockWidget.AllDockWidgetFeatures)  # 设置停靠窗口上的小按钮显示(关闭/折叠等)
        self.ui.dockWidget.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)  # 设置停靠窗口的停靠位置,这里是左右

        self.curPixmap = QPixmap()
        self.pixRation = 1
        # 自动滚动区域控件Qscrollarea,其中包含一个Qwidget控件
        self.ui.scrollArea.setWidgetResizable(True)  # 设置自动滚动区控件的尺寸为自适应
        self.ui.scrollArea.setAlignment(Qt.AlignCenter)  # 设置自动滚动区域对其方式,居中
        self.ui.LabPicture.setAlignment(Qt.AlignCenter)  # 设置图片标签控件对其方式,居中

        self.itemFlags = Qt.ItemIsSelectable | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled | Qt.ItemIsAutoTristate
        self.__initTree()

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~自定义函数~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # 初始化目录树,并添加顶层节点
    def __initTree(self):
        self.ui.treeFiles.clear()  # 清空树状窗口中所有数据
        icon = QIcon(r':icons/icons/15.ico')

        item = QTreeWidgetItem(TreeItemType.itTopItem.value)  # 创建一个数劣币爱哦作为顶层节点,需要传递顶层节点的类型,这里使用枚举值(int)
        item.setIcon(TreeColNum.colItem.value, icon)  # 为顶层节点添加图标和文字,第一个参数填入第几列(这里使用枚举值)
        item.setText(TreeColNum.colItem.value, '图片文件')
        item.setFlags(self.itemFlags)  # 设置提前定义好的标志(就是节点是否可选择,可勾选,可编辑,可使用三态
        item.setCheckState(TreeColNum.colItem.value, Qt.Checked)  # 设置节点的初始化选择状态
        item.setData(TreeColNum.colItem.value, Qt.UserRole, '')  # 设置节点的角色数据
        self.ui.treeFiles.addTopLevelItem(item)  # 添加顶层节点,注意和添加下级节点函数不同
    #当点击一个图片节点时调用,处理图片的显示
    def __displayImage(self,item:QTreeWidgetItem):
        fileName = item.data(TreeColNum.colItem.value,Qt.UserRole)
        self.ui.statusbar.showMessage(fileName)
        self.curPixmap.load(fileName)
        self.on_act_SuitableHeight_triggered()
        self.ui.act_SuitableHeight.setEnabled(True)
        self.ui.act_FitWidth.setEnabled(True)
        self.ui.act_Amplification.setEnabled(True)
        self.ui.act_Zoomout.setEnabled(True)
        self.ui.act_ActualSize.setEnabled(True)
    #使用递归,来遍历节点
    def __changeItemCaption(self,item):
        title = '*'+item.text(TreeColNum.colItem.value)
        item.setText(TreeColNum.colItem.value,title)
        if item.childCount() >0:
            for i in range(item.childCount()):
                self.__changeItemCaption(item.child(i))

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~自动生成的函数~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # 添加子节点
    @pyqtSlot()
    def on_act_AddDirectory_triggered(self):
        dirStr = QFileDialog.getExistingDirectory()  # 返回打开文件夹所在的路径
        if (dirStr == ''):
            return
        parItem = self.ui.treeFiles.currentItem()  # 返回被选择的节点
        if parItem == None:
            parItem = self.ui.treeFiles.topLevelItem(0)  # 如果没有选择任何节点,就把第一个节点当做被选择的节点
        icon = QIcon(r':icons/icons/open3.bmp')
        dirObj = QDir(dirStr)  # 这两段代码是获得被选择文件夹的文件夹名称
        nodeText = dirObj.dirName()

        item = QTreeWidgetItem(TreeItemType.itGroupItem.value)
        item.setIcon(TreeColNum.colItem.value, icon)
        item.setText(TreeColNum.colItem.value, nodeText)  # 第一列的节点名称
        item.setText(TreeColNum.colItemType.value, 'group')  # 第二列的节点名称
        item.setFlags(self.itemFlags)
        item.setCheckState(TreeColNum.colItem.value, Qt.Checked)
        item.setData(TreeColNum.colItem.value, Qt.UserRole, dirStr)
        parItem.addChild(item)  # 添加子节点使用addchild
        parItem.setExpanded(True)  # 展开子节点

    # 添加图片节点
    @pyqtSlot()
    def on_act_AddFiles_triggered(self):
        fileList, flt = QFileDialog.getOpenFileNames(self, '选择一个或多个文件', '', 'Images(*.jpg)')#打开文件选择对话框,返回文件目录字符串列表和筛选类型
        if len(fileList) < 1: #如歌没有选中任何文件则return
            return
        item = self.ui.treeFiles.currentItem()#当前选择节点
        if item == None:#如果没有选择节点,就把顶级节点当做选择节点
            item = self.ui.treeFiles.topLevelItem(0)
        if item.type() == TreeItemType.itImageItem.value:#判断当前选择的节点类型,如果是最终节点,就把父节点当做添加节点(因为要添加的节点在其之下,最终节点不可以再添加最终节点
            parItem = item.parent()
        else:
            parItem = item
        icon = QIcon(r':icons/icons/31.ico')
        for i in range(len(fileList)):
            fullFileName = fileList[i]
            fileinfo = QFileInfo(fullFileName)
            noteText = fileinfo.fileName()

            item = QTreeWidgetItem(TreeItemType.itImageItem.value)
            item.setIcon(TreeColNum.colItem.value, icon)
            item.setText(TreeColNum.colItem.value, noteText)
            item.setText(TreeColNum.colItemType.value, 'image')
            item.setFlags(self.itemFlags)
            item.setCheckState(TreeColNum.colItem.value, Qt.Checked)
            item.setData(TreeColNum.colItem.value, Qt.UserRole, fullFileName)
            parItem.addChild(item)
        parItem.setExpanded(True)
    #当treeWidget 节点发生变化之后会触发信号
    def on_treeFiles_currentItemChanged(self,current:QTreeWidgetItem,previous:QTreeWidgetItem):
        if current == None:
            return
        nodeType = current.type()
        if nodeType == TreeItemType.itTopItem.value:
            self.ui.act_AddFiles.setEnabled(True)
            self.ui.act_AddDirectory.setEnabled(True)
            self.ui.act_DelNode.setEnabled(False)
            return
        if nodeType == TreeItemType.itGroupItem.value:
            self.ui.act_AddFiles.setEnabled(True)
            self.ui.act_AddDirectory.setEnabled(True)
            self.ui.act_DelNode.setEnabled(True)
            return
        if nodeType == TreeItemType.itImageItem.value:
            self.ui.act_AddFiles.setEnabled(True)
            self.ui.act_AddDirectory.setEnabled(False)
            self.ui.act_DelNode.setEnabled(True)
            self.__displayImage(current)

    #点击适合高度后触发,控制图片的显示方式,按照高度满足显示(也是点击图片节点后默认触发方式)
    @pyqtSlot()
    def on_act_SuitableHeight_triggered(self):
        H = self.ui.scrollArea.height()#获得scrollarea高度
        realH = self.curPixmap.height()#获得图片真实高度
        self.pixRation = float(H) / realH#图片比例
        pix =self.curPixmap.scaledToHeight(H-30)#获得一个按照scrollarea高度为基准的图片缩放副本
        self.ui.LabPicture.setPixmap(pix)#设置图片
    #点击适应宽度后触发
    @pyqtSlot()
    def on_act_FitWidth_triggered(self):
        W = self.ui.scrollArea.width()-20
        realW = self.curPixmap.width()
        self.pixRation = float(W) / realW
        pix = self.curPixmap.scaledToWidth(W-30)
        self.ui.LabPicture.setPixmap(pix)
    #点击放大显示后触发
    @pyqtSlot()
    def on_act_Amplification_triggered(self):
        #取当前缩放比率,放大是*倍数,然后重新计算长度和宽度
        self.pixRation = self.pixRation * 1.2
        W = self.pixRation * self.curPixmap.width()
        H = self.pixRation * self.curPixmap.height()
        pix = self.curPixmap.scaled(W,H)
        self.ui.LabPicture.setPixmap(pix)

     # 点击缩小显示后触发
    @pyqtSlot()
    def on_act_Zoomout_triggered(self):
        # 取当前缩放比率,放大是*倍数,然后重新计算长度和宽度
        self.pixRation = self.pixRation *0.8
        W = self.pixRation * self.curPixmap.width()
        H = self.pixRation * self.curPixmap.height()
        pix = self.curPixmap.scaled(W, H)
        self.ui.LabPicture.setPixmap(pix)
    #点击实际大小触发
    @pyqtSlot()
    def on_act_ActualSize_triggered(self):
        self.pixRation =1
        self.ui.LabPicture.setPixmap(self.curPixmap)
    #设置窗体浮动性
    @pyqtSlot(bool)
    def on_act_FormFloating_triggered(self,checked):
        self.ui.dockWidget.setFloating(checked)
    #设置窗体可见性
    @pyqtSlot(bool)
    def on_act_FormVisible_triggered(self,checked):
        self.ui.dockWidget.setVisible(checked)
    #设置窗体浮动性改变状态
    @pyqtSlot(bool)
    def on_dockWidget_topLevelChanged(self,topLevel):
        self.ui.act_FormFloating.setChecked(topLevel)
    # 设置窗体可见性改变状态
    @pyqtSlot(bool)
    def on_dockWidget_visibilityChanged(self, visible):
        self.ui.act_FormVisible.setChecked(visible)


    @pyqtSlot()
    #点击删除节点行为后,删除当前选择的节点
    def on_act_DelNode_triggered(self):
        item = self.ui.treeFiles.currentItem()
        parItem = item.parent()#返回当前选择节点的父节点
        parItem.removeChild(item)#从父节点中移除子节点
    #点击遍历节点行为后,遍历当前拥有的节点
    @pyqtSlot()
    def on_act_IterationgNodes_triggered(self):
        count = self.ui.treeFiles.topLevelItemCount()#返回顶层节点的个数
        for i in range(count):
            item = self.ui.treeFiles.topLevelItem(i)#返回顶层节点的treewidgetitem对象
            self.__changeItemCaption(item)







if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QmyMainWidget()
    form.show()
    sys.exit(app.exec_())
