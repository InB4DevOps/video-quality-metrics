from enum import Enum


class VqmMode(Enum):
    crf = 1
    preset = 2


class Encoder(Enum):
    x264 = 1
    x265 = 2


class WidgetType(Enum):
    input = 1
    overview = 2
    comparison = 3
    start_process = 4
