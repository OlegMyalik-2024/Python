# 1. Используя функцию map() переписать функцию
# items = [1, 2, 3, 4, 5]
# squared = []
# for i in items:
#     squared.append(i**2)
print("----------------------------------Задание №1--------------------------------------")
# Исходный список элементов
items = [1, 2, 3, 4, 5]
squared = []
# Функция для возведения в квадрат каждого элемента списка
def square(x):
    return x**2
#Используем метод map и преобразовываем в список
squared = list(map(square, items))
print("Новый список: ", squared)
print("----------------------------------------------------------------------------------")


# 2.Используйте функцию reduce() и перепишите код
# product = 1
# list = [1, 2, 3, 4]
# for num in list:
#     product = product * num
print("----------------------------------Задание №2--------------------------------------")
#Импортируем из модуля functools функцию reduce
from functools import  reduce
# Исходные данные
product = 1
list1 = [1, 2, 3, 4]
#Используем функцию reduce
new_list=reduce(lambda num, product: product * num, list1)
print("Ответ равен: ", new_list)
print("----------------------------------------------------------------------------------")


# 3.Используйте функцию map() и перепишите код
# numbers = [1, 2, 3, 4, 5]
# squared = []
# for num in numbers:
#        squared.append(num ** 2)
# print(squared)
print("----------------------------------Задание №3--------------------------------------")
# Исходный список чисел
items = [1, 2, 3, 4, 5]
squared = []
#Используем лямбда-функцию
squared = list(map(lambda x: x **2 , items))
print("Новый список = ", squared)
print("----------------------------------------------------------------------------------")


# 4.Объедините списки x = [1, 2, 3] и y = [4, 5, 6] с помощью функции zip()
print("----------------------------------Задание №4--------------------------------------")
# Исходные списки элементов
x = [1, 2, 3]
y = [4, 5, 6]
#Используем zip() функцию для объединения списков
res=list(zip(x,y))
print("Результат: ", res)
print("----------------------------------------------------------------------------------")


# 5.Используйте функцию zip() чтобы преобразовать код:
#
# name_hero = [
#     'Hulk',
#     'Mr. Fantastic',
#     'Invisible Woman',
#     'Doctor Strange',
#     'Doctor Octopus',
#     'Spider-Man',
# ]
#
# name_real = [
#     'Bruce Banner',
#     'Reed Richards',
#     'Sue Storm',
#     'Stephen Strange',
#     'Otto Octavius',
#     'Peter Parker',
# ]
#
# for i in range(len(name_hero)):
#     print(name_hero[i], '-', name_real[i])
print("----------------------------------Задание №5--------------------------------------")
# Исходные списки элементов
name_hero = ['Hulk', 'Mr. Fantastic', 'Invisible Woman', 'Doctor Strange', 'Doctor Octopus', 'Spider-Man']
name_real = ['Bruce Banner', 'Reed Richards', 'Sue Storm', 'Stephen Strange', 'Otto Octavius', 'Peter Parker',]
#Используем zip() функцию для объединения списков
hero_list=list(zip(name_hero,name_real))
#Используя map() функцию выводим список
hero_list = list(map(lambda n: print(n), hero_list))
print(hero_list)
print("----------------------------------------------------------------------------------")


#С помощью функции filter() переместите из списка numbers = [1, 2, 4, 5, 7, 8, 10, 11]
# нечетные элементы в новый список.
print("----------------------------------Задание №6--------------------------------------")
# Исходный список элементов
numbers = [1, 2, 4, 5, 7, 8, 10, 11]
#Используем filter() функцию для перемещения нечетных элементов в новый список
res_list=list(filter(lambda x: x%2!=0, numbers))
print(res_list)
print("----------------------------------------------------------------------------------")