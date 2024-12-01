import matplotlib.pyplot as plt
import os
import numpy as np

# Функція для прочитання датасету з текстового файлу
def read_file(file_path):
    # Перевяємо, чи існує файл
    if not os.path.exists(file_path):
        print(f"Файл '{file_path}' не знайдено в директорії проєкту.")
        return []
    # Збергіаємо точки як список кортежів після перевірки на їх коректність
    points = []
    with open(file_path, 'r') as file:
        # Рахуємо номер рядку, щоб при можливих некоректних значеннях координат вказати користувачу, де саме помилка
        line_number = 1
        for line in file:
            try:
                y, x = map(int, line.split())
                points.append((x, y))
            except ValueError:
                # Повідомляємо користувача, якщо є некоректні значення в файлі
                print(f"Некоректні значення координат у рядку {line_number}: {line.strip()}")
                return []
            line_number += 1
    return points

# Функція для створення матриці перетворення
def create_transform_matrix(angle, center):
    # Перетворюємо кут у радіани і обчислюємо для нього синус і косинус
    cos_alpha = np.cos(np.radians(angle))
    sin_alpha = np.sin(np.radians(angle))
    x_c, y_c = center
    # Створюємо та обчислюємо матрицю перетворення
    transform_matrix = np.array([
        [cos_alpha, sin_alpha, 0],
        [-sin_alpha, cos_alpha, 0],
        [x_c * (1 - cos_alpha) + y_c * sin_alpha, y_c * (1 - cos_alpha) - x_c * sin_alpha, 1]
    ])
    return transform_matrix

# Функція для обертання точок з використанням матриці перетворення
def rotate(points, angle, center):
    transform_matrix = create_transform_matrix(angle, center)
    rotated_points = []
    # Обчислюємо нові координати для кожної точки
    for x, y in points:
        point = np.array([x, y, 1])
        rotated_point = point.dot(transform_matrix)
        rotated_points.append((rotated_point[0], rotated_point[1]))
    return rotated_points

# Функція для побудови графіка за точками
def plot(points):
    # Встановлюємо розміри полотна за умовами завдання
    plt.figure(figsize=(9.6, 9.6)) 
    # Розділюємо координати точок на х та у
    x, y = zip(*points)
    # Налаштування графіку та координатної площини
    plt.scatter(x, y, color = "blue")
    plt.title("Лабораторна робота №3\nСемеряга Софія, КМ-31, датасет DS8", fontsize=12)
    plt.savefig("affine_transform_plot.png", format="png")
    plt.show()
    plt.close()

# Головна функція
def main():
    # Назва файлу з датасетом
    file_path = "DS8.txt"
    points = read_file(file_path)
    # Винесла n, формулу для обчислення кута альфа і центр обертання в окремі змінні
    # для того, щоб у разі потреби швидно змінити ці значення
    n = 8
    alpha = 10 * (n + 1) 
    center = (480, 480)
    rotated_points = rotate(points, alpha, center)
    plot(rotated_points)

if __name__ == "__main__":
    main()
