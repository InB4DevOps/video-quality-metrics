from enums import VqmMode
from PyQt5 import QtWidgets
from vqm_widget_base import VqmBaseWidget


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

        self.preset_mode_groupbox.setChecked(self.model.vqm_mode ==
                                             VqmMode.preset)
        self.crf_mode_groupbox.setChecked(self.model.vqm_mode == VqmMode.crf)

    def crf_groupbox_clicked(self, checked):
        self.preset_mode_groupbox.setChecked(not checked)
        self.model.vqm_mode = VqmMode.crf

    def preset_groupbox_clicked(self, checked):
        self.crf_mode_groupbox.setChecked(not checked)
        self.model.vqm_mode = VqmMode.preset
