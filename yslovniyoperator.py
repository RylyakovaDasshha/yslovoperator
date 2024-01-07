#1
a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
c = float(input("Введите число c: "))

if a >= b and a >= c:
    print("Максимальное число:", a)
elif b >= a and b >= c:
    print("Максимальное число:", b)
else:
    print("Максимальное число:", c)

#2

a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
c = float(input("Введите число c: "))

if a == b or a == c or b == c:
    print("Ошибка")
elif a > b and a < c or a < b and a > c:
    print("Среднее число:", a)
elif b > a and b < c or b < a and b > c:
    print("Среднее число:", b)
else:
    print("Среднее число:", c)

    #3

a = int(input("Введите большее число: "))
b = int(input("Введите меньшее число: "))

if a % b == 0:
    print(a, "кратно", b)
else:
    print(a, "не кратно", b, ", остаток:", a % b)

    #4

x = float(input("Введите координату x: "))
y = float(input("Введите координату y: "))

if x > 0 and y > 0:
    print("Точка находится в первой четверти")
elif x < 0 and y > 0:
    print("Точка находится во второй четверти")
elif x < 0 and y < 0:
    print("Точка находится в третьей четверти")
elif x > 0 and y < 0:
    print("Точка находится в четвертой четверти")
else:
    print("Точка находится в начале координат")


#5

a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину стороны b: "))
c = float(input("Введите длину стороны c: "))

if a >= b + c or b >= a + c or c >= a + b:
    print("Треугольник с такими сторонами не существует")
else:
    print("Треугольник с такими сторонами существует")

    #6

x = float(input("Введите координату x точки: "))
y = float(input("Введите координату y точки: "))
r = float(input("Введите радиус круга: "))

if x**2 + y**2 <= r**2:
    print("Точка принадлежит кругу")
else:
    print("Точка не принадлежит кругу")

    #7

print("1 - прямоугольник")
print("2 - треугольник")
print("3 - круг")

choice = int(input("Выберите фигуру: "))

if choice == 1:
    a = float(input("Введите длину стороны a: "))
    b = float(input("Введите длину стороны b: "))
    s = a * b
    print("Площадь прямоугольника:", s)
elif choice == 2:
    a = float(input("Введите длину стороны a: "))
    b = float(input("Введите длину стороны b: "))
    c = float(input("Введите длину стороны c: "))
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print("Площадь треугольника:", s)
elif choice == 3:
    r = float(input("Введите радиус круга: "))
    s = 3.14 * r ** 2
    print("Площадь круга:", s)
else:
    print("Ошибка ввода")

    #8
year = int(input("Введите год: "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(year, "- високосный год")
    days = 366
else:
    print(year, "- не високосный год")
    days = 365

print("Количество дней в году:", days)

    #9
distance = float(input("Введите дальность выстрела: "))

if distance >= 28 and distance <= 30:
    print("ПОПАЛ")
elif distance > 30:
    print("ПЕРЕЛЕТ")
elif distance > 0:
    print("НЕДОЛЕТ")
else:
    print("НЕ БЕЙ ПО СВОИМ")

    #10

a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Корней бесконечно много")
        else:
            print("Корней нет")
    else:
        x = -c / b
        print("Корень уравнения:", x)
else:
    d = b**2 - 4 * a * c
    if d > 0:
        x1 = (-b + d**0.5) / (2 * a)
        x2 = (-b - d**0.5) / (2 * a)
        print("Корни уравнения:", x1, x2)
    elif d == 0:
        x = -b / (2 * a)
        print("Корень уравнения:", x)
    else:
        print("Корней нет")


    
