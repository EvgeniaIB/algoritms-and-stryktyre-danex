import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import subprocess
import os
from PIL import Image
import shutil

# Исходные данные
data = [3, 38, 5, 44, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
n = len(data)

fig, ax = plt.subplots(figsize=(12, 6))
ax.set_title("Сортировка вставками (плавное перемещение)", fontsize=14)
ax.set_xlim(-2, n + 2) 
ax.set_ylim(-15, max(data) + 15) 
ax.set_xticks([])
ax.set_yticks([])

# --- Генератор кадров ---
def insertion_sort_frames(arr):
    n = len(arr)
    steps = 4 # Количество промежуточных кадров

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        # 1. Поднимаем активный элемент (он "выезжает" и парит)
        for step in range(steps):
            curr_y = 15 * (step / steps)
            yield arr.copy(), i, -1, "lift", curr_y, i, i
            
        # 2. Ищем место и сдвигаем элементы вправо
        current_pos = i
        while j >= 0 and arr[j] > key:
            # Визуально сдвигаем j-й элемент на позицию j+1 (он уезжает вправо)
            for step in range(steps):
                shift_progress = (step + 1) / steps
                # Передаем изначальный индекс i, чтобы активный элемент висел на месте
                yield arr.copy(), i, j, "shift", 15, current_pos + shift_progress, i
                
            # Физически сдвигаем в массиве
            arr[j + 1] = arr[j]
            current_pos -= 1
            j -= 1
            
        # Ставим ключ на его новое место в массиве
        arr[j + 1] = key
        
        # 3. Опускаем активный элемент на освободившееся место (j+1)
        for step in range(steps):
            curr_y = 15 * (1 - (step + 1) / steps)
            # Двигаем по X из начальной позиции (i) в новую (j+1)
            curr_x = i - (i - (j + 1)) * ((step + 1) / steps)
            yield arr.copy(), j + 1, -1, "drop", curr_y, curr_x, i
            
    yield arr.copy(), -1, -1, "done", 0, 0, 0

# --- Генерация картинок ---
frames = list(insertion_sort_frames(data.copy()))
temp_dir = "temp_frames_insertion_v3"
if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)

print(f"Генерация {len(frames)} кадров...")

for idx, (arr, active_idx, shift_idx, action, y_offset, x_pos, origin_pos) in enumerate(frames):
    ax.clear()
    ax.set_title("Сортировка вставками (плавное перемещение)", fontsize=14)
    ax.set_xlim(-2, n + 2) 
    ax.set_ylim(-15, max(data) + 15) 
    ax.set_xticks([])
    ax.set_yticks([])

    if action == "done":
        for k in range(n):
            rect = plt.Rectangle((k - 0.4, 0), 0.8, arr[k], facecolor='lightgreen', edgecolor='grey')
            ax.add_patch(rect)
            ax.text(k, arr[k] + 2, str(arr[k]), ha='center', va='bottom', fontsize=12, fontweight='bold')
    else:
        for k in range(n):
            pos_x = k
            pos_y = 0
            color = 'skyblue'
            zorder = 1
            height = arr[k]
            
            # --- ЛОГИКА ОТРИСОВКИ ---
            
            # Если это сдвигаемый элемент (он подсвечивается и уезжает)
            if action == "shift" and k == shift_idx:
                pos_x = x_pos 
                color = 'green'
                zorder = 5
                
            # Если это активный (парящий) элемент
            if k == active_idx and action != "none":
                # Если идет сдвиг, активный элемент висит строго на своей ИЗНАЧАЛЬНОЙ позиции
                if action == "shift":
                    pos_x = origin_pos 
                else:
                    pos_x = x_pos
                    
                pos_y = y_offset
                color = 'orange' if action != "drop" else 'crimson'
                zorder = 10 # Поверх всех

            # Рисуем столбец
            rect = plt.Rectangle((pos_x - 0.4, pos_y), 0.8, height, 
                                 facecolor=color, edgecolor='grey', zorder=zorder)
            ax.add_patch(rect)
            
            # Текст
            text_val = arr[k] if k != active_idx else int(height) 
            ax.text(pos_x, pos_y + height + 2, str(text_val), 
                    ha='center', va='bottom', fontsize=12, fontweight='bold', zorder=zorder+1)

    filename = f"{temp_dir}/frame_{idx:03d}.png"
    fig.savefig(filename, dpi=80)

print("Склейка в GIF...")
images = [Image.open(f"{temp_dir}/frame_{idx:03d}.png") for idx in range(len(frames))]

gif_path = "insertion_sort_clean.gif"
images[0].save(gif_path, save_all=True, append_images=images[1:], duration=200, loop=0)

shutil.rmtree(temp_dir)
print(f"Готово! Открываю {gif_path}...")
subprocess.call(["open", gif_path])