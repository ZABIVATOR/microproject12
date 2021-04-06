import warnings
import sys
warnings.filterwarnings("ignore")
import gmsh
import warnings
warnings.filterwarnings("ignore")
from datetime import date
from PyQt5 import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox, QHBoxLayout, QLabel, QLineEdit,QPushButton,QGridLayout,QInputDialog, QDoubleSpinBox
from PyQt5.QtGui import QIcon, QPixmap
figura = 0 
poradok= 0

class bd(QWidget):#oshibka

	def __init__(self):
		super().__init__()

		self.initUI()

		
		#primer
			#self.g=bd()
			#self.g.show()
		
		
	def initUI(self):

		hbox = QHBoxLayout(self)
		pixmap = QPixmap("bsod_2.jpg")
		self.setGeometry(-13, -40, 1920, 1080)
		lbl = QLabel(self)
		lbl.setPixmap(pixmap)
		hbox.addWidget(lbl)
		self.setLayout(hbox)

class gmh():#mesh
	def __init__(self):
		self.dt = date.today()

	def in1(self,a):
		gmsh.initialize()
		global poradok
		poradok+=1
		gmsh.model.add("krug" + str(self.dt)+'('+str(poradok)+')')
		lc = 1e-2
		gmsh.model.geo.addPoint(0, 0, 0, lc, 1)
		gmsh.model.geo.addPoint(a, 0, 0, lc, 2)
		gmsh.model.geo.addPoint(-a, 0, 0, lc, 3)
		gmsh.model.geo.addCircleArc(2, 1, 3, 1)
		gmsh.model.geo.addCircleArc(3, 1, 2, 2)
		gmsh.model.geo.addCurveLoop([1, 2], 1)
		gmsh.model.geo.addPlaneSurface([1], 1)
		gmsh.model.geo.synchronize()
		gmsh.model.mesh.generate(2)
		gmsh.write("krug" + str(self.dt) +'('+str(poradok)+')'+".msh") 
		if '-nopopup' not in sys.argv:
			gmsh.fltk.run()
		gmsh.finalize()

	def in2(self,a,b):
		gmsh.initialize()
		global poradok
		poradok+=1
		gmsh.model.add("treougolnic" + str(self.dt)+'('+str(poradok)+')')
		lc = 1e-2
		gmsh.model.geo.addPoint(0, 0, 0, lc, 1)
		gmsh.model.geo.addPoint(a, 0, 0, lc, 2)
		gmsh.model.geo.addPoint(a, b, 0, lc, 3)
		gmsh.model.geo.addLine(1, 2, 1)
		gmsh.model.geo.addLine(2, 3, 2)
		gmsh.model.geo.addLine(3, 1, 3)
		gmsh.model.geo.addCurveLoop([1, 2, 3], 1)
		gmsh.model.geo.addPlaneSurface([1], 1)
		gmsh.model.geo.synchronize()
		gmsh.model.mesh.generate(2)
		gmsh.write("treougolnic" + str(self.dt) +'('+str(poradok)+')'+".msh") 
		if '-nopopup' not in sys.argv:
			gmsh.fltk.run()
		gmsh.finalize()

	def in3(self,a,b):
		gmsh.initialize()
		global poradok
		poradok+=1
		gmsh.model.add("pramougolnic" + str(self.dt)+'('+str(poradok)+')')
		lc = 1e-2
		gmsh.model.geo.addPoint(0, 0, 0, lc, 1)
		gmsh.model.geo.addPoint(a, 0, 0, lc, 2)
		gmsh.model.geo.addPoint(a, b, 0, lc, 3)
		p4 = gmsh.model.geo.addPoint(0, b, 0, lc)
		gmsh.model.geo.addLine(1, 2, 1)
		gmsh.model.geo.addLine(3, 2, 2)
		gmsh.model.geo.addLine(3, p4, 3)
		gmsh.model.geo.addLine(4, 1, p4)
		gmsh.model.geo.addCurveLoop([4, 1, -2, 3], 1)
		gmsh.model.geo.addPlaneSurface([1], 1)
		gmsh.model.geo.synchronize()
		gmsh.model.mesh.generate(2)
		gmsh.write("pramougolnic" + str(self.dt) +'('+str(poradok)+')'+".msh") 
		if '-nopopup' not in sys.argv:
			gmsh.fltk.run()
		gmsh.finalize()

	def in23(self,h,r):
		gmsh.initialize()
		global poradok
		poradok+=1
		gmsh.model.add("cylinder" + str(self.dt)+'('+str(poradok)+')')
		cylinder = gmsh.model.occ.addCylinder(0, 0, 0 ,h, 0, 0, r)
		gmsh.model.occ.addVolume([cylinder])
		gmsh.model.occ.synchronize()
		gmsh.model.mesh.generate()
		gmsh.write("cylinder" + str(self.dt) +'('+str(poradok)+')'+".msh") 
		if '-nopopup' not in sys.argv:
			gmsh.fltk.run()
		gmsh.finalize()

	def in24(self,h,R,r):
		gmsh.initialize()
		global poradok
		poradok+=1
		gmsh.model.add("cone" + str(self.dt)+'('+str(poradok)+')')
		cylinder = gmsh.model.occ.addCone(0, 0, 0 ,h, 0, 0, r,R)	
		gmsh.model.occ.addVolume([cylinder])
		gmsh.model.occ.synchronize()
		gmsh.model.mesh.generate()
		gmsh.write("cone" + str(self.dt) +'('+str(poradok)+')'+".msh") 
		if '-nopopup' not in sys.argv:
			gmsh.fltk.run()
		gmsh.finalize()

	def in26(self,R,r):
		gmsh.initialize()
		print(R, ' ',r)
		global poradok
		poradok+=1
		gmsh.model.add("tor" + str(self.dt)+'('+str(poradok)+')')
		torus = gmsh.model.occ.addTorus(0, 0,0,R, r)
		gmsh.model.occ.addVolume([torus])
		gmsh.model.occ.synchronize()
		gmsh.model.mesh.generate()
		gmsh.write("tor" + str(self.dt) +'('+str(poradok)+')'+".msh") 
		if '-nopopup' not in sys.argv:
			gmsh.fltk.run()
		gmsh.finalize()

	def in28(self,b,c,a):
		gmsh.initialize()
		global poradok
		poradok+=1
		gmsh.model.add("wedge" + str(self.dt)+'('+str(poradok)+')')
		cylinder = gmsh.model.occ.addWedge(0, 0, 0 ,a, b, c)	
		gmsh.model.occ.addVolume([cylinder])
		gmsh.model.occ.synchronize()
		gmsh.model.mesh.generate()
		gmsh.write("wedge" + str(self.dt) +'('+str(poradok)+')'+".msh") 
		if '-nopopup' not in sys.argv:
			gmsh.fltk.run()
		gmsh.finalize()

	def in4(self,n,text):
		gmsh.initialize()
		global poradok
		poradok+=1
		lc = 1e-2
		gmsh.model.add("ownfigure" + str(self.dt) +'('+str(poradok)+')')
		self.p = (list(map(float, text.split())))
		n=int(len(self.p)/2)
		for i in range(n):
			gmsh.model.geo.addPoint(self.p[2*i+0], self.p[2*i+1], 0, lc, i+1)
			print (self.p[2*i+0],' ', self.p[2*i+1])
		for i in range(n-1):
			gmsh.model.geo.addLine(i+1, i+2, i+1)
		gmsh.model.geo.addLine(n, 1, n)
		gmsh.model.geo.addCurveLoop([i+1 for i in range(n)], 1)
		gmsh.model.geo.addPlaneSurface([1], 1)
		gmsh.model.geo.synchronize()
		gmsh.model.mesh.generate()
		if '-nopopup' not in sys.argv:
			gmsh.fltk.run()
		gmsh.write("ownfigure" + str(self.dt) +'('+str(poradok)+')'+".msh") 
		gmsh.finalize()

	def in6(self,a):
		gmsh.initialize()
		global poradok
		poradok+=1
		gmsh.model.add("SPHERE" + str(self.dt) +'('+str(poradok)+')')
		cylinder = gmsh.model.occ.addSphere (0, 0,0,a)
		gmsh.model.occ.addVolume([cylinder])
		gmsh.model.occ.synchronize()
		gmsh.model.mesh.generate()
		gmsh.write("SPHERE" + str(self.dt) +'('+str(poradok)+')'+".msh") 
		if '-nopopup' not in sys.argv:
			gmsh.fltk.run()
		gmsh.finalize()

	def in7(self,a,b,c):
		gmsh.initialize()
		global poradok
		poradok+=1
		gmsh.model.add("paralelepiped"+ str(self.dt)+'('+str(poradok)+')')
		lc = 1e-2
		gmsh.model.geo.addPoint(0, 0, 0, lc, 1)
		
		gmsh.model.geo.addPoint(a, 0, 0, lc, 2)
		gmsh.model.geo.addPoint(a, b, 0, lc, 3)
		gmsh.model.geo.addPoint(0, b, 0, lc, 4)
		gmsh.model.geo.addPoint(0, 0, c, lc, 5)
		gmsh.model.geo.addPoint(a, 0, c, lc, 6)
		gmsh.model.geo.addPoint(a, b, c, lc, 7)
		gmsh.model.geo.addPoint(0, b, c, lc, 8)

		gmsh.model.geo.addLine(1, 2,1)
		gmsh.model.geo.addLine(2, 3,2)
		gmsh.model.geo.addLine(3, 4,3)
		gmsh.model.geo.addLine(4, 1,4)
		gmsh.model.geo.addLine(5, 6,5)
		gmsh.model.geo.addLine(6, 7,6)
		gmsh.model.geo.addLine(7, 8,7)
		gmsh.model.geo.addLine(8, 5,8)
		gmsh.model.geo.addLine(1, 5,9)
		gmsh.model.geo.addLine(2, 6,10)
		gmsh.model.geo.addLine(3, 7,11)
		gmsh.model.geo.addLine(4, 8,12)
		gmsh.model.geo.addCurveLoop([1, 2, 3, 4], 1)
		gmsh.model.geo.addPlaneSurface([1], 1)
		gmsh.model.geo.addCurveLoop([5, 6, 7, 8], 2)
		gmsh.model.geo.addPlaneSurface([2], 2)
		gmsh.model.geo.addCurveLoop([1, 10, -5, -9], 3)
		gmsh.model.geo.addPlaneSurface([3], 3)
		gmsh.model.geo.addCurveLoop([4, 9, -8, -12], 4)
		gmsh.model.geo.addPlaneSurface([4], 4)
		gmsh.model.geo.addCurveLoop([3, 12, -7, -11], 5)
		gmsh.model.geo.addPlaneSurface([5], 5)
		gmsh.model.geo.addCurveLoop([10, 6, -11, -2], 6)
		gmsh.model.geo.addPlaneSurface([6], 6)
		l = gmsh.model.geo.addSurfaceLoop([1,2,3,4,5,6])
		gmsh.model.geo.addVolume([l])
		gmsh.model.geo.synchronize()
		gmsh.model.mesh.generate(3)
		gmsh.write("paralelepiped"+ str(self.dt) +'('+str(poradok)+')'+".msh")
		if '-nopopup' not in sys.argv:
			gmsh.fltk.run()
		gmsh.finalize()

