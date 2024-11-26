
def rectangle(a, b, squares):
    if a == 0 or b == 0:
        return print("Сторона квадрата не может равняться нулю. Введите значение стороны больше 0!!!")
    # Определяем размер максимального квадрата
    side = min(a, b)
    # Добавляем квадрат в список
    squares.append(side)
    # Рекурсивный вызов для оставшейся части
    if a > b:
        rectangle(a - side, b, squares)
    else:
        rectangle(a, b - side, squares)


a = int(input("Введите размер стороны a прямоугольника: "))
b = int(input("Введите размер стороны b прямоугольника: "))
squares = []
rectangle(a, b, squares)

print("Полученные квадраты: ", squares)
print("Количество полученных квадратов: ", len(squares))