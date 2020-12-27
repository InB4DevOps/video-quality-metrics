from enums import WidgetType
from vqm_widgets import ComparisonModeWidget, InputFileWidget, OverviewWidget


class WidgetFactory:
    def __init__(self, central_widget, model):
        super().__init__()
        self.central_widget = central_widget
        self.model = model

        self.widgets = {
            WidgetType.input: InputFileWidget,
            WidgetType.overview: OverviewWidget,
            WidgetType.comparison: ComparisonModeWidget
        }

    def create_widget(self, widget_type):
        widget_func = self.widgets.get(widget_type)

        return widget_func(self.central_widget, self.model)
