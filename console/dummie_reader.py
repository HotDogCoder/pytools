import os
from datetime import datetime

import cpuinfo
import pytz
import wmi
import platform
import psutil

print(f'Architecture: {platform.architecture()}')
print(f'Network Name: {platform.node()}')
print(f'platform: {platform.platform()}')
print(f'processor: {platform.processor()}')

my_cpuinfo = cpuinfo.get_cpu_info()

print(f"Full CPU Name: {my_cpuinfo['brand_raw']}")
print(f"Full CPU Name: {my_cpuinfo['hz_actual_friendly']}")
print(f"Full CPU Name: {my_cpuinfo['hz_advertised_friendly']}")

print(f"virtual memory: {psutil.virtual_memory().total / 1024 / 1024 / 1024}")

pc = wmi.WMI()

print(pc.Win32_Processor()[0].name)
print(pc.Win32_VideoController()[0].name)
print((pc.MSAcpi_ThermalZoneTemperature()[0].CurrentTemperature / 10.0)-273.15)

# w_temp = wmi.WMI(namespace="root\\wmi")
# print(w_temp)
# print((w_temp.MSAcpi_ThermalZoneTemperature()[0].CurrentTemperature / 10.0)-273.15)
class DummieReader():

    def __init__(self, counter, get_counter, post_counter, date_string):
        self.counter = counter
        self.get_counter = get_counter
        self.post_counter = post_counter
        self.local_path = 'C:/Users/jhospinal/Documents/LogFiles'
        self.daily_directory_list = os.listdir(f'{self.local_path}')
        self.message = 'success'
        self.last_file_readed = 'no one'
        self.date_string = date_string

    # print(daily_directory_list)

    def read_directories(self):
        try:

            for daily_directory in self.daily_directory_list:
                daily_directory_file_list = os.listdir(f'{self.local_path}/{daily_directory}')
                # print(daily_directory_file_list)
                for daily_directory_file in daily_directory_file_list:
                    self.last_file_readed = f'{self.local_path}/{daily_directory}/{daily_directory_file}'
                    print('reading', self.last_file_readed)

                    file = open(
                        f'{self.local_path}/{daily_directory}/{daily_directory_file}',
                        mode='r',
                        encoding='utf8',
                        errors='ignore'
                    )

                    for line in file:
                        self.counter = self.counter + 1

                        line_split = line.split(' ')

                        if 'GET' in line_split:
                            self.get_counter = self.get_counter + 1

                        if 'POST' in line_split:
                            self.post_counter = self.post_counter + 1

                        if self.counter == 100000000:
                            self.message = 'Too much'
                            return

        except UnicodeDecodeError as e:

            print('error on: ', self.last_file_readed)
            print('line: ', self.counter + 1)
            print('error: ', e)


tz = pytz.timezone('America/Bogota')
directory_name = datetime.now(tz).strftime('%Y%m%d')
# dummie_reader = DummieReader(0, 0, 0)
# dummie_reader.read_directories()

# print('message: ', dummie_reader.message)
# print('counter: ', dummie_reader.counter)
# print('get_counter: ', dummie_reader.get_counter)
# print('post_counter: ', dummie_reader.post_counter)

