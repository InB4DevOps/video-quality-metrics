from PyQt5 import QtCore, QtWidgets

from vqm_widget_base import VqmBaseWidget


class OverviewWidget(VqmBaseWidget):
    def __init__(self, parent, model):
        super().__init__(parent, model,
                         title='Enable Overview Mode (optional)')

        self.setObjectName('OverviewWidget')
        self.setCheckable(True)
        self.clicked.connect(self.toggle_options)
        self.setChecked(self.model.overview_mode.enabled)

        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName('verticalLayout')

        self.overview_options = QtWidgets.QWidget(self)
        self.overview_options.setObjectName('overview_options')

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
