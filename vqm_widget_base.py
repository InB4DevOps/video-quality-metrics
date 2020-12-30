from PyQt5.QtWidgets import QGroupBox


class VqmBaseWidget(QGroupBox):
    def __init__(self, parent, model, **kwargs):
        super().__init__(parent, **kwargs)
        self.model = model
