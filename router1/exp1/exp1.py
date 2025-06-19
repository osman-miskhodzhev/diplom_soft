import pyautogui
import time
import datetime
import os

channel_select_btn = (1660, 990)
channel_1_9 = (1660, 775)
channel_10 = (1660, 818)
channel_11 = (1660, 860)
channel_12 = (1660, 890)
channel_13 = (1660, 935)
save_btn = (1770, 1160)

def test():
    os.system('iperf3 -c 192.168.1.101 -t 30 -u')

def move_to_change_channel():
    pyautogui.moveTo(channel_select_btn)

def move_to_save():
    pyautogui.moveTo(save_btn)

for x in range(8):
    move_to_change_channel()
    pyautogui.leftClick()
    pyautogui.moveTo(channel_1_9)
    pyautogui.leftClick()
    move_to_save()
    pyautogui.leftClick()
    time.sleep(10.0)
    print(datetime.datetime.now())
    print('Провести исследование на', x+2)
    os.system(f'iperf3 -c 192.168.1.101 -t 10 --logfile ex1-router1-channe-{x+2}.txt')
    print('Исследование завершено')
    print(datetime.datetime.now())

move_to_change_channel()
pyautogui.leftClick()
pyautogui.moveTo(channel_10)
pyautogui.leftClick()
move_to_save()
pyautogui.leftClick()
time.sleep(10.0)
print(datetime.datetime.now())
print('Провести исследование на', 10)
os.system(f'iperf3 -c 192.168.1.101 -t 10 --logfile ex1-router1-channel-{10}.txt')
print(datetime.datetime.now())

move_to_change_channel()
pyautogui.leftClick()
pyautogui.moveTo(channel_11)
pyautogui.leftClick()
move_to_save()
pyautogui.leftClick()
time.sleep(10.0)
print(datetime.datetime.now())
print('Провести исследование на', 11)
os.system(f'iperf3 -c 192.168.1.101 -t 10 --logfile ex1-router1-channel-{11}.txt')
print(datetime.datetime.now())

move_to_change_channel()
pyautogui.leftClick()
pyautogui.moveTo(channel_12)
pyautogui.leftClick()
move_to_save()
pyautogui.leftClick()
time.sleep(10.0)
print(datetime.datetime.now())
print('Провести исследование на', 12)
os.system(f'iperf3 -c 192.168.1.101 -t 10 --logfile ex1-router1-channel-{12}.txt')
print(datetime.datetime.now())

move_to_change_channel()
pyautogui.leftClick()
pyautogui.moveTo(channel_13)
pyautogui.leftClick()
move_to_save()
pyautogui.leftClick()
time.sleep(10.0)
print(datetime.datetime.now())
print('Провести исследование на', 13)
os.system(f'iperf3 -c 192.168.1.101 -t 10 --logfile ex1-router1-channel-{13}.txt')
print(datetime.datetime.now())
