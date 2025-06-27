import os
import time
import pyautogui

from router_managment.core import RouterInterfase

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
router = RouterInterfase(
    name='router_1',
    ip_addr='192.168.0.103',
    path='results',
    ch_list=cors,
    ch_select=select,
    ch_save=save,
    pause=0.9
)

# while True:
#     ch_number = int(input('Номер канала >>> '))
#     router.change_channel(ch_num=ch_number)

e1_r1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for x in e1_r1:
    comand = input('>>> ')
    if comand == 'n':
        router.change_channel(ch_num=x)
    elif comand == 't':
        router.test(test_dur=10)
