import time
import math
import sys
from pathlib import Path

from ffmpeg import probe


def get_pretty_codec_name(codec):
    dict = {
                'h264': 'H.264 (AVC)',
                'hevc': 'H.265 (HEVC)'
            }

    return dict.get(codec, codec)


def line():
    print('-------------------------------------------------------------------\
          ----------------------------------------')


def subprocess_printer(message, arguments_list):
    line()
    print(f'[DEBUG] {message}:\n{" ".join(arguments_list)}')
    line()


def is_list(argument_object):
    return isinstance(argument_object, list)


def force_decimal_places(value, decimal_places):
    return '{:0.{dp}f}'.format(value, dp=decimal_places)


def exit_program(message):
    line()
    print(f'[Exiting Program] {message}')
    line()
    sys.exit()


class VideoInfoProvider:
    def __init__(self, video_path):
        self._video_path = video_path

    def get_bitrate(self, video_path=None, unit='Kbps'):
        if video_path:
            bitrate = probe(video_path)['format']['bit_rate'] 
        else:
            bitrate = probe(self._video_path)['format']['bit_rate']
        if unit == 'Kbps':
            return f'{math.trunc(int(bitrate) / 1000)} Kbps'
        elif unit == 'Mbps':
            return f'{round(int(bitrate) / 1000000, 2)} Mbps'

    def get_duration(self):
        return probe(self._video_path)['format']['duration']

    def get_encoder(self):
        encoder = [stream for stream in probe(self._video_path)['streams']
                   if stream['codec_type'] == 'video'][0]['codec_name']

        return get_pretty_codec_name(encoder)

    def get_framerate_fraction(self):
        r_frame_rate = [stream for stream in probe(self._video_path)['streams']
                        if stream['codec_type'] == 'video'][0]['r_frame_rate']
        return r_frame_rate

    def get_framerate_float(self):
        numerator, denominator = self.get_framerate_fraction().split('/')
        return round((int(numerator) / int(denominator)), 3)

    def get_pretty_duration(self):
        duration = round(float(self.get_duration()))
        return time.strftime('%H:%M:%S', time.gmtime(duration))

    def get_resolution(self):
        width = [stream for stream in probe(self._video_path)['streams']
                 if stream['codec_type'] == 'video'][0]['width']
        height = [stream for stream in probe(self._video_path)['streams']
                  if stream['codec_type'] == 'video'][0]['height']

        return f'{width}x{height}'

    def get_statusbar_text(self):
        bitrate = self.get_bitrate(unit='Mbps')
        return f'Video File: {Path(self._video_path).name} | ' + \
               f'{self.get_encoder()} | ' + \
               f'{self.get_resolution()} | ' + \
               f'{self.get_pretty_duration()} | ' + \
               f'{bitrate}'

    def is_file_a_video_file(self):
        try:
            _ = self.get_duration()
            return True
        except Exception:
            return False

    @property
    def file_name(self):
        return Path(self._video_path).name


class Timer:
    def start(self):
        self.__start_time = time()

    def end(self, decimal_places):
        time_to_convert = time() - self.__start_time
        time_rounded = force_decimal_places(round(time_to_convert,
                                                  decimal_places),
                                            decimal_places)
        return time_rounded
