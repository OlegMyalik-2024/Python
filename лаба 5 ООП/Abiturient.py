class Abiturient:
    #Статическое поле для подсчета id
    id = 1

    def __init__(self, surname, name, middle_name, address, telephone, marks):
        self.id = Abiturient.id
        Abiturient.id += 1
        self.surname = surname
        self.name = name
        self.middle_name = middle_name
        self.address = address
        self.telephone = telephone
        #Инкапсулированное поле
        self.__marks = marks  

    #Метод объекта для получения оценок
    def get_marks(self):
        return self.__marks

    #Метод объекта для установки оценок с проверкой корректности
    def set_marks(self, marks):
        if all(isinstance(mark, int) and 0 <= mark <= 10 for mark in marks):
            self.__marks = marks
        else:
            raise ValueError("Оценки должны быть целыми числами от 0 до 10")

    #Статический метод для проверки, есть ли неудовлетворительные оценки
    @staticmethod
    def abiturient_marks(marks):
        return any(mark < 4 for mark in marks)

    #Метод класса для создания списка абитуриентов с неудовлетворительными оценками
    @classmethod
    def abiturient_list(cls, abiturients):
        return [a for a in abiturients if cls.abiturient_marks(a.get_marks())]

    # Метод для проверки суммы баллов
    def abiturient_sum(self, value):
        return sum(self.__marks) > value

# Пример использования
abiturients = [
    Abiturient("Иванов", "Иван", "Иванович", "г. Минск, ул. Бобруйская, д. 18. кв. 45", "+375336674521", [5, 3, 6, 1]),
    Abiturient("Петров", "Петр", "Петрович", "г. Брест, ул. Советская, д. 23, кв. 88", "+375298265634", [10, 7, 8, 9]),
    Abiturient("Сидоров", "Анатолий", "Сергеевич", "г. Ивацевичи, ул. Клютко, д. 22", "+375297725634", [2, 4, 5, 3]),
    Abiturient("Колесников", "Александр", "Александрович", "г. Могилев, ул. Первомайская, д. 45, кв. 127", "+375291232465", [7, 6, 4, 4]),
    Abiturient("Гайдук", "Елена", "Анатольевна", "г. Гродно, ул. Ленина, д. 67, кв. 56", "+375333369987", [5, 6, 10, 3, 2])
]
#Задание 1
#Список абитуриентов с неудовлетворительными оценками
list_marks = Abiturient.abiturient_list(abiturients)
print("Неудовлетворительные оценки:", [a.surname  for a in list_marks])

#Задание 2
#Список абитуриентов с суммой баллов выше 16
list_sum = [a for a in abiturients if a.abiturient_sum(16)]
print("Сумма баллов выше 12:", [a.surname for a in list_sum])