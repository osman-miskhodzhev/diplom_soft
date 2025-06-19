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
change_channel(1)
for sub_ch in range(2, 6):
    os.system(f'iperf3 -c 192.168.0.101 -t {test_dr} --logfile ex2-router1-channels-1-{sub_ch}.csv')
    print(sub_ch)

# Канал 2
change_channel(2)
for sub_ch in range(3, 7):
    os.system(f'iperf3 -c 192.168.0.101 -t {test_dr} --logfile ex2-router1-channels-2-{sub_ch}.csv')
    print(sub_ch)

# Канал 3
change_channel(3)
for sub_ch in range(4, 8):
    os.system(f'iperf3 -c 192.168.0.101 -t {test_dr} --logfile ex2-router1-channels-3-{sub_ch}.csv')
    print(sub_ch)

# Канал 4
change_channel(4)
for sub_ch in range(5, 9):
    os.system(f'iperf3 -c 192.168.0.101 -t {test_dr} --logfile ex2-router1-channels-4-{sub_ch}.csv')
    print(sub_ch)

# Канал 5
change_channel(5)
for sub_ch in range(6, 10):
    os.system(f'iperf3 -c 192.168.0.101 -t {test_dr} --logfile ex2-router1-channels-5-{sub_ch}.csv')
    print(sub_ch)

# Канал 6
change_channel(6)
for sub_ch in range(7, 11):
    os.system(f'iperf3 -c 192.168.0.101 -t {test_dr} --logfile ex2-router1-channels-6-{sub_ch}.csv')
    print(sub_ch)

# Канал 7
change_channel(7)
for sub_ch in range(8, 12):
    os.system(f'iperf3 -c 192.168.0.101 -t {test_dr} --logfile ex2-router1-channels-7-{sub_ch}.csv')
    print(sub_ch)

# Канал 8
change_channel(8)
for sub_ch in range(9, 13):
    os.system(f'iperf3 -c 192.168.0.101 -t {test_dr} --logfile ex2-router1-channels-8-{sub_ch}.csv')
    print(sub_ch)

# Канал 9
change_channel(9)
for sub_ch in range(10, 14):
    os.system(f'iperf3 -c 192.168.0.101 -t {test_dr} --logfile ex2-router1-channels-9-{sub_ch}.csv')
    print(sub_ch)

# Канал 10
change_channel(10)
for sub_ch in range(11, 14):
    os.system(f'iperf3 -c 192.168.0.101 -t {test_dr} --logfile ex2-router1-channels-10-{sub_ch}.csv')
    print(sub_ch)

# Канал 11
change_channel(11)
for sub_ch in range(12, 14):
    os.system(f'iperf3 -c 192.168.0.101 -t {test_dr} --logfile ex2-router1-channels-11-{sub_ch}.csv')
    print(sub_ch)

# Канал 12
change_channel(12)
for sub_ch in range(13, 14):
    os.system(f'iperf3 -c 192.168.0.101 -t {test_dr} --logfile ex2-router1-channels-12-{sub_ch}.csv')
    print(sub_ch)
