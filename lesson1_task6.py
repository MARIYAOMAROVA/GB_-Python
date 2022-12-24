# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

# запрос данных пользователя
a = int(input("Введите расстояние первой пробежки в км: "))
b = int(input("Введите целевой результат в км: "))

counter = 1  # начальное значение счетчика дней

while a < b:
    a *= 1.1  # расчет расстояния пробежки
    counter += 1  # увеличение счетчика дней

# вывод рез-та
print(f"На {counter}-й день спортсмен достиг результата — не менее {b} км")