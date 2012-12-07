# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '925_gui.ui'
#
# Created: Fri Dec  7 16:45:01 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

#CHANGES FROM AUTO CREATION
#1) Ui_MainWindow class inherits the QtGui.QMainWindow
#2) Passed Ui_MainWindow the mainwindow instance
#3) Wrote the whole init function
#4) Wrote everything not in the Ui_MainWindow class


from PyQt4 import QtCore, QtGui
import sys

class Ui_MainWindow(QtGui.QMainWindow):

    def __init__(self):
    	'''Initialize the GUI window'''
    	self.main_gui = QtGui.QMainWindow()
    	self.setupUi(self.main_gui)
    	self.main_gui.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(872, 690)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 610, 791, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.pressure_plot_widget = QtGui.QWidget(self.centralwidget)
        self.pressure_plot_widget.setGeometry(QtCore.QRect(139, 179, 551, 251))
        self.pressure_plot_widget.setObjectName(_fromUtf8("pressure_plot_widget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(140, 449, 551, 81))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(40)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.setpoint1_label = QtGui.QLabel(self.widget)
        self.setpoint1_label.setTextFormat(QtCore.Qt.LogText)
        self.setpoint1_label.setAlignment(QtCore.Qt.AlignCenter)
        self.setpoint1_label.setObjectName(_fromUtf8("setpoint1_label"))
        self.verticalLayout.addWidget(self.setpoint1_label)
        self.lineEdit_setpoint1 = QtGui.QLineEdit(self.widget)
        self.lineEdit_setpoint1.setObjectName(_fromUtf8("lineEdit_setpoint1"))
        self.verticalLayout.addWidget(self.lineEdit_setpoint1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.setpoint2_label = QtGui.QLabel(self.widget)
        self.setpoint2_label.setTextFormat(QtCore.Qt.LogText)
        self.setpoint2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.setpoint2_label.setObjectName(_fromUtf8("setpoint2_label"))
        self.verticalLayout_2.addWidget(self.setpoint2_label)
        self.lineEdit_setpoint2 = QtGui.QLineEdit(self.widget)
        self.lineEdit_setpoint2.setObjectName(_fromUtf8("lineEdit_setpoint2"))
        self.verticalLayout_2.addWidget(self.lineEdit_setpoint2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.setpoint2_label_2 = QtGui.QLabel(self.widget)
        self.setpoint2_label_2.setTextFormat(QtCore.Qt.LogText)
        self.setpoint2_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.setpoint2_label_2.setObjectName(_fromUtf8("setpoint2_label_2"))
        self.verticalLayout_3.addWidget(self.setpoint2_label_2)
        self.lineEdit_setpoint2_2 = QtGui.QLineEdit(self.widget)
        self.lineEdit_setpoint2_2.setObjectName(_fromUtf8("lineEdit_setpoint2_2"))
        self.verticalLayout_3.addWidget(self.lineEdit_setpoint2_2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.widget1 = QtGui.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(111, 21, 591, 111))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pressure_number = QtGui.QLCDNumber(self.widget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pressure_number.sizePolicy().hasHeightForWidth())
        self.pressure_number.setSizePolicy(sizePolicy)
        self.pressure_number.setObjectName(_fromUtf8("pressure_number"))
        self.horizontalLayout_2.addWidget(self.pressure_number)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.units_label = QtGui.QLabel(self.widget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.units_label.sizePolicy().hasHeightForWidth())
        self.units_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(64)
        self.units_label.setFont(font)
        self.units_label.setTextFormat(QtCore.Qt.AutoText)
        self.units_label.setAlignment(QtCore.Qt.AlignCenter)
        self.units_label.setObjectName(_fromUtf8("units_label"))
        self.verticalLayout_4.addWidget(self.units_label)
        self.units_comboBox = QtGui.QComboBox(self.widget1)
        self.units_comboBox.setObjectName(_fromUtf8("units_comboBox"))
        self.verticalLayout_4.addWidget(self.units_comboBox)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.widget2 = QtGui.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(140, 550, 551, 32))
        self.widget2.setObjectName(_fromUtf8("widget2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setSpacing(79)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.update_setpoints_button = QtGui.QPushButton(self.widget2)
        self.update_setpoints_button.setEnabled(False)
        self.update_setpoints_button.setObjectName(_fromUtf8("update_setpoints_button"))
        self.horizontalLayout_3.addWidget(self.update_setpoints_button)
        self.reset_button = QtGui.QPushButton(self.widget2)
        self.reset_button.setObjectName(_fromUtf8("reset_button"))
        self.horizontalLayout_3.addWidget(self.reset_button)
        self.start_stop_button = QtGui.QPushButton(self.widget2)
        self.start_stop_button.setObjectName(_fromUtf8("start_stop_button"))
        self.horizontalLayout_3.addWidget(self.start_stop_button)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 872, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionReset = QtGui.QAction(MainWindow)
        self.actionReset.setObjectName(_fromUtf8("actionReset"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionReset)
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.start_stop_button, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), MainWindow.raise_)
        QtCore.QObject.connect(self.reset_button, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), MainWindow.raise_)
        QtCore.QObject.connect(self.update_setpoints_button, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), MainWindow.raise_)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.setpoint1_label.setText(QtGui.QApplication.translate("MainWindow", "Set Point 1", None, QtGui.QApplication.UnicodeUTF8))
        self.setpoint2_label.setText(QtGui.QApplication.translate("MainWindow", "Set Point 2", None, QtGui.QApplication.UnicodeUTF8))
        self.setpoint2_label_2.setText(QtGui.QApplication.translate("MainWindow", "Set Point 1", None, QtGui.QApplication.UnicodeUTF8))
        self.units_label.setText(QtGui.QApplication.translate("MainWindow", "Torr", None, QtGui.QApplication.UnicodeUTF8))
        self.units_comboBox.setToolTip(QtGui.QApplication.translate("MainWindow", "Pressure Units", None, QtGui.QApplication.UnicodeUTF8))
        self.update_setpoints_button.setText(QtGui.QApplication.translate("MainWindow", "Update Set Points", None, QtGui.QApplication.UnicodeUTF8))
        self.reset_button.setText(QtGui.QApplication.translate("MainWindow", "Reset Plot", None, QtGui.QApplication.UnicodeUTF8))
        self.start_stop_button.setText(QtGui.QApplication.translate("MainWindow", "Start / Stop Gauge", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReset.setText(QtGui.QApplication.translate("MainWindow", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))

if __name__ == "__main__":
    #==========================================Setup Parameters
    
	try:
		_fromUtf8 = QtCore.QString.fromUtf8
	except AttributeError:
		_fromUtf8 = lambda s: s
	
	app = QtGui.QApplication(sys.argv)

	#Create class instances
	GUI = Ui_MainWindow()
	
	
	sys.exit(app.exec_())
