# ПЕРЕИМЕНОВАТЬ: минуты — minutes, время — time
a = int(input(' '))
# ИСПРАВИТЬ: лишний пробел в выводе: в случае если вы будете генерировать строку не для человека, а для другой функции/класса/программы — это может стоить вам неработающего приложения
print(f' {a} мин - это {a // 60} час {a % 60} мин')

#  201
#  201 мин - это 3 час 21 мин


# ИТОГ: хорошо, доработать — 2/3