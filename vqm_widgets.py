from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QGroupBox

from utils import VideoInfoProvider
from vqm_consts import PRESETS


class VqmBaseWidget(QGroupBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class InputFileWidget(VqmBaseWidget):

    video_selected = pyqtSignal()
    status_bar_text = pyqtSignal(str)

    def __init__(self, parent):
        super().__init__(parent, title='Select an input video file')

        self.setObjectName("InputFileWidget")

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

        self.pushButtonBrowse.clicked.connect(self.browseFile)

    def browseFile(self):
        video_file, _ = QtWidgets.QFileDialog.getOpenFileName(
                        None,
                        "Select a video file",
                        "",
                        "All video files (*)")

        if video_file != '':
            vip = VideoInfoProvider(video_file)
            if vip.is_file_a_video_file():
                self.lineEditSelectFile.setText(video_file)
                # self.input_Widget.setEnabled(False)
                # self.overview_Widget.setEnabled(True)
                self.video_selected.emit()
                self.status_bar_text.emit(vip.get_statusbar_text())
            else:
                QMessageBox.warning(self.pushButtonBrowse, "Invalid video file",
                                    "The selected file is not a video file.")

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.labelselectfile.setText(_translate("InputFileWidget",
                                                "Select a video file"))
        self.pushButtonBrowse.setText(_translate("InputFileWidget", "Browse"))


class OverviewWidget(VqmBaseWidget):
    def __init__(self, parent):
        super().__init__(parent, title='Enable overview mode (optional)')

        self.setObjectName("OverviewWidget")
        self.setCheckable(True)
        self.setChecked(False)

        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName('verticalLayout')

        self.clicked.connect(self.toggle_options)

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
        self.overview_options.setEnabled(self.isChecked())

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.labelInterval.setText(_translate("OverviewWidget", "Interval (seconds)"))
        self.lineEditInterval.setPlaceholderText(_translate("OverviewWidget", "60"))
        self.labelClipLength.setText(_translate("OverviewWidget", "Clip Length (seconds)"))
        self.lineEditClipLength.setPlaceholderText(_translate("OverviewWidget", "2"))


class ComparisonModeWidget(VqmBaseWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.setObjectName("ComparisonModeWidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName('horizontalLayout')

        self.crf_mode_groupbox = QtWidgets.QGroupBox('CRF comparison mode')
        self.crf_mode_groupbox.setCheckable(True)
        self.crf_vbox = QtWidgets.QVBoxLayout()
        self.crf_mode_groupbox.setLayout(self.crf_vbox)

        self.select_crfs_label = QtWidgets.QLabel('Select CRFs for comparison')
        self.crf_vbox.addWidget(self.select_crfs_label)

        crf_checkbox_model = QStandardItemModel()
        for crf in range(0, 52):
            item = QStandardItem(f'CRF {crf}')
            item.setCheckState(QtCore.Qt.Unchecked)
            item.setCheckable(True)
            item.setData(crf)
            crf_checkbox_model.appendRow(item)

        self.crf_listview = QtWidgets.QListView(self)
        self.crf_listview.setModel(crf_checkbox_model)

        self.crf_vbox.addWidget(self.crf_listview)

        # create preset combobox
        self.preset_combobox_model = QStandardItemModel()

        for preset in PRESETS:
            item = QStandardItem(preset)
            item.setData(preset)
            self.preset_combobox_model.appendRow(item)

        self.preset_combobox = QtWidgets.QComboBox()
        self.preset_combobox.setModel(self.preset_combobox_model)

        self.select_preset_label = QtWidgets.QLabel('Select a preset')
        self.crf_vbox.addWidget(self.select_preset_label)
        self.crf_vbox.addWidget(self.preset_combobox)

        # create groupbox for preset mode
        self.preset_mode_groupbox = QtWidgets.QGroupBox('Preset comparison mode')
        self.preset_mode_groupbox.setCheckable(True)
        self.preset_mode_groupbox.setChecked(False)

        # create vertical layout for preset mode
        self.preset_vbox = QtWidgets.QVBoxLayout()
        self.preset_mode_groupbox.setLayout(self.preset_vbox)
        # create label
        self.select_presets_label = QtWidgets.QLabel('Select presets for comparison')
        self.preset_vbox.addWidget(self.select_presets_label)

        # create preset selection listview
        preset_listview_model = QStandardItemModel()

        for preset in PRESETS:
            item = QStandardItem(preset)
            item.setData(preset)
            item.setCheckState(QtCore.Qt.Unchecked)
            item.setCheckable(True)
            preset_listview_model.appendRow(item)

        self.preset_listview = QtWidgets.QListView(self)
        self.preset_listview.setModel(preset_listview_model)
        self.preset_combobox.setCurrentIndex(5)     # preset medium

        self.preset_vbox.addWidget(self.preset_listview)

        # create label
        self.select_CRF_label = QtWidgets.QLabel('Select a CRF')
        self.preset_vbox.addWidget(self.select_CRF_label)

        # create CRF combobox
        crf_combobox_model = QStandardItemModel()

        for crf in range(0, 52):
            item = QStandardItem(f'CRF {crf}')
            item.setData(crf)
            crf_combobox_model.appendRow(item)

        self.crf_combobox = QtWidgets.QComboBox()
        self.crf_combobox.setModel(crf_combobox_model)
        self.crf_combobox.setCurrentIndex(18)   # crf 18 default
        
        self.preset_vbox.addWidget(self.crf_combobox)

        # add group boxes to horizontal layout
        self.setLayout(self.horizontalLayout)
        self.horizontalLayout.addWidget(self.crf_mode_groupbox)
        self.horizontalLayout.addWidget(self.preset_mode_groupbox)

        # connect signals to slots
        self.preset_mode_groupbox.clicked.connect(self.preset_groupbox_clicked)
        self.crf_mode_groupbox.clicked.connect(self.crf_groupbox_clicked)

    # def paintEvent(self, event):
    #     self.crf_listview.setMaximumWidth(self.crf_mode_groupbox.width() / 2)
    #     self.preset_combobox.setMaximumWidth(self.crf_mode_groupbox.width() / 2)

    def crf_groupbox_clicked(self, checked):
        self.preset_mode_groupbox.setChecked(not checked)

    def preset_groupbox_clicked(self, checked):
        self.crf_mode_groupbox.setChecked(not checked)
