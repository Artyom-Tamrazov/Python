"""
    /   - Деление с остатком
    //  - Целочисленное деление
    %   - Остаток от деления
        1. Остаток не может стать больше Делителя
        2. Если Делитель больше Делимого, то результатом будет Делитель
"""
"""
Дано трёхзначное число, необходимо найти сумму его цифр.
Пример: 123 => 6
"""

num = int(input())
a = num // 100
b = num // 10 % 10
c = num % 10
print(a + b + c)
