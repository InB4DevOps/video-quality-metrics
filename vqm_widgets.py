from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QGroupBox

from utils import VideoInfoProvider
from enums import VqmMode


class VqmBaseWidget(QGroupBox):
    def __init__(self, parent, model, **kwargs):
        super().__init__(parent, **kwargs)
        self.model = model


class InputFileWidget(VqmBaseWidget):

    video_selected = pyqtSignal()
    status_bar_text = pyqtSignal(str)

    def __init__(self, parent, model):
        super().__init__(parent, model, title='Select an input video file')

        self.setObjectName('InputFileWidget')

        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName('horizontalLayout')

        self.labelselectfile = QtWidgets.QLabel(self)
        self.labelselectfile.setObjectName('labelselectfile')
        self.horizontalLayout.addWidget(self.labelselectfile)

        self.lineEditSelectFile = QtWidgets.QLineEdit(self)
        self.lineEditSelectFile.setObjectName('lineEditSelectFile')
        self.horizontalLayout.addWidget(self.lineEditSelectFile)

        self.pushButtonBrowse = QtWidgets.QPushButton(self)
        self.pushButtonBrowse.setObjectName('pushButtonBrowse')
        self.horizontalLayout.addWidget(self.pushButtonBrowse)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.pushButtonBrowse.clicked.connect(self.browseFile)

    def browseFile(self):
        video_file, _ = QtWidgets.QFileDialog.getOpenFileName(
                        None,
                        'Select a video file',
                        '',
                        'All video files (*)')

        if video_file != '':
            vip = VideoInfoProvider(video_file)
            if vip.is_file_a_video_file():
                self.lineEditSelectFile.setText(video_file)
                self.video_selected.emit()
                self.status_bar_text.emit(vip.get_statusbar_text())
            else:
                QtWidgets.QMessageBox.warning(self.pushButtonBrowse,
                                              'Invalid video file',
                                              'The selected file is not a '
                                              'video file.')

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.labelselectfile.setText(_translate('InputFileWidget',
                                                'Select a video file'))
        self.pushButtonBrowse.setText(_translate('InputFileWidget', 'Browse'))


class OverviewWidget(VqmBaseWidget):
    def __init__(self, parent, model):
        super().__init__(parent, model,
                         title='Enable overview mode (optional)')

        self.setObjectName('OverviewWidget')
        self.setCheckable(True)
        self.setChecked(False)

        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName('verticalLayout')

        self.clicked.connect(self.toggle_options)

        self.overview_options = QtWidgets.QWidget(self)
        self.overview_options.setObjectName('overview_options')
        self.overview_options.setEnabled(False)

        self.grid_layout = QtWidgets.QGridLayout(self.overview_options)
        self.grid_layout.setObjectName('grid_layout')

        self.labelInterval = QtWidgets.QLabel('Interval (seconds)')
        self.labelInterval.setObjectName('labelInterval')
        self.grid_layout.addWidget(self.labelInterval, 0, 0, 1, 1)

        self.lineEditInterval = QtWidgets.QLineEdit(self.overview_options)
        self.lineEditInterval.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEditInterval.setPlaceholderText('60')
        self.lineEditInterval.setObjectName('lineEditInterval')
        self.grid_layout.addWidget(self.lineEditInterval, 0, 1, 1, 1)

        self.labelClipLength = QtWidgets.QLabel('Clip Length (seconds)')
        self.labelClipLength.setObjectName('labelClipLength')
        self.grid_layout.addWidget(self.labelClipLength, 0, 2, 1, 1)

        self.lineEditClipLength = QtWidgets.QLineEdit(self.overview_options)
        self.lineEditClipLength.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEditClipLength.setPlaceholderText('2')
        self.lineEditClipLength.setObjectName('lineEditClipLength')
        self.grid_layout.addWidget(self.lineEditClipLength, 0, 3, 1, 1)

        self.verticalLayout.addWidget(self.overview_options)

    def toggle_options(self):
        self.overview_options.setEnabled(self.isChecked())


class ComparisonModeWidget(VqmBaseWidget):
    def __init__(self, parent, model):
        super().__init__(parent, model, title='Select a comparison mode')

        self.setObjectName('ComparisonModeWidget')

        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName('horizontalLayout')

        # create groupbox for CRF mode
        self.crf_mode_groupbox = QtWidgets.QGroupBox('CRF comparison')
        self.crf_mode_groupbox.setCheckable(True)

        # create vertical layout for CRF mode
        self.crf_vbox = QtWidgets.QVBoxLayout()
        self.crf_mode_groupbox.setLayout(self.crf_vbox)

        self.select_crfs_label = QtWidgets.QLabel('Select CRFs for comparison')
        self.crf_vbox.addWidget(self.select_crfs_label)

        self.crf_listview = QtWidgets.QListView(self)
        self.crf_listview.setModel(model.crf_mode.crf_listview_model)

        self.crf_vbox.addWidget(self.crf_listview)

        self.preset_combobox = QtWidgets.QComboBox()
        self.preset_combobox.setModel(model.crf_mode.preset_combobox_model)

        self.select_preset_label = QtWidgets.QLabel('Select a preset')
        self.crf_vbox.addWidget(self.select_preset_label)
        self.crf_vbox.addWidget(self.preset_combobox)

        # create groupbox for preset mode
        self.preset_mode_groupbox = QtWidgets.QGroupBox('Preset comparison')
        self.preset_mode_groupbox.setCheckable(True)
        self.preset_mode_groupbox.setChecked(False)

        # create vertical layout for preset mode
        self.preset_vbox = QtWidgets.QVBoxLayout()
        self.preset_mode_groupbox.setLayout(self.preset_vbox)
        # create label
        self.select_presets_label = QtWidgets.QLabel('Select presets for '
                                                     'comparison')
        self.preset_vbox.addWidget(self.select_presets_label)

        # create preset selection listview
        self.preset_listview = QtWidgets.QListView(self)
        self.preset_listview.setModel(model.preset_mode.preset_listview_model)
        self.preset_combobox.setCurrentIndex(5)     # preset medium

        self.preset_vbox.addWidget(self.preset_listview)

        # create label
        self.select_CRF_label = QtWidgets.QLabel('Select a CRF value')
        self.preset_vbox.addWidget(self.select_CRF_label)

        # create CRF combobox
        self.crf_combobox = QtWidgets.QComboBox()
        self.crf_combobox.setModel(model.preset_mode.crf_combobox_model)
        self.crf_combobox.setCurrentIndex(18)   # crf 18 default

        self.preset_vbox.addWidget(self.crf_combobox)

        # add group boxes to horizontal layout
        self.setLayout(self.horizontalLayout)
        self.horizontalLayout.addWidget(self.crf_mode_groupbox)
        self.horizontalLayout.addWidget(self.preset_mode_groupbox)

        # connect signals to slots
        self.preset_mode_groupbox.clicked.connect(self.preset_groupbox_clicked)
        self.crf_mode_groupbox.clicked.connect(self.crf_groupbox_clicked)

    def crf_groupbox_clicked(self, checked):
        self.preset_mode_groupbox.setChecked(not checked)
        self.model.vqm_mode = VqmMode.crf

    def preset_groupbox_clicked(self, checked):
        self.crf_mode_groupbox.setChecked(not checked)
        self.model.vqm_mode = VqmMode.preset