class Ui_Form26(object):
	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.resize(201, 185)
		self.verticalLayoutWidget = QtWidgets.QWidget(Form)
		self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 200, 180))
		self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
		self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
		self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_4.setObjectName("horizontalLayout_4")
		self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label_2.setObjectName("label_2")
		self.horizontalLayout_4.addWidget(self.label_2)
		self.lineEdit_2 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
		self.lineEdit_2.setMaximum(1.7976931348623158e+308)
		self.lineEdit_2.setObjectName("lineEdit_2")
		self.horizontalLayout_4.addWidget(self.lineEdit_2)
		self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label_4.setObjectName("label_4")
		self.horizontalLayout_4.addWidget(self.label_4)
		self.verticalLayout_2.addLayout(self.horizontalLayout_4)
		self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_3.setObjectName("horizontalLayout_3")
		self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label.setObjectName("label")
		self.horizontalLayout_3.addWidget(self.label)
		self.lineEdit = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
		self.lineEdit.setMaximum(1.7976931348623157e+308)
		self.lineEdit.setObjectName("lineEdit")
		self.horizontalLayout_3.addWidget(self.lineEdit)
		self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label_3.setObjectName("label_3")
		self.horizontalLayout_3.addWidget(self.label_3)
		self.verticalLayout_2.addLayout(self.horizontalLayout_3)
		self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
		self.pushButton.setObjectName("pushButton")
		self.verticalLayout_2.addWidget(self.pushButton)

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "Form"))
		self.label_2.setText(_translate("Form", " Радиус"))
		self.label_4.setText(_translate("Form", "[м] "))
		self.label.setText(_translate("Form", " радиус"))
		self.label_3.setText(_translate("Form", "[м] "))
		self.pushButton.setText(_translate("Form", "OK"))

