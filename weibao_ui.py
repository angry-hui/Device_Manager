# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'weibao.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModal)
        MainWindow.resize(1333, 949)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_7 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(16777215, 45))
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font.setPointSize(10)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.Le_ID = QLineEdit(self.groupBox_2)
        self.Le_ID.setObjectName(u"Le_ID")
        self.Le_ID.setMaximumSize(QSize(100, 16777215))
        self.Le_ID.setFont(font)

        self.horizontalLayout.addWidget(self.Le_ID)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout.addWidget(self.label_2)

        self.Le_User = QLineEdit(self.groupBox_2)
        self.Le_User.setObjectName(u"Le_User")
        self.Le_User.setMaximumSize(QSize(100, 16777215))
        self.Le_User.setFont(font)

        self.horizontalLayout.addWidget(self.Le_User)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.horizontalLayout.addWidget(self.label_4)

        self.lineEdit_IP_Query = QLineEdit(self.groupBox_2)
        self.lineEdit_IP_Query.setObjectName(u"lineEdit_IP_Query")
        self.lineEdit_IP_Query.setMinimumSize(QSize(150, 0))
        self.lineEdit_IP_Query.setMaximumSize(QSize(100, 16777215))
        self.lineEdit_IP_Query.setFont(font)

        self.horizontalLayout.addWidget(self.lineEdit_IP_Query)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.horizontalLayout.addWidget(self.label_5)

        self.comboBox_State = QComboBox(self.groupBox_2)
        self.comboBox_State.setObjectName(u"comboBox_State")
        self.comboBox_State.setMinimumSize(QSize(25, 20))
        self.comboBox_State.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.comboBox_State.setEditable(True)

        self.horizontalLayout.addWidget(self.comboBox_State)

        self.Pb_Query = QPushButton(self.groupBox_2)
        self.Pb_Query.setObjectName(u"Pb_Query")
        self.Pb_Query.setFont(font)

        self.horizontalLayout.addWidget(self.Pb_Query)

        self.horizontalSpacer = QSpacerItem(40, 13, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_Trace = QPushButton(self.groupBox_2)
        self.pushButton_Trace.setObjectName(u"pushButton_Trace")
        self.pushButton_Trace.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")

        self.horizontalLayout.addWidget(self.pushButton_Trace)

        self.pushButton_analysis = QPushButton(self.groupBox_2)
        self.pushButton_analysis.setObjectName(u"pushButton_analysis")
        self.pushButton_analysis.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_analysis)

        self.pushButton_Ip_Manager = QPushButton(self.groupBox_2)
        self.pushButton_Ip_Manager.setObjectName(u"pushButton_Ip_Manager")
        self.pushButton_Ip_Manager.setEnabled(False)
        self.pushButton_Ip_Manager.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")

        self.horizontalLayout.addWidget(self.pushButton_Ip_Manager)

        self.pushButton_2 = QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.Tb_Device = QTableView(self.centralwidget)
        self.Tb_Device.setObjectName(u"Tb_Device")
        self.Tb_Device.setMinimumSize(QSize(0, 200))
        self.Tb_Device.setMaximumSize(QSize(2000, 285))
        self.Tb_Device.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.Tb_Device.horizontalHeader().setMinimumSectionSize(15)
        self.Tb_Device.horizontalHeader().setDefaultSectionSize(90)
        self.Tb_Device.horizontalHeader().setProperty("showSortIndicator", True)
        self.Tb_Device.horizontalHeader().setStretchLastSection(True)
        self.Tb_Device.verticalHeader().setVisible(False)
        self.Tb_Device.verticalHeader().setDefaultSectionSize(33)

        self.verticalLayout.addWidget(self.Tb_Device)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMaximumSize(QSize(16777215, 520))
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet(u"gridline-color: rgb(85, 85, 255);")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.horizontalLayout_8 = QHBoxLayout(self.tab_3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.comboBox_ios = QComboBox(self.tab_3)
        self.comboBox_ios.setObjectName(u"comboBox_ios")
        self.comboBox_ios.setMinimumSize(QSize(100, 25))
        self.comboBox_ios.setMaximumSize(QSize(100, 16777215))
        self.comboBox_ios.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.comboBox_ios.setEditable(True)

        self.gridLayout.addWidget(self.comboBox_ios, 0, 7, 1, 1)

        self.Cb_State = QComboBox(self.tab_3)
        self.Cb_State.setObjectName(u"Cb_State")
        self.Cb_State.setMinimumSize(QSize(100, 25))
        self.Cb_State.setMaximumSize(QSize(100, 16777215))
        self.Cb_State.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.Cb_State.setEditable(True)

        self.gridLayout.addWidget(self.Cb_State, 2, 7, 1, 1)

        self.Cb_baoxiu = QComboBox(self.tab_3)
        self.Cb_baoxiu.setObjectName(u"Cb_baoxiu")
        self.Cb_baoxiu.setMinimumSize(QSize(100, 25))
        self.Cb_baoxiu.setMaximumSize(QSize(300, 16777215))
        self.Cb_baoxiu.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.Cb_baoxiu.setEditable(True)

        self.gridLayout.addWidget(self.Cb_baoxiu, 2, 5, 1, 1)

        self.label_8 = QLabel(self.tab_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(30, 0))
        self.label_8.setMaximumSize(QSize(80, 16777215))
        self.label_8.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_8, 0, 2, 1, 1)

        self.label_22 = QLabel(self.tab_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(30, 0))
        self.label_22.setMaximumSize(QSize(80, 16777215))
        self.label_22.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_22.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_22, 2, 2, 1, 1)

        self.Le_Userinfo = QLineEdit(self.tab_3)
        self.Le_Userinfo.setObjectName(u"Le_Userinfo")
        self.Le_Userinfo.setMinimumSize(QSize(30, 25))
        self.Le_Userinfo.setMaximumSize(QSize(100, 16777215))
        self.Le_Userinfo.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")

        self.gridLayout.addWidget(self.Le_Userinfo, 0, 9, 1, 1)

        self.Cb_Provider = QComboBox(self.tab_3)
        self.Cb_Provider.setObjectName(u"Cb_Provider")
        self.Cb_Provider.setMinimumSize(QSize(100, 25))
        self.Cb_Provider.setMaximumSize(QSize(300, 16777215))
        self.Cb_Provider.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.Cb_Provider.setEditable(True)

        self.gridLayout.addWidget(self.Cb_Provider, 2, 3, 1, 1)

        self.Le_Title = QLineEdit(self.tab_3)
        self.Le_Title.setObjectName(u"Le_Title")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Le_Title.sizePolicy().hasHeightForWidth())
        self.Le_Title.setSizePolicy(sizePolicy1)
        self.Le_Title.setMinimumSize(QSize(10, 25))
        self.Le_Title.setMaximumSize(QSize(100, 16777215))
        self.Le_Title.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.Le_Title.setReadOnly(True)

        self.gridLayout.addWidget(self.Le_Title, 2, 9, 1, 1)

        self.label_19 = QLabel(self.tab_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(30, 0))
        self.label_19.setMaximumSize(QSize(80, 16777215))
        self.label_19.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_19, 1, 2, 1, 1)

        self.label_32 = QLabel(self.tab_3)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(30, 0))
        self.label_32.setMaximumSize(QSize(80, 16777215))
        self.label_32.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_32.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_32, 0, 6, 1, 1)

        self.label_7 = QLabel(self.tab_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(30, 0))
        self.label_7.setMaximumSize(QSize(80, 16777215))
        self.label_7.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)

        self.label_24 = QLabel(self.tab_3)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(30, 0))
        self.label_24.setMaximumSize(QSize(80, 16777215))
        self.label_24.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_24.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_24, 2, 6, 1, 1)

        self.label_9 = QLabel(self.tab_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(30, 0))
        self.label_9.setMaximumSize(QSize(80, 16777215))
        self.label_9.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_9, 0, 4, 1, 1)

        self.label_21 = QLabel(self.tab_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(30, 0))
        self.label_21.setMaximumSize(QSize(80, 16777215))
        self.label_21.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_21.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_21, 1, 6, 1, 1)

        self.label_3 = QLabel(self.tab_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(30, 0))
        self.label_3.setMaximumSize(QSize(80, 16777215))
        self.label_3.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_27 = QLabel(self.tab_3)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(30, 0))
        self.label_27.setMaximumSize(QSize(80, 16777215))
        self.label_27.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_27.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_27, 2, 8, 1, 1)

        self.label_23 = QLabel(self.tab_3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(30, 0))
        self.label_23.setMaximumSize(QSize(80, 16777215))
        self.label_23.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_23.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_23, 2, 4, 1, 1)

        self.Cb_Type = QComboBox(self.tab_3)
        self.Cb_Type.setObjectName(u"Cb_Type")
        self.Cb_Type.setMinimumSize(QSize(100, 25))
        self.Cb_Type.setMaximumSize(QSize(300, 16777215))
        self.Cb_Type.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.Cb_Type.setEditable(True)

        self.gridLayout.addWidget(self.Cb_Type, 0, 3, 1, 1)

        self.Cb_SolidDisk = QComboBox(self.tab_3)
        self.Cb_SolidDisk.setObjectName(u"Cb_SolidDisk")
        self.Cb_SolidDisk.setMinimumSize(QSize(100, 25))
        self.Cb_SolidDisk.setMaximumSize(QSize(300, 16777215))
        self.Cb_SolidDisk.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.Cb_SolidDisk.setEditable(True)

        self.gridLayout.addWidget(self.Cb_SolidDisk, 1, 5, 1, 1)

        self.Cb_Memory = QComboBox(self.tab_3)
        self.Cb_Memory.setObjectName(u"Cb_Memory")
        self.Cb_Memory.setMinimumSize(QSize(100, 25))
        self.Cb_Memory.setMaximumSize(QSize(300, 16777215))
        self.Cb_Memory.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.Cb_Memory.setEditable(True)

        self.gridLayout.addWidget(self.Cb_Memory, 1, 3, 1, 1)

        self.label_6 = QLabel(self.tab_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(60, 0))
        self.label_6.setMaximumSize(QSize(80, 16777215))
        self.label_6.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.Cb_CPU = QComboBox(self.tab_3)
        self.Cb_CPU.setObjectName(u"Cb_CPU")
        self.Cb_CPU.setMinimumSize(QSize(100, 25))
        self.Cb_CPU.setMaximumSize(QSize(300, 16777215))
        self.Cb_CPU.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.Cb_CPU.setEditable(True)

        self.gridLayout.addWidget(self.Cb_CPU, 1, 1, 1, 1)

        self.label_20 = QLabel(self.tab_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(30, 0))
        self.label_20.setMaximumSize(QSize(80, 16777215))
        self.label_20.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_20, 1, 4, 1, 1)

        self.label_31 = QLabel(self.tab_3)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(30, 0))
        self.label_31.setMaximumSize(QSize(80, 16777215))
        self.label_31.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_31.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_31, 1, 8, 1, 1)

        self.Cb_Branch = QComboBox(self.tab_3)
        self.Cb_Branch.setObjectName(u"Cb_Branch")
        self.Cb_Branch.setMinimumSize(QSize(100, 25))
        self.Cb_Branch.setMaximumSize(QSize(300, 16777215))
        self.Cb_Branch.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.Cb_Branch.setEditable(True)

        self.gridLayout.addWidget(self.Cb_Branch, 0, 1, 1, 1)

        self.Cb_Level = QComboBox(self.tab_3)
        self.Cb_Level.setObjectName(u"Cb_Level")
        self.Cb_Level.setMinimumSize(QSize(100, 25))
        self.Cb_Level.setMaximumSize(QSize(300, 16777215))
        self.Cb_Level.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.Cb_Level.setEditable(True)

        self.gridLayout.addWidget(self.Cb_Level, 0, 5, 1, 1)

        self.Cb_MachineDisk = QComboBox(self.tab_3)
        self.Cb_MachineDisk.setObjectName(u"Cb_MachineDisk")
        self.Cb_MachineDisk.setMinimumSize(QSize(100, 25))
        self.Cb_MachineDisk.setMaximumSize(QSize(100, 16777215))
        self.Cb_MachineDisk.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.Cb_MachineDisk.setEditable(True)

        self.gridLayout.addWidget(self.Cb_MachineDisk, 1, 7, 1, 1)

        self.label_25 = QLabel(self.tab_3)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(30, 0))
        self.label_25.setMaximumSize(QSize(80, 16777215))
        self.label_25.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_25.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_25, 0, 8, 1, 1)

        self.lineEdit_Dept = QLineEdit(self.tab_3)
        self.lineEdit_Dept.setObjectName(u"lineEdit_Dept")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_Dept.sizePolicy().hasHeightForWidth())
        self.lineEdit_Dept.setSizePolicy(sizePolicy2)
        self.lineEdit_Dept.setMinimumSize(QSize(30, 25))
        self.lineEdit_Dept.setMaximumSize(QSize(100, 16777215))
        self.lineEdit_Dept.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.lineEdit_Dept.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_Dept, 1, 9, 1, 1)

        self.dateEdit = QDateEdit(self.tab_3)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMinimumSize(QSize(100, 25))
        self.dateEdit.setMaximumSize(QSize(300, 16777215))
        self.dateEdit.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.dateEdit.setCalendarPopup(True)

        self.gridLayout.addWidget(self.dateEdit, 2, 1, 1, 1)

        self.label_10 = QLabel(self.tab_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(30, 0))
        self.label_10.setMaximumSize(QSize(80, 16777215))
        self.label_10.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_10, 0, 10, 1, 1)

        self.label_26 = QLabel(self.tab_3)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(30, 0))
        self.label_26.setMaximumSize(QSize(80, 16777215))
        self.label_26.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_26.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_26, 1, 10, 1, 1)

        self.lineEdit_Ip = QLineEdit(self.tab_3)
        self.lineEdit_Ip.setObjectName(u"lineEdit_Ip")
        self.lineEdit_Ip.setMinimumSize(QSize(100, 25))
        self.lineEdit_Ip.setMaximumSize(QSize(100, 16777215))
        self.lineEdit_Ip.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")

        self.gridLayout.addWidget(self.lineEdit_Ip, 1, 11, 1, 1)

        self.lineEdit_model = QLineEdit(self.tab_3)
        self.lineEdit_model.setObjectName(u"lineEdit_model")
        self.lineEdit_model.setMinimumSize(QSize(100, 25))
        self.lineEdit_model.setMaximumSize(QSize(100, 16777215))
        self.lineEdit_model.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")

        self.gridLayout.addWidget(self.lineEdit_model, 0, 11, 1, 1)


        self.horizontalLayout_6.addLayout(self.gridLayout)

        self.Pb_Update = QPushButton(self.tab_3)
        self.Pb_Update.setObjectName(u"Pb_Update")
        self.Pb_Update.setMinimumSize(QSize(0, 80))
        self.Pb_Update.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")

        self.horizontalLayout_6.addWidget(self.Pb_Update)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.lineEdit_Remark = QLineEdit(self.tab_3)
        self.lineEdit_Remark.setObjectName(u"lineEdit_Remark")
        self.lineEdit_Remark.setMinimumSize(QSize(0, 450))
        self.lineEdit_Remark.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.lineEdit_Remark.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.lineEdit_Remark)


        self.horizontalLayout_8.addLayout(self.verticalLayout_3)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_5 = QHBoxLayout(self.tab)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Tb_WB = QTableView(self.tab)
        self.Tb_WB.setObjectName(u"Tb_WB")
        self.Tb_WB.setMaximumSize(QSize(220, 16777215))
        self.Tb_WB.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.Tb_WB.horizontalHeader().setDefaultSectionSize(100)

        self.horizontalLayout_3.addWidget(self.Tb_WB)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_28 = QLabel(self.tab)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(40, 0))
        self.label_28.setMaximumSize(QSize(40, 16777215))
        self.label_28.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_28.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_28)

        self.comboBox_wb_type = QComboBox(self.tab)
        self.comboBox_wb_type.setObjectName(u"comboBox_wb_type")
        self.comboBox_wb_type.setMinimumSize(QSize(120, 25))
        self.comboBox_wb_type.setMaximumSize(QSize(300, 16777215))
        font1 = QFont()
        font1.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.comboBox_wb_type.setFont(font1)
        self.comboBox_wb_type.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 9pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.comboBox_wb_type.setEditable(True)
        self.comboBox_wb_type.setIconSize(QSize(16, 16))
        self.comboBox_wb_type.setDuplicatesEnabled(False)
        self.comboBox_wb_type.setModelColumn(0)

        self.horizontalLayout_2.addWidget(self.comboBox_wb_type)

        self.label_29 = QLabel(self.tab)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(40, 0))
        self.label_29.setMaximumSize(QSize(80, 16777215))
        self.label_29.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_29.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_29)

        self.comboBox_operate_user = QComboBox(self.tab)
        self.comboBox_operate_user.setObjectName(u"comboBox_operate_user")
        self.comboBox_operate_user.setMinimumSize(QSize(120, 25))
        self.comboBox_operate_user.setMaximumSize(QSize(300, 16777215))
        self.comboBox_operate_user.setFont(font1)
        self.comboBox_operate_user.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 9pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.comboBox_operate_user.setEditable(True)

        self.horizontalLayout_2.addWidget(self.comboBox_operate_user)

        self.label_30 = QLabel(self.tab)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(30, 0))
        self.label_30.setMaximumSize(QSize(80, 16777215))
        self.label_30.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_30.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_30)

        self.dateEdit_wbdate = QDateEdit(self.tab)
        self.dateEdit_wbdate.setObjectName(u"dateEdit_wbdate")
        self.dateEdit_wbdate.setMinimumSize(QSize(120, 25))
        self.dateEdit_wbdate.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")

        self.horizontalLayout_2.addWidget(self.dateEdit_wbdate)

        self.pushButton_upd_weibao = QPushButton(self.tab)
        self.pushButton_upd_weibao.setObjectName(u"pushButton_upd_weibao")
        self.pushButton_upd_weibao.setFont(font)

        self.horizontalLayout_2.addWidget(self.pushButton_upd_weibao)

        self.pushButton_new_wb = QPushButton(self.tab)
        self.pushButton_new_wb.setObjectName(u"pushButton_new_wb")
        self.pushButton_new_wb.setFont(font)

        self.horizontalLayout_2.addWidget(self.pushButton_new_wb)

        self.pushButton_wb_record_del = QPushButton(self.tab)
        self.pushButton_wb_record_del.setObjectName(u"pushButton_wb_record_del")
        self.pushButton_wb_record_del.setFont(font)

        self.horizontalLayout_2.addWidget(self.pushButton_wb_record_del)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.Te_Wb_Info = QTextEdit(self.tab)
        self.Te_Wb_Info.setObjectName(u"Te_Wb_Info")
        self.Te_Wb_Info.setMaximumSize(QSize(16777215, 300))
        self.Te_Wb_Info.setFont(font)

        self.verticalLayout_2.addWidget(self.Te_Wb_Info)

        self.Te_Solution = QTextEdit(self.tab)
        self.Te_Solution.setObjectName(u"Te_Solution")
        self.Te_Solution.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_2.addWidget(self.Te_Solution)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_9 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.tableView_Ch = QTableView(self.tab_2)
        self.tableView_Ch.setObjectName(u"tableView_Ch")
        self.tableView_Ch.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView_Ch.horizontalHeader().setStretchLastSection(True)

        self.horizontalLayout_9.addWidget(self.tableView_Ch)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.horizontalLayout_7.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        font2 = QFont()
        font2.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font2.setPointSize(11)
        self.statusBar.setFont(font2)
        self.statusBar.setLayoutDirection(Qt.RightToLeft)
        self.statusBar.setStyleSheet(u"color: rgb(255, 0, 0);")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1333, 23))
        self.menu = QMenu(self.menuBar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menuBar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menuBar)
        self.menu_3.setObjectName(u"menu_3")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())
        self.menuBar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u8bbe\u5907\u7ef4\u4fdd\u7cfb\u7edf", None))
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.groupBox_2.setTitle("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u786c\u4ef6\u7f16\u7801", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u4f7f\u7528\u4eba\u5458", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"IP\u5730\u5740", None))
        self.lineEdit_IP_Query.setInputMask("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u5907\u72b6\u6001:", None))
