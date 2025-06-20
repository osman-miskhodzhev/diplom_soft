import os
import time
import pyautogui
from datetime import datetime
from functools import wraps

def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Засекаем время
        result = func(*args, **kwargs)
        end_time = time.time()    # Засекаем после выполнения
        duration = end_time - start_time
        print(f"Функция '{func.__name__}' выполнена за {duration:.4f} секунд(ы)")
        return result
    return wrapper

class RouterInterfase:
    def __init__(self, name, ip_addr, path, ch_list, ch_select, ch_save, pause=5):
        self.name = name
        self.ip_addr = ip_addr
        self.ch_list = ch_list 
        self.ch_select = ch_select 
        self.ch_save = ch_save 
        self.pause = pause
        self.path = path
        self.current_ch_num = 0

    @timing_decorator
    def change_channel(self, ch_num):
        if self.current_ch_num == ch_num:
            print(f'Номер канала сейчас - {self.current_ch_num}')
            time.sleep(self.pause)
        else:
            pyautogui.moveTo(self.ch_select)
            pyautogui.leftClick()
            pyautogui.moveTo(self.ch_list[ch_num])
            pyautogui.leftClick()
            pyautogui.moveTo(self.ch_save)
            pyautogui.leftClick()
            time.sleep(self.pause-0.9)
        self.current_ch_num = ch_num
        print(f'Канал изменен на {ch_num}')

    
    def channel_plus_one(self):
        if self.current_ch_num == 13:
            self.change_channel(1)
        else:
            self.change_channel(self.current_ch_num + 1)

    @timing_decorator
    def test(self, test_dur=15):
        current_time = datetime.now().strftime("%H-%M-%S")
        os.system(f'iperf3 -c 192.168.0.101 -t {test_dur} --logfile {self.path}/{self.name}_{current_time}_{self.current_ch_num}.csv')
        print(f'Тестирование на {self.current_ch_num} прошло')


if __name__ == '__main__':
    cors = [
        '',
        [1550, 559],
        [1550, 592],
        [1550, 623],
        [1550, 656],
        [1550, 685],
        [1550, 716],
        [1550, 749],
        [1550, 777],
        [1550, 810],
        [1550, 839],
        [1550, 866],
        [1550, 900],
        [1550, 935],
    ]
    save = [1684, 1169]

    select = [1535, 972]


    router1 = RouterInterfase(name='router', ip_addr='192.168.0.101', ch_list=cors, ch_select=select, ch_save=save)
    router1.change_channel(2)
    router1.change_channel(2)
    router1.change_channel(2)
    router1.change_channel(2)