class Window26(QMainWindow, Ui_Form26):#chetyreh ugolnic 2 okna
	def __init__(self):
		super().__init__()
		self.v1=0.0
		self.v2=0.0
		self.setupUi(self)
		self.lineEdit.valueChanged.connect(self.Chan)
		self.lineEdit_2.valueChanged.connect(self.Chan2)
		self.pushButton.clicked.connect(self.iniz)
	def Chan(self):
		self.v1=self.lineEdit.value()
	def Chan2(self):
		self.v2=self.lineEdit_2.value()
	def iniz(self):
		self.g=gmh()
		self.g.in26(self.v2,self.v1)
		self.close()

class Ui_Form23(object):
	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.resize(201, 185)
		self.verticalLayoutWidget = QtWidgets.QWidget(Form)
		self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 200, 180))
		self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
		self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
		self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_4.setObjectName("horizontalLayout_4")
		self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label_2.setObjectName("label_2")
		self.horizontalLayout_4.addWidget(self.label_2)
		self.lineEdit_2 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
		self.lineEdit_2.setMaximum(1.7976931348623158e+308)
		self.lineEdit_2.setObjectName("lineEdit_2")
		self.horizontalLayout_4.addWidget(self.lineEdit_2)
		self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label_4.setObjectName("label_4")
		self.horizontalLayout_4.addWidget(self.label_4)
		self.verticalLayout_2.addLayout(self.horizontalLayout_4)
		self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_3.setObjectName("horizontalLayout_3")
		self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label.setObjectName("label")
		self.horizontalLayout_3.addWidget(self.label)
		self.lineEdit = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
		self.lineEdit.setMaximum(1.7976931348623157e+308)
		self.lineEdit.setObjectName("lineEdit")
		self.horizontalLayout_3.addWidget(self.lineEdit)
		self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label_3.setObjectName("label_3")
		self.horizontalLayout_3.addWidget(self.label_3)
		self.verticalLayout_2.addLayout(self.horizontalLayout_3)
		self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
		self.pushButton.setObjectName("pushButton")
		self.verticalLayout_2.addWidget(self.pushButton)

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "Form"))
		self.label_2.setText(_translate("Form", " Высота"))
		self.label_4.setText(_translate("Form", "[м] "))
		self.label.setText(_translate("Form", " Радиус"))
		self.label_3.setText(_translate("Form", "[м] "))
		self.pushButton.setText(_translate("Form", "OK"))

class Window23(QMainWindow, Ui_Form23):#chetyreh ugolnic 2 okna
	def __init__(self):
		super().__init__()
		self.v1=0.0
		self.v2=0.0
		self.setupUi(self)
		self.lineEdit.valueChanged.connect(self.Chan)
		self.lineEdit_2.valueChanged.connect(self.Chan2)
		self.pushButton.clicked.connect(self.iniz)
	def Chan(self):
		self.v1=self.lineEdit.value()
	def Chan2(self):
		self.v2=self.lineEdit_2.value()
	def iniz(self):
		self.g=gmh()
		self.g.in23(self.v2,self.v1)
		self.close()

