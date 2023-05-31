# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

sd.resolution = (1400, 700)

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)


# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)


def rainbow_line():  # сделал функцию для удобства
    x_start, y_start = 5, 10
    x_end, y_end = 1395, 610
    for color in rainbow_colors:
        start_point = sd.get_point(x_start, y_start)
        end_point = sd.get_point(x_end, y_end)
        sd.line(start_point, end_point, color, 12)
        y_start += 13
        y_end += 13


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво


def rainbow_circle():  # сделал функцию для удобства
    x_center, y_center = 700, -1000
    center_point = sd.get_point(x_center, y_center)
    radius = 1500
    width = 12
    for color in rainbow_colors:
        sd.circle(center_point, radius, color, width)
        radius -= 11


rainbow_line()
rainbow_circle()

sd.pause()
