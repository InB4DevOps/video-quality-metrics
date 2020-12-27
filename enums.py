from enum import Enum


class VqmMode(Enum):
    crf = 1
    preset = 2


class Encoder(Enum):
    x264 = 1
    x265 = 2
