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

router1 = RouterInterfase(
    name='router_1',
    ip_addr='192.168.0.101',
    path='experiment_1/results',
    ch_list=cors,
    ch_select=select,
    ch_save=save,
    pause=0.9
)

"""
На первом роутере поочередно меняю канал от 2 до 13 и провожу тестирование
"""
bad_list = [1, 2, 5, 7, 9, 11, 13]
for x in bad_list:
    router1.change_channel(x)
    router1.test(test_dur=10)