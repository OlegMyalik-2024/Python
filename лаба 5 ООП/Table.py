class Table:
    __mass = 0

    def __init__(self, mass0):
        self.__mass = mass0

    # чтение инкапсулированной массы
    def get_mass(self):
        return self.__mass

# журнальный стол
class JournalTable(Table):
    storage = 0

    def __init__(self, mass0):
        super().__init__(mass0)
        self.storage = mass0 // 10  # Пример: количество полок в журнальном столе

# обеденный стол
class DinnerTable(Table):
    __places = 0

    def __init__(self, mass0):
        super().__init__(mass0)
        self.__places = mass0 // 5  # Пример: количество мест за столом

    # чтение инкапсулированного числа мест
    def get_places(self):
        return self.__places

class Truck:
    __maxMass = 0
    __tables = []

    def __init__(self, max_mass):
        self.__maxMass = max_mass
        self.__tables = []

    # Метод для добавления стола в грузовик
    def add_table(self, table):
        if self.get_total_mass() + table.get_mass() <= self.__maxMass:
            self.__tables.append(table)
            print(f"Стол добавлен. Текущая масса: {self.get_total_mass()} кг")
        else:
            print("Невозможно добавить стол: превышена максимальная грузоподъемность.")

    # Метод для получения общей массы всех столов в грузовике
    def get_total_mass(self):
        return sum(table.get_mass() for table in self.__tables)

    # Метод для вывода информации о загруженных столах
    def show_tables(self):
        journal_count = sum(isinstance(table, JournalTable) for table in self.__tables)
        dinner_count = sum(isinstance(table, DinnerTable) for table in self.__tables)
        print(f"Журнальных столов: {journal_count}, Обеденных столов: {dinner_count}")
        print(f"Общая масса: {self.get_total_mass()} кг")

# Грузовик с максимальной грузоподъемностью 100 кг
truck = Truck(100)  

# Создаем несколько столов
table1 = JournalTable(30)  
table2 = DinnerTable(10)   
table3 = JournalTable(25)  
table4 = DinnerTable(50)   

# Добавляем столы в грузовик
truck.add_table(table1)
truck.add_table(table2)
truck.add_table(table3)
truck.add_table(table4)  

# Выводим информацию о загруженных столах
truck.show_tables()