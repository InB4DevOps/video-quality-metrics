from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtWidgets import QMessageBox, QFrame
import sys

from utils import VideoInfoProvider
from vqm_window import Ui_MainWindow
# from vqm_overview_frame import Ui_FrameOverviewMode
from vqm_frames import InputFileFrame, OverviewFrame


class VqmGui(Ui_MainWindow):
    def __init__(self):
        '''Initialize the super class
        '''
        super().__init__()


    def setupUi(self, MW):
        ''' Setup the UI of the super class, and add here code
        that relates to the way we want our UI to operate.
        '''
        super().setupUi(MW)

        self.input_frame = InputFileFrame(self.centralwidget)
        self.input_frame.setupUi()
        self.input_frame.pushButtonBrowse.clicked.connect(self.browseFile)
        self.verticalLayout.addWidget(self.input_frame)

        self.overview_frame = OverviewFrame(self.centralwidget)
        self.overview_frame.setupUi()
        self.verticalLayout.addWidget(self.overview_frame)

        self.verticalLayout.addStretch()

    def browseFile(self):
        video_file, _ = QtWidgets.QFileDialog.getOpenFileName(
                        None,
                        "Select a video file",
                        "",
                        "All video files (*)")
        if video_file != '':
            vip = VideoInfoProvider(video_file)
            if vip.is_file_a_video_file():
                self.input_frame.lineEditSelectFile.setText(video_file)
                self.input_frame.setEnabled(False)
                self.update_statusbar(vip)
            else:
                QMessageBox.warning(self.pushButtonBrowse, "Invalid video file",
                                    "The selected file is not a video file.")

    def update_statusbar(self, vip):
        self.statusbar.showMessage(vip.get_statusbar_text())


def main():
    """
    This is the MAIN ENTRY POINT of our application.  The code at the end
    of the mainwindow.py script will not be executed, since this script is now
    our main program.   We have simply copied the code from mainwindow.py here
    since it was automatically generated by '''pyuic5'''.

    """
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = VqmGui()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


main()