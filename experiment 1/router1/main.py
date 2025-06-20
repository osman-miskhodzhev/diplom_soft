from router_managment.core import RouterInterfase

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

router1 = RouterInterfase(
    ch_list=cors,
    ch_select=select,
    ch_save=save
)

router1.change_channel(2)