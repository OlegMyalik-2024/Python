class Abiturient:
    count = 0 # Статическое поле: счетчик абитуриентов

    def __new__(cls, *args, **kwargs):
        cls.count += 1
        return super().__new__(cls)

    def __init__(self, id, sername, name, middle_name, address, telephone, grades):
        self.id = id
        self.sername = sername
        self.name = name
        self.middle_name = middle_name
        self.address = address
        self.telephone = telephone
        self.__grades = grades  # Инкапсулированное поле

    def __str__(self):
        return f"{self.sername} {self.name} (ID: {self.id}, Оценки: {self.__grades})"

    def get_grades(self):
        return self.__grades

    def set_grades(self, grades):
        if all(isinstance(grade, int) and 1 <= grade <= 5 for grade in grades):
            self.__grades = grades
        else:
            print("Некорректные оценки")

    def average_grade(self):
        return sum(self.__grades) / len(self.__grades)

    def __add__(self, other):
        return self.average_grade() + other.average_grade()

    def __sub__(self, other):
        return self.average_grade() - other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()
    
    def __del__(self):
        Abiturient.count -= 1
        print(f"Абитуриент {self.sername} удален.")

    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod
    def telephone_check(telephone):
        return len(telephone) == 11 and telephone.startswith('8')

# Пример реализации
abiturients = [
    Abiturient(1, "Иванов", "Иван", "Иванович", "ул. Ленина, 33", "+375297734556", [10, 9, 8, 7]),
    Abiturient(2, "Петров", "Петр", "Петрович", "ул. Мира, 26", "+375253456734", [2, 3, 8, 4]),
    Abiturient(3, "Колесников", "Иван", "Сергеевич", "ул. Победы, 34", "+375445554433", [5, 10, 1, 5])
]

#Список студентов с неудовлетворительными оценками
bad_grades = [a for a in abiturients if any(grade <= 3 for grade in a.get_grades())]
print("Абитуриенты с неудами:", [str(a) for a in bad_grades])
#Список студентов у которых средний балл равен определенному значению
point = 5.0
value = [a for a in abiturients if a.average_grade() > point]
print(f"Абитуриенты с баллом выше {point}:", [str(a) for a in value])
#Удаление студентов
print(f"Общее количество абитуриентов: {Abiturient.get_count()}")
del abiturients[0]
