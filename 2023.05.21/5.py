# ПЕРЕИМЕНОВАТЬ: целая часть числа — integer: дробная часть числа — fractional
a, b = int(input(' ')), int(input(' '))
# ИСПРАВИТЬ: этот способ не сработает, если пользователю потребуется ввести дробную часть для числа с количеством десятичных знаков больше двух (см. пример ниже) — придумайте более универсальное решение
c = (a + (b / 10))

# ИСПОЛЬЗОВАТЬ: круглые скобки используются для формирования кортежа, генераторного выражения, изменения приоритетов операторов и записи многострочных выражений — больше нигде и никак
print(f'{c} миль = {c * 1.61:.1f} км')

#  9
#  4
# 9.4 миль = 15.1 км

#  5
#  81
# КОММЕНТАРИЙ: а должно быть 5.81 миль
# 13.1 миль = 21.1 км


# ИТОГ: доработать — 3/6
