from PyQt5 import QtWidgets

from vqm_widget_base import VqmBaseWidget


class EncoderWidget(VqmBaseWidget):
    def __init__(self, parent, model):
        super().__init__(parent, model, title='Select a Video Encoder')

        self.setObjectName('EncoderWidget')

        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName('verticalLayout')

        # create encoder combobox
        self.encoder_combobox = QtWidgets.QComboBox()
        self.encoder_combobox.setModel(model.encoder)
        self.encoder_combobox.setCurrentIndex(0)

        self.verticalLayout.addWidget(self.encoder_combobox)
