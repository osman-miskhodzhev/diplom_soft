import os
import time
import pyautogui

class RouterInterfase:
    def __init__(self, ch_list, ch_select, ch_save, pause=5):
        self.ch_list = ch_list 
        self.ch_select = ch_select 
        self.ch_save = ch_save 
        self.pause = pause
        self.current_ch_num = 1
    
    def change_channel(self, ch_num):
        pyautogui.moveTo(self.ch_select)
        pyautogui.leftClick()
        pyautogui.moveTo(self.ch_list[ch_num])
        pyautogui.leftClick()
        pyautogui.moveTo(self.ch_save)
        pyautogui.leftClick()
        time.sleep(self.pause)
        self.current_ch_num = ch_num
        print(f'Канал изменен на {ch_num}')

    
    def channel_plus_one(self):
        if self.current_ch_num == 13:
            self.change_channel(1)
        else:
            self.change_channel(self.current_ch_num + 1)


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


    router1 = RouterInterfase(ch_list=cors, ch_select=select, ch_save=save)
    router1.change_channel(2)
