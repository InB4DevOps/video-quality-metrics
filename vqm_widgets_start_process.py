from PyQt5 import QtCore, QtWidgets

from vqm_widget_base import VqmBaseWidget


class StartProcessWidget(VqmBaseWidget):
    def __init__(self, parent, model):
        super().__init__(parent, model, title='Start VQM analysis')

        self.setObjectName('StartProcessWidget')
        self.horizontal_Layout = QtWidgets.QHBoxLayout(self)
        self.horizontal_Layout.setObjectName('horizontalLayout')
        self.horizontal_Layout.setAlignment(QtCore.Qt.AlignRight)

        self.progress_bar = QtWidgets.QProgressBar(self)
        self.progress_bar.setObjectName('progress_bar')
        self.progress_bar.setTextVisible(True)
        self.progress_bar.setFormat('')
        self.progress_bar.setStyleSheet('text-align: center')
        self.horizontal_Layout.addWidget(self.progress_bar)

        self.pushButton_Start = QtWidgets.QPushButton(self)
        self.pushButton_Start.setObjectName('pushButton_Start')
        self.pushButton_Start.setText('Start')
        self.pushButton_Start.setFixedWidth(80)
        self.horizontal_Layout.addWidget(self.pushButton_Start,
                                         QtCore.Qt.AlignRight)
