class Abiturient:
    count = 0  # Статическое поле: счетчик абитуриентов

    def __new__(cls, *args, **kwargs):  # Метод new
        instance = super().__new__(cls)
        Abiturient.count += 1
        return instance

    def __init__(self, last_name, first_name, patronymic, address, phone, grades):
        self.id = Abiturient.count #Уникальный ID
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.address = address
        self.phone = phone
        self.__grades = grades  # Инкапсулированное поле

    def __str__(self): #Магический метод str
        return f"{self.last_name} {self.first_name} (ID: {self.id})"

    def __add__(self, other): #Магический метод сложения
        return sum(self.__grades) + sum(other.__grades)

    def __sub__(self, other): #Магический метод вычитания
        return sum(self.__grades) - sum(other.__grades)

    def __gt__(self, other): #Магический метод сравнения 
        return sum(self.__grades) > sum(other.__grades)

    def __lt__(self, other): #Магический метод сравнения 
        return sum(self.__grades) < sum(other.__grades)

    def get_grades(self): #Getter для оценок
        return self.__grades

    def set_grades(self, new_grades): #Setter для оценок
        if all(0 <= grade <= 100 for grade in new_grades):
            self.__grades = new_grades
        else:
            print("Некорректные оценки")

    @classmethod
    def get_total_abiturients(cls): #Классовый метод
        return cls.count

    @staticmethod
    def is_valid_phone(phone): #Статический метод
        return len(phone) == 10 and phone.isdigit()

    def display_info(self): #Метод объекта
        print(f"ID: {self.id}, ФИО: {self.last_name} {self.first_name} {self.patronymic}, Оценки: {self.__grades}")

    def __del__(self): #Метод del
        Abiturient.count -= 1
        print(f"Абитуриент {self.last_name} удален. Осталось {Abiturient.count}")

#Создаем список абитуриентов
abiturients = []
abiturients.append(Abiturient("Иванов", "Иван", "Иванович", "ул. Ленина, 1", "1234567890", [90, 70, 60]))
abiturients.append(Abiturient("Петров", "Петр", "Петрович", "ул. Мира, 2", "9876543210", [40, 50, 30]))
abiturients.append(Abiturient("Сидоров", "Сидор", "Сидорович", "ул. Победы, 3", "5551234567", [80, 90, 100]))


# Список абитуриентов с неудовлетворительными оценками
bad_grades_list = [abiturient for abiturient in abiturients if any(grade < 60 for grade in abiturient.get_grades())]
print("Абитуриенты с неудовлетворительными оценками:")
for abiturient in bad_grades_list:
    print(abiturient)


# Список абитуриентов с суммой баллов выше заданной
threshold = 200
high_score_list = [abiturient for abiturient in abiturients if sum(abiturient.get_grades()) > threshold]
print(f"Абитуриенты с суммой баллов выше {threshold}:")
for abiturient in high_score_list:
    print(abiturient)