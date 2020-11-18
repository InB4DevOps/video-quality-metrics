from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFrame


class VqmBaseFrame(QFrame):
    def setupUi(self):
        self.setFrameStyle(QFrame.StyledPanel)
        self.setLineWidth(1)


class InputFileFrame(VqmBaseFrame):
    def setupUi(self):
        super().setupUi()

        self.setObjectName("InputFileFrame")
        self.resize(492, 83)

        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.labelselectfile = QtWidgets.QLabel(self)
        self.labelselectfile.setObjectName("labelselectfile")
        self.horizontalLayout.addWidget(self.labelselectfile)

        self.lineEditSelectFile = QtWidgets.QLineEdit(self)
        self.lineEditSelectFile.setObjectName("lineEditSelectFile")
        self.horizontalLayout.addWidget(self.lineEditSelectFile)

        self.pushButtonBrowse = QtWidgets.QPushButton(self)
        self.pushButtonBrowse.setObjectName("pushButtonBrowse")
        self.horizontalLayout.addWidget(self.pushButtonBrowse)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.labelselectfile.setText(_translate("InputFileFrame",
                                                "Select a video file"))
        self.pushButtonBrowse.setText(_translate("InputFileFrame", "Browse"))


class OverviewFrame(VqmBaseFrame):
    def setupUi(self):
        super().setupUi()

        self.setObjectName("OverviewFrame")

        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName('verticalLayout')

        self.checkBoxEnableOverviewMode = QtWidgets.QCheckBox(self)
        self.checkBoxEnableOverviewMode.setObjectName("checkBoxEnableOverviewMode")
        self.verticalLayout.addWidget(self.checkBoxEnableOverviewMode)

        self.checkBoxEnableOverviewMode.clicked.connect(self.toggle_options)

        self.overview_options = QtWidgets.QWidget(self)
        self.overview_options.setObjectName("overview_options")
        self.overview_options.setEnabled(False)

        self.grid_layout = QtWidgets.QGridLayout(self.overview_options)
        self.grid_layout.setObjectName("grid_layout")

        self.labelInterval = QtWidgets.QLabel(self.overview_options)
        self.labelInterval.setObjectName("labelInterval")
        self.grid_layout.addWidget(self.labelInterval, 0, 0, 1, 1)

        self.lineEditInterval = QtWidgets.QLineEdit(self.overview_options)
        self.lineEditInterval.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEditInterval.setObjectName("lineEditInterval")
        self.grid_layout.addWidget(self.lineEditInterval, 0, 1, 1, 1)

        self.labelClipLength = QtWidgets.QLabel(self.overview_options)
        self.labelClipLength.setObjectName("labelClipLength")
        self.grid_layout.addWidget(self.labelClipLength, 0, 2, 1, 1)

        self.lineEditClipLength = QtWidgets.QLineEdit(self.overview_options)
        self.lineEditClipLength.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEditClipLength.setObjectName("lineEditClipLength")
        self.grid_layout.addWidget(self.lineEditClipLength, 0, 3, 1, 1)

        self.verticalLayout.addWidget(self.overview_options)
        self.retranslateUi()

    def toggle_options(self):
        self.overview_options.setEnabled(not self.overview_options.isEnabled())

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.checkBoxEnableOverviewMode.setText(_translate("OverviewFrame", "Enable overview mode (optional)"))
        self.labelInterval.setText(_translate("OverviewFrame", "Interval (seconds)"))
        self.lineEditInterval.setPlaceholderText(_translate("OverviewFrame", "60"))
        self.labelClipLength.setText(_translate("OverviewFrame", "Clip Length (seconds)"))
        self.lineEditClipLength.setPlaceholderText(_translate("OverviewFrame", "2"))



