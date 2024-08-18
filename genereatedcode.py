from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
import sys

class Window(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		layout = QGridLayout()
		self.setLayout(layout)

# generating radiobuttons

		#radiobutton1
		radiobutton1 =QRadioButton()
		radiobutton1.setText("test1")
		radiobutton1.setIcon(QIcon("static/img.svg"))
		radiobutton1.setChecked(True)
		layout.addWidget(radiobutton1,0,1)

		#radiobutton2
		radiobutton2 =QRadioButton()
		radiobutton2.setText("test2")
		radiobutton2.setIcon(QIcon("static/img.svg"))
		radiobutton2.setIconSize(QSize(50,50))
		radiobutton2.setDown(False)
		layout.addWidget(radiobutton2,0,2)

		#radiobutton3
		radiobutton3 =QRadioButton()
		radiobutton3.setText("test3")
		radiobutton3.setIcon(QIcon("static/img.svg"))
		radiobutton3.setIconSize(QSize(30,30))
		radiobutton3.toggled.connect(self.temp)
		radiobutton3.setStyleSheet("QRadioButton"
"{"
"border : 2px solid black;"
"}"
)
		layout.addWidget(radiobutton3,0,3)

		#radiobutton4
		radiobutton4 =QRadioButton()
		radiobutton4.setText("test4")
		radiobutton4.toggled.connect(self.Test)
		radiobutton4.setStyleSheet("QRadioButton"
"{"
"background-color : lightgreen;font-size:40px;"
"}"
)
		radiobutton4.setChecked(True)
		layout.addWidget(radiobutton4,0,4)

	def temp(self):
		radioButton = self.sender()
		# to be completed
	def Test(self):
		radioButton = self.sender()
		# to be completed

# end of generating
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())