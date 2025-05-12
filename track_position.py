import pyautogui
import time
import sys

def track_mouse_position(interval=0.1, duration=30):
    """
    Отображает текущие координаты мыши в реальном времени.
    
    :param interval: интервал обновления в секундах
    :param duration: продолжительность работы в секундах (None для бесконечной работы)
    """
    while True:
        x, y = pyautogui.position()
        print(f'x: {x} y: {y}')

if __name__ == "__main__":
    # Запуск на 30 секунд с обновлением каждые 0.1 секунды
    track_mouse_position(interval=0.9, duration=30)