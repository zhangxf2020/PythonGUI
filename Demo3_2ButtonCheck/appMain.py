from PyQt5.QtWidgets import QWidget,QApplication
from myWidget import QmyWidget
import sys

app = QApplication(sys.argv)
win= QmyWidget()
win.show()
sys.exit(app.exec_())
