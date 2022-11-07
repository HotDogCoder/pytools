from datetime import datetime

import pytz

from app.domain.models.log_reader import LogReader
from app.presentation.controllers.log_reader_controller import LogReaderController

LRC = LogReaderController()

LR = LogReader(
    counter=0,
    get_counter=0,
    post_counter=0,
    local_path="C:/Users/jhospinal/Documents/LogFiles",
    date_string='2022-11-07'
)
LRF = LRC.read_log_file_directories(LR)

print('message: ', LRF.message)
print('counter: ', LRF.counter)
print('get_counter: ', LRF.get_counter)
print('post_counter: ', LRF.post_counter)
