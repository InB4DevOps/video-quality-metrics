from utils import VideoInfoProvider
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
from vqm_widget_base import VqmBaseWidget


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
        self.lineEditSelectFile.setReadOnly(True)
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