class Ui_Form24(object): #paralelepiped 3 okna
	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.resize(192, 204)
		self.verticalLayoutWidget = QtWidgets.QWidget(Form)
		self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 191, 181))
		self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
		self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
		self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_4.setObjectName("horizontalLayout_4")
		self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label_2.setMaximumSize(QtCore.QSize(50, 16777215))
		self.label_2.setObjectName("label_2")
		self.horizontalLayout_4.addWidget(self.label_2)
		self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
		self.doubleSpinBox.setMaximum(1.7976931348623158e+308)
		self.doubleSpinBox.setObjectName("doubleSpinBox")
		self.horizontalLayout_4.addWidget(self.doubleSpinBox)
		self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label_4.setMaximumSize(QtCore.QSize(20, 20))
		self.label_4.setObjectName("label_4")
		self.horizontalLayout_4.addWidget(self.label_4)
		self.verticalLayout_2.addLayout(self.horizontalLayout_4)
		self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_3.setObjectName("horizontalLayout_3")
		self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label_11.setMaximumSize(QtCore.QSize(50, 16777215))
		self.label_11.setObjectName("label_11")
		self.horizontalLayout_3.addWidget(self.label_11)
		self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
		self.doubleSpinBox_3.setMaximum(1.7976931348623158e+308)
		self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
		self.horizontalLayout_3.addWidget(self.doubleSpinBox_3)
		self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label_10.setMaximumSize(QtCore.QSize(20, 20))
		self.label_10.setObjectName("label_10")
		self.horizontalLayout_3.addWidget(self.label_10)
		self.verticalLayout_2.addLayout(self.horizontalLayout_3)
		self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_7.setObjectName("horizontalLayout_7")
		self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label_9.setMaximumSize(QtCore.QSize(55, 16777215))
		self.label_9.setObjectName("label_9")
		self.horizontalLayout_7.addWidget(self.label_9)
		self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
		self.doubleSpinBox_2.setMaximum(1.7976931348623158e+308)
		self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
		self.horizontalLayout_7.addWidget(self.doubleSpinBox_2)
		self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label_3.setMaximumSize(QtCore.QSize(20, 20))
		self.label_3.setObjectName("label_3")
		self.horizontalLayout_7.addWidget(self.label_3)
		self.verticalLayout_2.addLayout(self.horizontalLayout_7)
		self.pushButton = QtWidgets.QPushButton(Form)
		self.pushButton.setGeometry(QtCore.QRect(5, 170, 180, 30))
		self.pushButton.setMaximumSize(QtCore.QSize(180, 30))
		self.pushButton.setObjectName("pushButton")

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "Form"))
		self.label_2.setText(_translate("Form", " Высота"))
		self.label_4.setText(_translate("Form", "[м] "))
		self.label_11.setText(_translate("Form", "Радиус 1"))
		self.label_10.setText(_translate("Form", "[м] "))
		self.label_9.setText(_translate("Form", " Радиус 2"))
		self.label_3.setText(_translate("Form", "[м] "))
		self.pushButton.setText(_translate("Form", "OK"))

class Window24(QMainWindow, Ui_Form24):#paralelepiped

	def __init__(self):
		super().__init__()
		self.v1=0.0
		self.v2=0.0
		self.v3=0.0
		self.setupUi(self)
		self.doubleSpinBox.valueChanged.connect(self.Chan)
		self.doubleSpinBox_2.valueChanged.connect(self.Chan2)
		self.doubleSpinBox_3.valueChanged.connect(self.Chan3)
		self.pushButton.clicked.connect(self.iniz)
	def Chan(self):
		self.v1=self.doubleSpinBox.value()
	def Chan2(self):
		self.v2=self.doubleSpinBox_2.value()
	def Chan3(self):
		self.v3=self.doubleSpinBox_3.value()
	def iniz(self):
		g=gmh()
		g.in24(self.v1,self.v2,self.v3)
		self.close()

class Ui_Form28(object): #paralelepiped 3 okna
	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.resize(192, 204)
		self.verticalLayoutWidget = QtWidgets.QWidget(Form)
		self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 191, 181))
		self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
		self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
		self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_4.setObjectName("horizontalLayout_4")
		self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label_2.setMaximumSize(QtCore.QSize(50, 16777215))
		self.label_2.setObjectName("label_2")
		self.horizontalLayout_4.addWidget(self.label_2)
		self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
		self.doubleSpinBox.setMaximum(1.7976931348623158e+308)
		self.doubleSpinBox.setObjectName("doubleSpinBox")
		self.horizontalLayout_4.addWidget(self.doubleSpinBox)
		self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label_4.setMaximumSize(QtCore.QSize(20, 20))
		self.label_4.setObjectName("label_4")
		self.horizontalLayout_4.addWidget(self.label_4)
		self.verticalLayout_2.addLayout(self.horizontalLayout_4)
		self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_3.setObjectName("horizontalLayout_3")
		self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label_11.setMaximumSize(QtCore.QSize(50, 16777215))
		self.label_11.setObjectName("label_11")
		self.horizontalLayout_3.addWidget(self.label_11)
		self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
		self.doubleSpinBox_3.setMaximum(1.7976931348623158e+308)
		self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
		self.horizontalLayout_3.addWidget(self.doubleSpinBox_3)
		self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label_10.setMaximumSize(QtCore.QSize(20, 20))
		self.label_10.setObjectName("label_10")
		self.horizontalLayout_3.addWidget(self.label_10)
		self.verticalLayout_2.addLayout(self.horizontalLayout_3)
		self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_7.setObjectName("horizontalLayout_7")
		self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label_9.setMaximumSize(QtCore.QSize(55, 16777215))
		self.label_9.setObjectName("label_9")
		self.horizontalLayout_7.addWidget(self.label_9)
		self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
		self.doubleSpinBox_2.setMaximum(1.7976931348623158e+308)
		self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
		self.horizontalLayout_7.addWidget(self.doubleSpinBox_2)
		self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label_3.setMaximumSize(QtCore.QSize(20, 20))
		self.label_3.setObjectName("label_3")
		self.horizontalLayout_7.addWidget(self.label_3)
		self.verticalLayout_2.addLayout(self.horizontalLayout_7)
		self.pushButton = QtWidgets.QPushButton(Form)
		self.pushButton.setGeometry(QtCore.QRect(5, 170, 180, 30))
		self.pushButton.setMaximumSize(QtCore.QSize(180, 30))
		self.pushButton.setObjectName("pushButton")

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "Form"))
		self.label_2.setText(_translate("Form", " Высота"))
		self.label_4.setText(_translate("Form", "[м] "))
		self.label_11.setText(_translate("Form", "Ширина"))
		self.label_10.setText(_translate("Form", "[м] "))
		self.label_9.setText(_translate("Form", " Длина"))
		self.label_3.setText(_translate("Form", "[м] "))
		self.pushButton.setText(_translate("Form", "OK"))

