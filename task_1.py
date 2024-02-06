def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 1:
            return n
        if n in cache:
            return cache[n]
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
        return cache[n]
    return fibonacci

# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(5))  # Виведе 55
print(fib(8))  # Виведе 610