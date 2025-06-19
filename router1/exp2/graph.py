import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из CSV
df = pd.read_csv("wifi_data.csv")

# Добавление столбца с первым номером канала
df['First_Channel'] = df['Конфигурация каналов'].apply(lambda x: int(x.split('-')[0]))

# Группировка по первому номеру канала
grouped = df.groupby('First_Channel')

# Параметры для построения графиков
params = {
    'Скорость передачи данных (Mbps)': 'Speed (Mbps)',
    'Потери пакетов (%)': 'Packet Loss (%)',
    'Задержка (мс)': 'Latency (ms)',
    'RSSI (dBm)': 'RSSI (dBm)'
}

# Построение графиков для каждой группы
for group_key, group_df in grouped:
    fig, axs = plt.subplots(2, 2, figsize=(14, 8))
    fig.suptitle(f'Конфигурации с первым каналом {group_key}', fontsize=16)
    
    for i, (col, label) in enumerate(params.items()):
        ax = axs[i // 2][i % 2]
        x = group_df['Конфигурация каналов']
        y1 = group_df[col]
        y2 = group_df[col + '.1']
        
        ax.plot(x, y1, marker='o', label='Сеть 1', color='blue')
        ax.plot(x, y2, marker='o', label='Сеть 2', color='red')
        ax.set_title(label)
        ax.set_xlabel('Конфигурация каналов')
        ax.set_ylabel(label)
        ax.legend()
        ax.grid(True)
        ax.tick_params(axis='x', rotation=45)
    
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()