class Window28(QMainWindow, Ui_Form28):#paralelepiped

	def __init__(self):
		super().__init__()
		self.v1=0.0
		self.v2=0.0
		self.v3=0.0
		self.setupUi(self)
		self.doubleSpinBox.valueChanged.connect(self.Chan)
		self.doubleSpinBox_2.valueChanged.connect(self.Chan2)
		self.doubleSpinBox_3.valueChanged.connect(self.Chan3)
		self.pushButton.clicked.connect(self.iniz)
	def Chan(self):
		self.v1=self.doubleSpinBox.value()
	def Chan2(self):
		self.v2=self.doubleSpinBox_2.value()
	def Chan3(self):
		self.v3=self.doubleSpinBox_3.value()
	def iniz(self):
		g=gmh()
		g.in28(self.v1,self.v2,self.v3)
		self.close()

class Ui_Form2(object):
	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.resize(201, 185)
		self.verticalLayoutWidget = QtWidgets.QWidget(Form)
		self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 200, 180))
		self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
		self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
		self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_4.setObjectName("horizontalLayout_4")
		self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label_2.setObjectName("label_2")
		self.horizontalLayout_4.addWidget(self.label_2)
		self.lineEdit_2 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
		self.lineEdit_2.setMaximum(1.7976931348623158e+308)
		self.lineEdit_2.setObjectName("lineEdit_2")
		self.horizontalLayout_4.addWidget(self.lineEdit_2)
		self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label_4.setObjectName("label_4")
		self.horizontalLayout_4.addWidget(self.label_4)
		self.verticalLayout_2.addLayout(self.horizontalLayout_4)
		self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_3.setObjectName("horizontalLayout_3")
		self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label.setObjectName("label")
		self.horizontalLayout_3.addWidget(self.label)
		self.lineEdit = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
		self.lineEdit.setMaximum(1.7976931348623157e+308)
		self.lineEdit.setObjectName("lineEdit")
		self.horizontalLayout_3.addWidget(self.lineEdit)
		self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label_3.setObjectName("label_3")
		self.horizontalLayout_3.addWidget(self.label_3)
		self.verticalLayout_2.addLayout(self.horizontalLayout_3)
		self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
		self.pushButton.setObjectName("pushButton")
		self.verticalLayout_2.addWidget(self.pushButton)

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "Form"))
		self.label_2.setText(_translate("Form", " Высота"))
		self.label_4.setText(_translate("Form", "[м] "))
		self.label.setText(_translate("Form", " Ширина"))
		self.label_3.setText(_translate("Form", "[м] "))
		self.pushButton.setText(_translate("Form", "OK"))

class Ui_Form3(object): #paralelepiped 3 okna
	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.resize(192, 204)
		self.verticalLayoutWidget = QtWidgets.QWidget(Form)
		self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 191, 181))
		self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
		self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
		self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_4.setObjectName("horizontalLayout_4")
		self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label_2.setMaximumSize(QtCore.QSize(50, 16777215))
		self.label_2.setObjectName("label_2")
		self.horizontalLayout_4.addWidget(self.label_2)
		self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
		self.doubleSpinBox.setMaximum(1.7976931348623158e+308)
		self.doubleSpinBox.setObjectName("doubleSpinBox")
		self.horizontalLayout_4.addWidget(self.doubleSpinBox)
		self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label_4.setMaximumSize(QtCore.QSize(20, 20))
		self.label_4.setObjectName("label_4")
		self.horizontalLayout_4.addWidget(self.label_4)
		self.verticalLayout_2.addLayout(self.horizontalLayout_4)
		self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_3.setObjectName("horizontalLayout_3")
		self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label_11.setMaximumSize(QtCore.QSize(50, 16777215))
		self.label_11.setObjectName("label_11")
		self.horizontalLayout_3.addWidget(self.label_11)
		self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
		self.doubleSpinBox_3.setMaximum(1.7976931348623158e+308)
		self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
		self.horizontalLayout_3.addWidget(self.doubleSpinBox_3)
		self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label_10.setMaximumSize(QtCore.QSize(20, 20))
		self.label_10.setObjectName("label_10")
		self.horizontalLayout_3.addWidget(self.label_10)
		self.verticalLayout_2.addLayout(self.horizontalLayout_3)
		self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_7.setObjectName("horizontalLayout_7")
		self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label_9.setMaximumSize(QtCore.QSize(55, 16777215))
		self.label_9.setObjectName("label_9")
		self.horizontalLayout_7.addWidget(self.label_9)
		self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
		self.doubleSpinBox_2.setMaximum(1.7976931348623158e+308)
		self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
		self.horizontalLayout_7.addWidget(self.doubleSpinBox_2)
		self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label_3.setMaximumSize(QtCore.QSize(20, 20))
		self.label_3.setObjectName("label_3")
		self.horizontalLayout_7.addWidget(self.label_3)
		self.verticalLayout_2.addLayout(self.horizontalLayout_7)
		self.pushButton = QtWidgets.QPushButton(Form)
		self.pushButton.setGeometry(QtCore.QRect(5, 170, 180, 30))
		self.pushButton.setMaximumSize(QtCore.QSize(180, 30))
		self.pushButton.setObjectName("pushButton")

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "Form"))
		self.label_2.setText(_translate("Form", " Высота"))
		self.label_4.setText(_translate("Form", "[м] "))
		self.label_11.setText(_translate("Form", "Ширина"))
		self.label_10.setText(_translate("Form", "[м] "))
		self.label_9.setText(_translate("Form", " Глубина"))
		self.label_3.setText(_translate("Form", "[м] "))
		self.pushButton.setText(_translate("Form", "OK"))

