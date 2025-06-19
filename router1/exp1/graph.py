import matplotlib.pyplot as plt
import numpy as np

# Данные из таблицы 1 (оригинальные)
data1 = [
    ("1-2", 1.02, 3, 1.058, -72),
    ("1-3", 1.04, 0.54, 1.477, -65),
    ("1-4", 1.05, 0, 2.306, -58),
    ("1-5", 1.01, 3.2, 1.764, -75),
    ("1-6", 1.05, 0, 0.946, -55),
    ("1-7", 1.05, 0, 1.064, -60),
    ("1-8", 1.03, 1.7, 1.042, -68),
    ("1-9", 1.05, 0, 0.795, -52),
    ("1-10", 1.05, 0, 1.160, -62),
    ("1-11", 1.05, 0, 0.896, -57),
    ("1-12", 1.04, 0.91, 1.619, -67),
    ("1-13", 1.04, 0.69, 0.901, -63),
]

# Данные из таблицы 2 (Сеть 2)
data2 = [
    ("1-2", 1.03, 1.1, 1.12, -71),
    ("1-3", 1.05, 0.8, 1.45, -66),
    ("1-4", 1.06, 0.3, 1.98, -59),
    ("1-5", 1.00, 3.3, 1.60, -74),
    ("1-6", 1.04, 0.2, 0.92, -54),
    ("1-7", 1.06, 0.1, 1.01, -61),
    ("1-8", 1.02, 1.6, 1.10, -69),
    ("1-9", 1.05, 0.1, 0.76, -53),
    ("1-10", 1.04, 0.2, 1.18, -63),
    ("1-11", 1.05, 0.3, 0.93, -56),
    ("1-12", 1.03, 1.2, 1.58, -68),
    ("1-13", 1.03, 0.9, 0.88, -62),
]

# Извлечение данных
channels = [item[0] for item in data1]
speed1 = [item[1] for item in data1]
loss1 = [item[2] for item in data1]
delay1 = [item[3] for item in data1]
rssi1 = [item[4] for item in data1]

speed2 = [item[1] for item in data2]
loss2 = [item[2] for item in data2]
delay2 = [item[3] for item in data2]
rssi2 = [item[4] for item in data2]

# Настройка стиля и размера графиков
plt.style.use('ggplot')  # Альтернативный стиль
plt.rcParams['figure.figsize'] = [10, 6]
plt.rcParams['font.size'] = 10

# Функция для создания отдельных графиков
def create_single_plot(x, y, title, ylabel, xlabel="Конфигурация каналов", color='blue'):
    plt.figure()
    plt.bar(x, y, color=color)
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

# 1. Графики скорости передачи данных
create_single_plot(channels, speed1, 
                  "Скорость передачи данных (Сеть 1)", 
                  "Скорость (Mbps)", color='royalblue')

create_single_plot(channels, speed2, 
                  "Скорость передачи данных (Сеть 2)", 
                  "Скорость (Mbps)", color='cornflowerblue')

# 2. Графики потерь пакетов
create_single_plot(channels, loss1, 
                  "Потери пакетов (Сеть 1)", 
                  "Потери (%)", color='crimson')

create_single_plot(channels, loss2, 
                  "Потери пакетов (Сеть 2)", 
                  "Потери (%)", color='lightcoral')

# 3. Графики задержки
create_single_plot(channels, delay1, 
                  "Задержка передачи (Сеть 1)", 
                  "Задержка (мс)", color='forestgreen')

create_single_plot(channels, delay2, 
                  "Задержка передачи (Сеть 2)", 
                  "Задержка (мс)", color='limegreen')

# 4. Графики мощности сигнала (RSSI)
create_single_plot(channels, rssi1, 
                  "Мощность сигнала RSSI (Сеть 1)", 
                  "RSSI (dBm)", color='darkorange')

create_single_plot(channels, rssi2, 
                  "Мощность сигнала RSSI (Сеть 2)", 
                  "RSSI (dBm)", color='gold')