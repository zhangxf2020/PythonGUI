from PyQt5.QtCore import Qt,pyqtSignal,QObject,pyqtSlot

class human(QObject):
    nameChanged = pyqtSignal(str)

    ageChanged = pyqtSignal([int],[str])

    def __init__(self,name ='MIKE',age =10,parent = None):
        super().__init__(parent)
        self.setAge(age)
        self.setName(name)
    def setName(self,name):
        self.__name = name
        self.nameChanged.emit(self.__name)
    def setAge(self,age):
        self.__age = age
        self.ageChanged.emit(self.__age)
        if self.__age <= 18:
            angInfo = '你是 少年'
        elif self.__age <=35:
            angInfo = '你是 年轻人'
        elif self.__age <= 55:
            angInfo = '你是 中年人'
        elif self.__age <=80:
            angInfo = '你是 老年人'
        else:
            angInfo ='您是 寿星啊'
        self.ageChanged[str].emit(angInfo)

class Responsor(QObject):#响应期
    def __init__(self):
        super().__init__()

    def do_ageChanged_int(self,age):
        print('您的年龄是：',str(age))
    @pyqtSlot(str)
    def do_ageChanged_str(self,anginfo):
        print(anginfo)
    def do_nameChanged_str(self,name):
        print('Hello,{}'.format(name))

if __name__ == '__main__':
    '''其它类发射的信号可以关联别的类中槽函数'''
    boy = human('JOCK',20)

    resp = Responsor()
    boy.ageChanged.connect(resp.do_ageChanged_int)
    boy.ageChanged[str].connect(resp.do_ageChanged_str)
    boy.nameChanged.connect(resp.do_nameChanged_str)

    boy.setName('MMMM')
    boy.setAge(80)

    boy.ageChanged[str].disconnect(resp.do_ageChanged_str)#断开信号与槽的链接
    boy.setName('JJJJ')
    boy.setAge(60)