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
    ip_addr='192.168.0.100',
    ch_list=cors,
    ch_select=select,
    ch_save=save
)

"""
На втором роутере всегда канал номер 1, тестирование проводится с интервалом в 5 сек
"""
for x in range(2, 14):
    time.sleep(5.1)
    router1.test()