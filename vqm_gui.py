from PyQt5 import QtWidgets
import sys

from enums import WidgetType
from vqm_model import VqmModel
from vqm_widget_factory import WidgetFactory
from vqm_window import Ui_MainWindow


class VqmGui(Ui_MainWindow):
    def __init__(self):
        '''Initialize the super class
        '''
        super().__init__()

    def setupUi(self, MainWindow):
        ''' Setup the UI of the super class
        '''
        super().setupUi(MainWindow)

        # create model
        self.model = VqmModel()

        # create widget factory
        wf = WidgetFactory(self.centralwidget, self.model)

        self.input_Widget = wf.create(WidgetType.input)
        self.verticalLayout.addWidget(self.input_Widget)

        self.overview_Widget = wf.create(WidgetType.overview)
        self.verticalLayout.addWidget(self.overview_Widget)
        self.overview_Widget.setEnabled(False)

        self.comparison_mode_Widget = wf.create(WidgetType.comparison)
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
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = VqmGui()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


main()
