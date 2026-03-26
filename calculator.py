def add(a, b):
    return a + b

def substract(a, b):
    return a - b

if __name__ == "__main__":
    print("Простой калькулятор")
    print("Сложить 5 + 3 =", add(5, 3))
    print("Вычитание 10 - 4 =", substract(10, 4))

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Ошибка: Деление на ноль!"
    return a / b

print("Умножение 6 * 7 =", multiply(6, 7))
print("Деление 15 / 3 =", divide(15, 3))
