a, b, c = map(float, input().split())  # Считываем три вещественных числа - длины  сторон треугольника


def triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        print("Треугольник не существует")
    elif a == b == c:
        print("Треугольник равносторонний")
    elif a == b or a == c or b == c:
        print("Треугольник равнобедренный")
    else:
        print("Треугольник общего вида")


triangle(a, b, c)  # Вызываем функцию, в которой программа решает поставленную задачу
