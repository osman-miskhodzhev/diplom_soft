import pandas as pd
import matplotlib.pyplot as plt

# Замените путь к вашему файлу здесь
file_path = "data/ex2.csv"  # например: 'network_data.csv'

# Чтение CSV-файла
df = pd.read_csv(file_path, sep=';')

# Словарь с параметрами для построения графиков
params = {
    "Скорость передачи данных": ("Скорость передачи данных (Mbps)", "Скорость передачи данных (Mbps)", "Мбит/с"),
    "Потери пакетов": ("Потери пакетов (%)", "Потери пакетов (%)", "%"),
    "Задержка": ("Задержка (мс)", "Задержка (мс)", "мс"),
    "RSSI": ("RSSI (dBm)", "RSSI (dBm)", "dBm")
}

# Префиксы для столбцов двух сетей
net1_prefix = "Сеть 1"
net2_prefix = "Сеть 2"

# Построение графиков по каждому параметру
for title, (param1, param2, unit) in params.items():
    plt.figure(figsize=(10, 5))
    plt.plot(df["Конфигурация каналов"], df[f"{net1_prefix}.{param1}"], marker='o', label='Сеть 1')
    plt.plot(df["Конфигурация каналов"], df[f"{net2_prefix}.{param2}"], marker='s', label='Сеть 2')
    plt.title(f"{title} от конфигурации каналов")
    plt.xlabel("Конфигурация каналов")
    plt.ylabel(f"{title} ({unit})")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