#if QT_CONFIG(tooltip)
        self.Pb_Query.setToolTip(QCoreApplication.translate("MainWindow", u"\u56de\u8f66\u76f4\u63a5\u67e5\u8be2", None))
#endif // QT_CONFIG(tooltip)
        self.Pb_Query.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u627eF5", None))
#if QT_CONFIG(shortcut)
        self.Pb_Query.setShortcut(QCoreApplication.translate("MainWindow", u"F5", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_Trace.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u5907\u8ddf\u8e2a", None))
#if QT_CONFIG(tooltip)
        self.pushButton_analysis.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton_analysis.setText(QCoreApplication.translate("MainWindow", u"\u5206\u6790", None))
        self.pushButton_Ip_Manager.setText(QCoreApplication.translate("MainWindow", u"IP\u7ba1\u7406", None))
#if QT_CONFIG(tooltip)
        self.pushButton_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u589e\u4e3b\u673a", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u7c7b\u578b:", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u4f9b\u5e94\u5546:", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u5185\u5b58:", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"\u64cd\u4f5c\u7cfb\u7edf:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"CPU:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u5907\u72b6\u6001:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u7ea7\u522b:", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u673a\u68b0\u786c\u76d8:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u54c1\u724c:", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u804c\u79f0:", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u4fee\u5e74\u9650:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u8d2d\u4e70\u65e5\u671f:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u56fa\u6001\u786c\u76d8:", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u7ec4\u522b\uff1a", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u4f7f\u7528\u4eba:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u578b\u53f7:", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"IP\u5730\u5740:", None))
        self.lineEdit_Ip.setInputMask("")
        self.lineEdit_model.setInputMask("")
        self.Pb_Update.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u4fee\u6539", None))
#if QT_CONFIG(shortcut)
        self.Pb_Update.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u914d\u7f6e\u660e\u7ec6", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u7c7b\u522b:", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u7ef4\u4fdd\u4eba\u5458:", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u7ef4\u4fdd\u65e5\u671f:", None))
        self.pushButton_upd_weibao.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u4fee\u6539", None))
        self.pushButton_new_wb.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u589e\u7ef4\u4fdd\u8bb0\u5f55", None))
        self.pushButton_wb_record_del.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u7ef4\u4fdd\u8bb0\u5f55", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u7ef4\u4fdd\u8bb0\u5f55", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u53d8\u66f4\u8bb0\u5f55", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u786c\u4ef6\u7ba1\u7406", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u5e93\u5b58\u7ba1\u7406", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u4f9b\u5e94\u5546\u7ba1\u7406", None))
    # retranslateUi

