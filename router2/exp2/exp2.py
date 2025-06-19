import os
import time
import pyautogui

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

def change_channel(ch_num):
    pyautogui.moveTo(select)
    pyautogui.leftClick()
    pyautogui.moveTo(cors[ch_num])
    pyautogui.leftClick()
    pyautogui.moveTo(save)
    pyautogui.leftClick()
    time.sleep(5)
    print(f'текущий канал - {ch_num}')

def move_to_save():
    pyautogui.moveTo(save)

test_dr = 1

current_ch = 1

# Канал 1
# change_channel(1)
# for sub_ch in range(2, 6):
#     os.system(f'iperf3 -c 192.168.0.101 -t {test_dr} --logfile ex2-router1-channels-1-{sub_ch}.csv')
#     print(sub_ch)

for ch in range(1, 10):
    for sub_ch in range(ch+1, ch+5):
        change_channel(sub_ch)
        print(f'Комбинация {ch} - {sub_ch}')
        os.system(f'iperf3 -c 192.168.0.101 -t {test_dr} --logfile ex2-router1-channels-{ch}-{sub_ch}.csv')