from vqm_widget_encoder import EncoderWidget
from vqm_widget_overview import OverviewWidget
from PyQt5 import QtWidgets
from vqm_widget_base import VqmBaseWidget


class CombinedWidget(VqmBaseWidget):
    def __init__(self, parent, model):
        super().__init__(parent, model)

        self.setObjectName('CombinedEncoderAndOverviewWidget')

        self.encoder_widget = EncoderWidget(parent, model)
        self.overview_widget = OverviewWidget(parent, model)

        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName('horizontalLayout')

        self.horizontalLayout.addWidget(self.encoder_widget)
        self.horizontalLayout.addWidget(self.overview_widget)
