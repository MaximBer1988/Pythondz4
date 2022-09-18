# 1.	Вычислить число c заданной точностью d
# Пример:
# a.	при $d = 0.001, π = 3.141

import math
Pi = math.pi
n= int(input("Введите количество отображаемых знаков после запятой числа Пи: "))
st=10**n
print(st)
digits = round(Pi*st)
print(digits/st)
