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
    path='experiment_2/results',
    ch_list=cors,
    ch_select=select,
    ch_save=save
)

"""
схема эксперимета:
1-2
1-3
1-4
1-5
2-3
2-4
2-5
2-6
...
9-10
9-11
9-12
9-13

10-11
10-12
10-13

11-12
11-13

12-13

на первом роутере меняю первые номера каналов
"""

for i in range(1, 13):
    if i <= 9:
        max_j = i + 4
    else:
        max_j = 13
    for j in range(i + 1, max_j + 1):
        router1.change_channel(i)
        router1.test()

