from PyQt5 import QtCore
from PyQt5.QtGui import QStandardItem, QStandardItemModel

from enums import Encoder, VqmMode
from vqm_consts import PRESETS


class VqmModel:
    def __init__(self):
        self.video_path = str()
        self.overview_mode = OverviewMode()
        self.crf_mode = CrfMode()
        self.preset_mode = PresetMode()
        self.vqm_mode = VqmMode.crf
        self.encoder = EncoderModel()


class EncoderModel(QStandardItemModel):
    def __init__(self):
        super().__init__()

        for enc in Encoder:
            item = QStandardItem(enc.name)
            item.setData(enc)
            self.appendRow(item)


class CrfMode:
    def __init__(self):
        self.crf_listview_model = QStandardItemModel()
        for crf in range(0, 52):
            item = QStandardItem(f'CRF {crf}')
            item.setCheckState(QtCore.Qt.Unchecked)
            item.setCheckable(True)
            item.setData(crf)
            self.crf_listview_model.appendRow(item)

        self.preset_combobox_model = QStandardItemModel()

        for preset in PRESETS:
            item = QStandardItem(preset)
            item.setData(preset)
            self.preset_combobox_model.appendRow(item)


class OverviewMode:
    def __init__(self):
        self.enabled = False
        self.interval = int()
        self.clip_length = int()


class PresetMode:
    def __init__(self):
        self.preset_listview_model = QStandardItemModel()

        for preset in PRESETS:
            item = QStandardItem(preset)
            item.setData(preset)
            item.setCheckState(QtCore.Qt.Unchecked)
            item.setCheckable(True)
            self.preset_listview_model.appendRow(item)

        self.crf_combobox_model = QStandardItemModel()

        for crf in range(0, 52):
            item = QStandardItem(f'CRF {crf}')
            item.setData(crf)
            self.crf_combobox_model.appendRow(item)
