# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000

parental_help = 0
month_counter = 1
total_expenses = expenses
indexation = 1.03
quantity_number = 10

while month_counter < quantity_number:
    expenses *= indexation
    total_expenses += expenses
    month_counter += 1

parental_help = round(total_expenses - educational_grant * quantity_number, 2)

print('Студенту необходимо попросить у родителей', parental_help, 'руб.')