class Ui_Form4(object): #krug 1 okno
	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.resize(200, 90)
		self.pushButton = QtWidgets.QPushButton(Form)
		self.pushButton.setGeometry(QtCore.QRect(10, 50, 180, 28))
		self.pushButton.setObjectName("pushButton")
		self.label_2 = QtWidgets.QLabel(Form)
		self.label_2.setGeometry(QtCore.QRect(10, 10, 50, 20))
		self.label_2.setObjectName("label_2")
		self.doubleSpinBox = QtWidgets.QDoubleSpinBox(Form)
		self.doubleSpinBox.setMaximum(1.7976931348623158e+308)
		self.doubleSpinBox.setGeometry(QtCore.QRect(70, 10, 90, 20))
		self.doubleSpinBox.setObjectName("doubleSpinBox")
		self.label_4 = QtWidgets.QLabel(Form)
		self.label_4.setGeometry(QtCore.QRect(175, 10, 31, 20))
		self.label_4.setObjectName("label_4")

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "Form"))
		self.pushButton.setText(_translate("Form", "OK"))
		self.label_2.setText(_translate("Form", "Радиус"))
		self.label_4.setText(_translate("Form", "[м] "))

class Ui_Form5(object): #kolichwstvo tochek
	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.resize(220, 90)
		self.pushButton = QtWidgets.QPushButton(Form)
		self.pushButton.setGeometry(QtCore.QRect(10, 50, 199, 28))
		self.pushButton.setObjectName("pushButton")
		self.label_2 = QtWidgets.QLabel(Form)
		self.label_2.setGeometry(QtCore.QRect(10, 10, 110, 20))
		self.label_2.setObjectName("label_2")
		self.doubleSpinBox = QtWidgets.QSpinBox(Form)
		self.doubleSpinBox.setGeometry(QtCore.QRect(120, 10, 90, 20))
		self.doubleSpinBox.setObjectName("doubleSpinBox")
 

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "Form"))
		self.pushButton.setText(_translate("Form", "OK"))
		self.label_2.setText(_translate("Form", "Количество точек"))

class Ui_Form6(object): #input of points
	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.resize(390, 400)
		self.spinBox = QtWidgets.QSpinBox(Form)
		self.spinBox.setGeometry(QtCore.QRect(210, 15, 40, 20))
		self.spinBox.setObjectName("spinBox")
		self.label = QtWidgets.QLabel(Form)
		self.label.setGeometry(QtCore.QRect(10, 15, 170, 20))
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(Form)
		self.label_2.setGeometry(QtCore.QRect(10, 40, 360, 30))
		self.label_2.setObjectName("label_2")
		self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
		self.plainTextEdit.setGeometry(QtCore.QRect(10, 70, 370, 270))
		self.plainTextEdit.setObjectName("plainTextEdit")
		self.pushButton = QtWidgets.QPushButton(Form)
		self.pushButton.setGeometry(QtCore.QRect(10, 350, 370, 40))
		self.pushButton.setObjectName("pushButton")

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "Окно ввода"))
		self.label.setText(_translate("Form", "Введите количество точек"))
		self.label_2.setText(_translate("Form", "Введите точки через пробел, каждая пара на новой строке"))
		self.pushButton.setText(_translate("Form", "OK"))

class Window6(QMainWindow, Ui_Form6):#input of points
	def __init__(self):
		super().__init__()
		self.v=0.0
		self.p=[]
		self.setupUi(self)
		self.spinBox.valueChanged.connect(self.Chan)
		self.pushButton.clicked.connect(self.iniz)
	def Chan(self):
		self.v=int(self.spinBox.value())
	def iniz(self):
		text = self.plainTextEdit.toPlainText()
		g=gmh()
		g.in4(self.v,text)
		self.close()

class Window5(QMainWindow, Ui_Form5):#krug
	def __init__(self):
		super().__init__()
		self.v=0.0
		self.setupUi(self)
		self.doubleSpinBox.valueChanged.connect(self.Chan)
		self.pushButton.clicked.connect(self.iniz)
	def Chan(self):
		self.v=self.doubleSpinBox.value()
	def iniz(self):
		global figura
		if (figura == 1):
			g=gmh()
			g.in1(self.v)
		if (figura == 6):
			g=gmh()
			g.in6(self.v)
		self.close()

