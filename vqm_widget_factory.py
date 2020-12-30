from enums import WidgetType
from vqm_widget_combined_encoder_overview import CombinedWidget
from vqm_widget_comparison import ComparisonModeWidget
from vqm_widget_encoder import EncoderWidget
from vqm_widget_inputfile import InputFileWidget
from vqm_widget_overview import OverviewWidget
from vqm_widgets_start_process import StartProcessWidget


class WidgetFactory:
    def __init__(self, central_widget, model):
        super().__init__()
        self.central_widget = central_widget
        self.model = model

        self.widgets = {
            WidgetType.input: InputFileWidget,
            WidgetType.overview: OverviewWidget,
            WidgetType.comparison: ComparisonModeWidget,
            WidgetType.start_process: StartProcessWidget,
            WidgetType.encoder: EncoderWidget,
            WidgetType.combined: CombinedWidget  # encoder & overview
        }

    def create(self, widget_type):
        widget_func = self.widgets.get(widget_type)

        return widget_func(self.central_widget, self.model)
