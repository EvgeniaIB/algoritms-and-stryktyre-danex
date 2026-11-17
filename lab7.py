import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import subprocess
import os
import sys
from PIL import Image

# --- Настройка данных ---
data = [3, 38, 5, 44, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
n = len(data)

fig, ax = plt.subplots(figsize=(12, 6))
ax.set_title("Сортировка пузырьком", fontsize=14)
ax.set_xlim(0, n)
ax.set_ylim(0, max(data) + 10)
ax.set_xticks([])
ax.set_yticks([])

bars = ax.bar(range(n), data, color='skyblue', edgecolor='grey')
texts = [ax.text(i + 0.5, data[i] + 2, str(data[i]), ha='center', va='bottom', fontsize=12, fontweight='bold') for i in range(n)]

def bubble_sort_steps(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            yield arr.copy(), j, j + 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

# --- Ручная генерация кадров ---
frames = list(bubble_sort_steps(data.copy()))
images = []
temp_dir = "temp_frames"
if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)

print(f"Генерация {len(frames)} кадров. Подожди...")

for idx, frame_data in enumerate(frames):
    arr, idx1, idx2 = frame_data
    
    # Сброс цветов
    for bar in bars:
        bar.set_color('skyblue')
        
    # Красим сравниваемую пару
    bars[idx1].set_color('green')
    bars[idx2].set_color('green')
    
    # Обновляем высоты
    for i, (bar, val) in enumerate(zip(bars, arr)):
        bar.set_height(val)
        texts[i].set_y(val + 2)
        texts[i].set_text(str(val))
        texts[i].set_x(bar.get_x() + bar.get_width() / 2)
        
    # Сохраняем кадр
    filename = f"{temp_dir}/frame_{idx:03d}.png"
    fig.savefig(filename, dpi=80)
    
print("Склейка в GIF...")

# --- Склейка картинок в GIF ---
images = []
for idx in range(len(frames)):
    img = Image.open(f"{temp_dir}/frame_{idx:03d}.png")
    images.append(img)

gif_path = "bubble_sort.gif"
# Сохраняем как GIF (duration=300ms, loop=0 означает бесконечный цикл)
images[0].save(gif_path, save_all=True, append_images=images[1:], duration=300, loop=0)

# Очистка временных файлов
import shutil
shutil.rmtree(temp_dir)

print(f"Готово! Открываю {gif_path}...")
subprocess.call(["open", gif_path])