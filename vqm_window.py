# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Gregor\Documents\GitHub\video-quality-metrics\vqm__window.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFrame


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(838, 490)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        # self.frame = QtWidgets.QFrame(self.centralwidget)
        # self.frame.setMaximumSize(QtCore.QSize(16777215, 80))
        # self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame.setObjectName("frame")
        # self.frame.setFrameStyle(QFrame.Box)
        # self.frame.setLineWidth(1)
        # self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        # self.verticalLayout_2.setObjectName("verticalLayout_2")
        # self.horizontalLayout = QtWidgets.QHBoxLayout()
        # self.horizontalLayout.setObjectName("horizontalLayout")
        # self.labelselectfile = QtWidgets.QLabel(self.frame)
        # self.labelselectfile.setObjectName("labelselectfile")
        # self.horizontalLayout.addWidget(self.labelselectfile)
        # self.lineEditSelectFile = QtWidgets.QLineEdit(self.frame)
        # self.lineEditSelectFile.setObjectName("lineEditSelectFile")
        # self.horizontalLayout.addWidget(self.lineEditSelectFile)
        # self.pushButtonBrowse = QtWidgets.QPushButton(self.frame)
        # self.pushButtonBrowse.setObjectName("pushButtonBrowse")
        # self.horizontalLayout.addWidget(self.pushButtonBrowse)
        # self.verticalLayout_2.addLayout(self.horizontalLayout)
        # self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Video Quality Metrics"))
        # self.labelselectfile.setText(_translate("MainWindow", "Select a video file"))
        # self.pushButtonBrowse.setText(_translate("MainWindow", "Browse"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())