import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import subprocess
import os
from PIL import Image
import shutil

# Исходные данные (как на скриншотах)
data = [3, 38, 5, 44, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
n = len(data)

fig, ax = plt.subplots(figsize=(12, 6))
ax.set_title("Сортировка выбором (плавное перемещение)", fontsize=14)
ax.set_xlim(-2, n + 2) 
ax.set_ylim(-15, max(data) + 15) 
ax.set_xticks([])
ax.set_yticks([])

# --- Генератор кадров ---
def selection_sort_frames(arr):
    n = len(arr)
    steps = 5 # Количество промежуточных кадров для плавности

    for i in range(n - 1):
        min_idx = i
        
        # 1. Подсвечиваем текущий минимум (он будет "парить" или просто выделяться)
        # Мы просто проходим по массиву и ищем минимум. Чтобы не перегружать анимацию,
        # мы будем показывать только сам процесс поиска (смену min_idx).
        
        # Проходим по неотсортированной части
        for j in range(i + 1, n):
            # Показываем сравнение: текущий минимум (оранжевый) и проверяемый (синий)
            for step in range(steps):
                yield arr.copy(), min_idx, j, "compare", step / steps, i
                
            if arr[j] < arr[min_idx]:
                # Нашли новый минимум
                min_idx = j
                # Визуально "перекидываем" корону минимума
                for step in range(steps):
                    yield arr.copy(), min_idx, -1, "new_min", step / steps, i

        # 2. Обмен (если минимум не на своем месте)
        if min_idx != i:
            # Поднимаем оба элемента для обмена
            for step in range(steps):
                yield arr.copy(), i, min_idx, "lift", step / steps, i
                
            # Перелет (двигаются навстречу)
            for step in range(steps):
                yield arr.copy(), i, min_idx, "swap", (step + 1) / steps, i
                
            # Физически меняем в массиве
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            
            # Опускаем на места
            for step in range(steps):
                yield arr.copy(), i, min_idx, "drop", 1 - (step + 1) / steps, i
                
    yield arr.copy(), -1, -1, "done", 0, 0

# --- Генерация картинок ---
frames = list(selection_sort_frames(data.copy()))
temp_dir = "temp_frames_selection"
if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)

print(f"Генерация {len(frames)} кадров...")

for idx, (arr, active_idx, target_idx, action, progress, sorted_limit) in enumerate(frames):
    ax.clear()
    ax.set_title("Сортировка выбором (плавное перемещение)", fontsize=14)
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
            
            # Элементы, которые уже отсортированы, делаем бледно-голубыми или зеленоватыми
            if k < sorted_limit:
                color = 'lightblue'
            
            # --- ЛОГИКА ОТРИСОВКИ ---
            
            # Текущий минимум (подсвечиваем оранжевым)
            if k == active_idx:
                color = 'orange'
                zorder = 5
                
                if action in ["lift", "swap", "drop"]:
                    pos_y = 15 * progress if action == "lift" else (15 if action == "swap" else 15 * progress)
                    if action == "swap":
                        if k == active_idx:
                            pos_x = k + (target_idx - k) * progress
                        elif k == target_idx:
                            pos_x = k - (k - active_idx) * progress
            
            # Проверяемый элемент (подсвечиваем зеленым)
            if k == target_idx and action != "new_min":
                color = 'green'
                zorder = 3
                
            # Если это обмен, второй элемент тоже летит
            if action in ["lift", "swap", "drop"] and k == target_idx:
                color = 'crimson' if action == "swap" else 'green'
                zorder = 5
                pos_y = 15 * progress if action == "lift" else (15 if action == "swap" else 15 * progress)
                if action == "swap":
                    if k == active_idx:
                        pos_x = k + (target_idx - k) * progress
                    elif k == target_idx:
                        pos_x = k - (k - active_idx) * progress

            # Рисуем столбец
            rect = plt.Rectangle((pos_x - 0.4, pos_y), 0.8, height, 
                                 facecolor=color, edgecolor='grey', zorder=zorder)
            ax.add_patch(rect)
            
            # Текст
            ax.text(pos_x, pos_y + height + 2, str(arr[k]), 
                    ha='center', va='bottom', fontsize=12, fontweight='bold', zorder=zorder+1)

    filename = f"{temp_dir}/frame_{idx:03d}.png"
    fig.savefig(filename, dpi=80)

print("Склейка в GIF...")
images = [Image.open(f"{temp_dir}/frame_{idx:03d}.png") for idx in range(len(frames))]

gif_path = "selection_sort_clean.gif"
images[0].save(gif_path, save_all=True, append_images=images[1:], duration=150, loop=0)

shutil.rmtree(temp_dir)
print(f"Готово! Открываю {gif_path}...")
subprocess.call(["open", gif_path])