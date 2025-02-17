class TribonacciSequence:
    
    # Итерируемый объект, возвращающий генератор чисел Трибоначчи.
    def __init__(self, n=35):  
        self.n = n

    def __iter__(self):
        
        # Возвращает генератор чисел Трибоначчи.
        a, b, c = 0, 1, 1  # Начальные значения последовательности

        for _ in range(self.n):
            yield a  # Возвращает текущее значение
            a, b, c = b, c, a + b + c  # Обновляет значения для следующей итерации

# Создаем экземпляр итерируемого объекта
tribonacci = TribonacciSequence()

# Выводим числа Трибоначчи, итерируясь по объекту
for num in tribonacci:
    print(num, end="; ")