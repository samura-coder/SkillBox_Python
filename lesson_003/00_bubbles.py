# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1400, 700)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей

radius = 50
step = 5
point_0 = sd.get_point(600, 300)
color = sd.COLOR_RED
y = 100


# for _ in range(3):
#     sd.circle(point_0, radius)
#     radius += step


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг


def bubble(point=point_0, radius=radius, step=step, color=color):
    for _ in range(3):
        sd.circle(point, radius, color=color)
        radius += step


# Нарисовать 10 пузырьков в ряд

# for x in range(100, 1100, 100):
#     bubble(sd.get_point(x, y), radius, step, color)

# Нарисовать три ряда по 10 пузырьков

# for y in range(100, 400, 100):
#     for x in range(100, 1100, 100):
#         bubble(sd.get_point(x, y), radius, step, color)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами

for _ in range(100):
    point = sd.random_point()
    step = sd.randint(4, 10)
    radius = sd.randint(20, 80)
    color = sd.random_color()
    bubble(point, radius, step, color)

sd.pause()
