# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

sd.resolution = (1400, 700)
sd.background_color = sd.COLOR_DARK_RED

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for


shift = 50
for y in range(0, 700, 50):
    length_x = 100
    length_y = 50
    shift = 50 - shift
    for x in range(shift, 1400, 100):
        left_bottom = sd.get_point(x, y)
        right_top = sd.get_point(x + length_x, y + length_y)
        sd.rectangle(left_bottom, right_top, sd.COLOR_WHITE, 2)

sd.pause()
