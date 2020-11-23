from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtCore import QObject, pyqtSlot
# from PyQt5.QtWidgets import QMessageBox, QWidget
import sys

from vqm_window import Ui_MainWindow
# from vqm_overview_Widget import Ui_WidgetOverviewMode

from vqm_widgets import ComparisonModeWidget, InputFileWidget, OverviewWidget


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

        self.input_Widget = InputFileWidget(self.centralwidget)
        # self.input_Widget
        self.verticalLayout.addWidget(self.input_Widget)

        self.overview_Widget = OverviewWidget(self.centralwidget)
        self.verticalLayout.addWidget(self.overview_Widget)
        self.overview_Widget.setEnabled(False)

        self.comparison_mode_Widget = ComparisonModeWidget(self.centralwidget)
        self.verticalLayout.addWidget(self.comparison_mode_Widget)
        self.comparison_mode_Widget.setEnabled(False)

        self.verticalLayout.addStretch()
        self.input_Widget.video_selected.connect(self.enable_widgets)
        self.input_Widget.status_bar_text.connect(self.update_statusbar)

    def enable_widgets(self):
        self.overview_Widget.setEnabled(True)
        self.comparison_mode_Widget.setEnabled(True)

    def update_statusbar(self, text):
        self.statusbar.showMessage(text)


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