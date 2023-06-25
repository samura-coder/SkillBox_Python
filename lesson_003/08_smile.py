# -*- coding: utf-8 -*-

# (определение функций)

import simple_draw as sd
sd.resolution = (1400, 700)

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

x = 700
y = 350

def smile(x = x, y = y, size = 50, color = sd.COLOR_ORANGE):
    point = sd.get_point(x, y)
    sd.circle(point, size, color, 0)
    point_mouth_1 = sd.get_point(x - size * 0.6, y - size * 0.4)
    point_mouth_2 = sd.get_point(x - size * 0.57, y - size * 0.45)
    point_mouth_3 = sd.get_point(x - size * 0.55, y - size * 0.5)
    point_mouth_4 = sd.get_point(x - size * 0.465, y - size * 0.62)
    point_mouth_5 = sd.get_point(x - size * 0.35, y - size * 0.63)
    point_mouth_6 = sd.get_point(x - size * 0.18, y - size * 0.68)
    point_mouth_7 = sd.get_point(x - size * 0.1, y - size * 0.7)
    point_mouth_8 = sd.get_point(x + size * 0.1, y - size * 0.7)
    point_mouth_9 = sd.get_point(x + size * 0.18, y - size * 0.68)
    point_mouth_10 = sd.get_point(x + size * 0.35, y - size * 0.63)
    point_mouth_11 = sd.get_point(x + size * 0.465, y - size * 0.62)
    point_mouth_12 = sd.get_point(x + size * 0.55, y - size * 0.5)
    point_mouth_13 = sd.get_point(x + size * 0.57, y - size * 0.45)
    point_mouth_14 = sd.get_point(x + size * 0.6, y - size * 0.4)
    point_list_mouth = [point_mouth_1,                # список точек для отрисовки улыбки
                        point_mouth_2,
                        point_mouth_3,
                        point_mouth_4,
                        point_mouth_5,
                        point_mouth_6,
                        point_mouth_7,
                        point_mouth_8,
                        point_mouth_9,
                        point_mouth_10,
                        point_mouth_11,
                        point_mouth_12,
                        point_mouth_13,
                        point_mouth_14
                       ]
    sd.lines(point_list_mouth, sd.COLOR_BLACK, True, 3)
    point_eye_left_1 = sd.get_point(x - size * 0.6, y + size * 0.3)
    point_eye_left_2 = sd.get_point(x - size * 0.1, y + size * 0.15)
    point_eye_left_3 = sd.get_point(x - size * 0.6, y + size * 0.01)
    point_eye_left_4 = sd.get_point(x - size * 0.2, y + size * 0.15)
    point_list_eye_left = [point_eye_left_1,
                            point_eye_left_2,
                            point_eye_left_3,
                            point_eye_left_4
                            ]
    sd.lines(point_list_eye_left, sd.COLOR_BLACK, True, 3)
    point_eye_right_1 = sd.get_point(x + size * 0.6, y + size * 0.3)
    point_eye_right_2 = sd.get_point(x + size * 0.1, y + size * 0.15)
    point_eye_right_3 = sd.get_point(x + size * 0.6, y + size * 0.01)
    point_eye_right_4 = sd.get_point(x + size * 0.2, y + size * 0.15)
    point_list_eye_right = [point_eye_right_1,
                            point_eye_right_2,
                            point_eye_right_3,
                            point_eye_right_4
                            ]
    sd.lines(point_list_eye_right, sd.COLOR_BLACK, True, 3)


for i in range(10):
    x = sd.random_number(0, 1400)
    y = sd.random_number(0, 700)
    smile(x, y)


sd.pause()