class Window3(QMainWindow, Ui_Form3):#paralelepiped

	def __init__(self):
		super().__init__()
		self.v1=0.0
		self.v2=0.0
		self.v3=0.0
		self.setupUi(self)
		self.doubleSpinBox.valueChanged.connect(self.Chan)
		self.doubleSpinBox_2.valueChanged.connect(self.Chan2)
		self.doubleSpinBox_3.valueChanged.connect(self.Chan3)
		self.pushButton.clicked.connect(self.iniz)
	def Chan(self):
		self.v1=self.doubleSpinBox.value()
	def Chan2(self):
		self.v2=self.doubleSpinBox_2.value()
	def Chan3(self):
		self.v3=self.doubleSpinBox_3.value()
	def iniz(self):
		g=gmh()
		g.in7(self.v1,self.v2,self.v3)
		self.close()

class Window4(QMainWindow, Ui_Form4):#radius
	def __init__(self):
		super().__init__()
		self.v=0.0
		self.setupUi(self)
		self.doubleSpinBox.valueChanged.connect(self.Chan)
		self.pushButton.clicked.connect(self.iniz)
	def Chan(self):
		self.v=self.doubleSpinBox.value()
	def iniz(self):
		global figura
		if (figura == 1):
			g=gmh()
			g.in1(self.v)
		if (figura == 6):
			g=gmh()
			g.in6(self.v)
		self.close()

