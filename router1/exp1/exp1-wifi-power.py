import pyautogui
import time
import datetime
import os
import subprocess

# Координаты для управления интерфейсом роутера
channel_select_btn = (1660, 990)
channel_1_9 = (1660, 775)
channel_10 = (1660, 818)
channel_11 = (1660, 860)
channel_12 = (1660, 890)
channel_13 = (1660, 935)
save_btn = (1770, 1160)

def get_wifi_signal():
    """Возвращает RSSI в dBm с помощью netsh (с исправленной кодировкой)"""
    try:
        # Указываем кодировку 'cp866' для русской Windows или 'cp1251' для некоторых систем
        result = subprocess.check_output("netsh wlan show interfaces", shell=True, encoding='cp866')
        for line in result.split('\n'):
            if "Сигнал" in line or "Signal" in line:  # Поддержка разных языков
                percent = int(line.split(':')[1].replace('%', '').strip())
                rssi = -100 + (percent / 2)  # Примерная конвертация % в dBm
                return round(rssi, 1)
    except Exception as e:
        print(f"Ошибка при измерении сигнала: {e}")
    return None

def change_channel(channel_coords):
    """Переключает канал на роутере"""
    pyautogui.moveTo(channel_select_btn)
    pyautogui.leftClick()
    time.sleep(1)
    pyautogui.moveTo(channel_coords)
    pyautogui.leftClick()
    time.sleep(1)
    pyautogui.moveTo(save_btn)
    pyautogui.leftClick()
    time.sleep(5)  # Ждем применения настроек

def main():
    channels = {
        1: channel_1_9,
        2: channel_1_9,
        3: channel_1_9,
        4: channel_1_9,
        5: channel_1_9,
        6: channel_1_9,
        7: channel_1_9,
        8: channel_1_9,
        9: channel_1_9,
        10: channel_10,
        11: channel_11,
        12: channel_12,
        13: channel_13
    }

    with open("wifi_signal_log.csv", "w", encoding='utf-8') as log_file:
        log_file.write("Channel;RSSI (dBm);Timestamp\n")  # Заголовок CSV

        for channel, coords in channels.items():
            print(f"Переключаемся на канал {channel}...")
            change_channel(coords)
            time.sleep(10)  # Ждем стабилизации
            
            measurements = []
            for _ in range(3):  # 3 замера для усреднения
                rssi = get_wifi_signal()
                if rssi is not None:
                    measurements.append(rssi)
                time.sleep(2)
            
            if measurements:
                avg_rssi = round(sum(measurements) / len(measurements), 1)
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log_line = f"{channel};{avg_rssi};{timestamp}"
                log_file.write(log_line + "\n")
                print(f"Канал {channel}: {avg_rssi} dBm")
            else:
                print(f"Не удалось измерить сигнал для канала {channel}")

if __name__ == "__main__":
    main()