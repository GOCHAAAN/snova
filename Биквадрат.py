import math
print ("введите коэфицент для уровнения")
print ("ax^4 - bx^2 + c:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
pow(a ** 0.5, b ** 0.5)

discr = b ** 2 - 4 * a * c
print("Дискриминант D = ", discr)

if discr > 0:
    x1 = (b - math.sqrt(discr)) / (2 * a)
    x2 = (b + math.sqrt(discr)) / (2 * a)
    print("x1 = ", x1, "x2 = ", x2)
elif discr == 0:
    x = -b / (2 * a)
    print ('x = ', x)
else:
    print("Корней нет")