class Window2(QMainWindow, Ui_Form2):#chetyreh ugolnic 2 okna
	def __init__(self):
		super().__init__()
		self.v1=0.0
		self.v2=0.0
		self.setupUi(self)
		self.lineEdit.valueChanged.connect(self.Chan)
		self.lineEdit_2.valueChanged.connect(self.Chan2)
		self.pushButton.clicked.connect(self.iniz)
	def Chan(self):
		self.v1=self.lineEdit.value()
	def Chan2(self):
		self.v2=self.lineEdit_2.value()
	def iniz(self):
		if (figura == 2) :
			g=gmh()
			g.in2(self.v1,self.v2)
		if (figura == 3):
			g=gmh()
			g.in3(self.v1,self.v2)
		
		self.close()

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(800, 450)
		MainWindow.setMinimumSize(QtCore.QSize(800, 450))
		MainWindow.setMaximumSize(QtCore.QSize(800, 450))
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
		self.tabWidget.setGeometry(QtCore.QRect(0, 0, 800, 450))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.tabWidget.setFont(font)
		self.tabWidget.setObjectName("tabWidget")
		self.tab = QtWidgets.QWidget()
		font = QtGui.QFont()
		font.setPointSize(12)
		self.tab.setFont(font)
		self.tab.setObjectName("tab")
		self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab)
		self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 770, 90))
		self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
		self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
		self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
		self.pushButton_3.setObjectName("pushButton_3")
		self.horizontalLayout.addWidget(self.pushButton_3)
		self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
		self.pushButton_2.setObjectName("pushButton_2")
		self.horizontalLayout.addWidget(self.pushButton_2)
		self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
		self.pushButton.setObjectName("pushButton")
		self.horizontalLayout.addWidget(self.pushButton)
		self.label = QtWidgets.QLabel(self.tab)
		self.label.setGeometry(QtCore.QRect(10, 95, 770, 200))
		self.label.setText("")
		self.label.setPixmap(QtGui.QPixmap("1.png"))
		self.label.setObjectName("label")
		self.pushButton_4 = QtWidgets.QPushButton(self.tab)
		self.pushButton_4.setGeometry(QtCore.QRect(50, 310, 700, 60))
		self.pushButton_4.setObjectName("pushButton_4")
		self.tabWidget.addTab(self.tab, "")
		self.tab_2 = QtWidgets.QWidget()
		self.tab_2.setObjectName("tab_2")
		self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_2)
		self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 790, 390))
		self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
		self.verticalLayout.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout.setObjectName("verticalLayout")
		self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_11.setObjectName("horizontalLayout_11")
		self.pushButton_27 = QtWidgets.QPushButton(self.verticalLayoutWidget)
		self.pushButton_27.setObjectName("pushButton_27")
		
		
		self.horizontalLayout_11.addWidget(self.pushButton_27)
		self.pushButton_28 = QtWidgets.QPushButton(self.verticalLayoutWidget)
		self.pushButton_28.setObjectName("pushButton_28")
		self.horizontalLayout_11.addWidget(self.pushButton_28)
		self.verticalLayout.addLayout(self.horizontalLayout_11)
		self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_10.setObjectName("horizontalLayout_10")
		self.pushButton_25 = QtWidgets.QPushButton(self.verticalLayoutWidget)
		self.pushButton_25.setObjectName("pushButton_25")
		self.horizontalLayout_10.addWidget(self.pushButton_25)
		self.pushButton_26 = QtWidgets.QPushButton(self.verticalLayoutWidget)
		self.pushButton_26.setObjectName("pushButton_26")
		self.horizontalLayout_10.addWidget(self.pushButton_26)
		self.verticalLayout.addLayout(self.horizontalLayout_10)
		self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_9.setObjectName("horizontalLayout_9")
		self.pushButton_23 = QtWidgets.QPushButton(self.verticalLayoutWidget)
		self.pushButton_23.setObjectName("pushButton_23")
		self.horizontalLayout_9.addWidget(self.pushButton_23)
		self.pushButton_24 = QtWidgets.QPushButton(self.verticalLayoutWidget)
		self.pushButton_24.setObjectName("pushButton_24")
		self.horizontalLayout_9.addWidget(self.pushButton_24)
		self.verticalLayout.addLayout(self.horizontalLayout_9)
		self.tabWidget.addTab(self.tab_2, "")
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
		self.menubar.setObjectName("menubar")
		self.menu = QtWidgets.QMenu(self.menubar)
		self.menu.setObjectName("menu")
		self.menu_2 = QtWidgets.QMenu(self.menubar)
		self.menu_2.setObjectName("menu_2")
		self.menu_3 = QtWidgets.QMenu(self.menubar)
		self.menu_3.setObjectName("menu_3")
		MainWindow.setMenuBar(self.menubar)
		self.action = QtWidgets.QAction(MainWindow)
		self.action.setObjectName("action")
		self.action_2 = QtWidgets.QAction(MainWindow)
		self.action_2.setObjectName("action_2")
		self.action_3 = QtWidgets.QAction(MainWindow)
		self.action_3.setObjectName("action_3")
		self.action_4 = QtWidgets.QAction(MainWindow)
		self.action_4.setObjectName("action_4")
		self.action_5 = QtWidgets.QAction(MainWindow)
		self.action_5.setObjectName("action_5")
		self.action_6 = QtWidgets.QAction(MainWindow)
		self.action_6.setObjectName("action_6")
		self.action_7 = QtWidgets.QAction(MainWindow)
		self.action_7.setObjectName("action_7")
		self.action_8 = QtWidgets.QAction(MainWindow)
		self.action_8.setObjectName("action_8")
		self.menu.addAction(self.action_4)
		self.menu.addAction(self.action_5)
		self.menu.addAction(self.action_6)
		self.menu_2.addAction(self.action_7)
		self.menu_2.addAction(self.action_8)
		self.menu_3.addAction(self.action)
		self.menu_3.addAction(self.action_2)
		self.menu_3.addAction(self.action_3)
		self.menubar.addAction(self.menu.menuAction())
		self.menubar.addAction(self.menu_2.menuAction())
		self.menubar.addAction(self.menu_3.menuAction())

		self.retranslateUi(MainWindow)
		self.tabWidget.setCurrentIndex(0)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)\


	def retranslateUi(self, MainWindow):

		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "Automatic mesh generator"))
		self.pushButton_3.setText(_translate("MainWindow", "Прямоугольник"))
		self.pushButton_2.setText(_translate("MainWindow", "Треугольник"))
		self.pushButton.setText(_translate("MainWindow", "Круг"))
		self.pushButton_4.setText(_translate("MainWindow", "Создать свою фигуру"))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "2D"))
		self.pushButton_27.setText(_translate("MainWindow", "Параллелепипед"))
		self.pushButton_28.setText(_translate("MainWindow", "Клин"))
		self.pushButton_25.setText(_translate("MainWindow", "Сфера"))
		self.pushButton_26.setText(_translate("MainWindow", "Тор"))
		self.pushButton_23.setText(_translate("MainWindow", "Цилиндр"))
		self.pushButton_24.setText(_translate("MainWindow", "Конус"))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "3D"))
		self.menu.setTitle(_translate("MainWindow", "Файл"))
		self.menu_2.setTitle(_translate("MainWindow", "Вид"))
		self.menu_3.setTitle(_translate("MainWindow", "Справка"))
		self.action.setText(_translate("MainWindow", "Нажмите"))
		self.action_2.setText(_translate("MainWindow", "Понравившуюся"))
		self.action_3.setText(_translate("MainWindow", "Кнопку"))
		self.action_4.setText(_translate("MainWindow", "Тут"))
		self.action_5.setText(_translate("MainWindow", "Ничего"))
		self.action_6.setText(_translate("MainWindow", "Нет"))
		self.action_7.setText(_translate("MainWindow", "Тут"))
		self.action_8.setText(_translate("MainWindow", "Тоже"))

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.dt = date.today()
		#self.poradok=0
		#self.a=0.1
		#self.b=0.1
		#self.c=0.1
		self.pushButton.clicked.connect(lambda: self.inpk(1)) #KRUG
		self.pushButton_2.clicked.connect(lambda:self.inp(2)) #treugolnik
		self.pushButton_3.clicked.connect(lambda:self.inp(3)) #pramougoknik
		self.pushButton_4.clicked.connect(lambda:self.inps())#svoa figura
		self.pushButton_25.clicked.connect(lambda:self.inpk(6))#krug sphere
		self.pushButton_27.clicked.connect(lambda:self.inpp())#paralelepiped
		self.pushButton_26.clicked.connect(lambda:self.inptor())#tor
		self.pushButton_23.clicked.connect(lambda:self.inpcyl())#cyl
		self.pushButton_24.clicked.connect(lambda:self.inpcon())#conus
		self.pushButton_28.clicked.connect(lambda:self.inpwedge())#wedge


	def inpk(self,fg):#KRUG#shar
		global figura
		figura = fg
		self.coc=Window4()
		self.coc.show()

	def inpwedge(self):#cyl
		self.coc=Window28()
		self.coc.show()


	def inpcyl(self):#cyl
		self.coc=Window23()
		self.coc.show()

	def inpcon(self):#conus
		self.coc=Window24()
		self.coc.show()

	def inptor(self):#tor
		self.coc=Window26()
		self.coc.show()

	def inpp(self):#paralelepiped
		self.coc=Window3()
		self.coc.show()

	def inps(self):#own
		self.coc=Window6()
		self.coc.show()

	def inp(self,fg):#pramougoknik treugolnik
		global figura
		figura = fg
		self.coc=Window2()
		self.coc.show()

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	ui = MainWindow()
	ui.show()
	sys.exit(app.exec_())
