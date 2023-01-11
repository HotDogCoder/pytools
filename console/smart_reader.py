import sys
from app.domain.models.log_reader import LogReader
from app.presentation.controllers import LogReaderController

LRC = LogReaderController()

parameters = sys.argv

timezone = 'America/Bogota'
local_path = 'C:\inetpub\logs\LogFiles'
date_string = ''
read_all = False


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    if len(lst3) > 0:
        return lst3[0]
    else:
        return False


flag_val = intersection(('--read-all', '-ra'), parameters)
if flag_val:
    read_all = True

flag_val = intersection(('--date', '-d'), parameters)
if flag_val:
    date_index = parameters.index(flag_val)
    date_string = parameters[date_index + 1]

flag_val = intersection(('--timezone', '-tz'), parameters)
if flag_val:
    timezone_index = parameters.index(flag_val)
    timezone = parameters[timezone_index + 1]

flag_val = intersection(('--path', '-p'), parameters)
if flag_val:
    local_path_index = parameters.index(flag_val)
    local_path = parameters[local_path_index + 1]

LR = LogReader(
    counter=0,
    get_counter=0,
    post_counter=0,
    local_path=local_path,
    date_string=date_string,
    limit=1000000000,
    timezone=timezone,
    read_all=read_all
)

LRF = LRC.read_log_file_directories(LR)

# print('message: ', LRF.message)

print('TOTAL GET Y POST: ', LRF.counter)
print('TOTAL GET: ', LRF.get_counter)
print('TOTAL POST: ', LRF.post_counter)
print('---------------------------------')
print('---------------------------------')

# print('total|gets|post')
# sys.exit(f"{LRF.counter}|{LRF.get_counter}|{LRF.post_counter}")