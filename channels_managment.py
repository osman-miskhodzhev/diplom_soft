import os
import time
import pyautogui

def change_channel(ch_list, ch_select, ch_save, ch_num, pause=5):
    pyautogui.moveTo(ch_select)
    pyautogui.leftClick()
    pyautogui.moveTo(ch_list[ch_num])
    pyautogui.leftClick()
    pyautogui.moveTo(ch_save)
    pyautogui.leftClick()
    time.sleep(pause)
    print(f'Канал изменен на {ch_num}')
