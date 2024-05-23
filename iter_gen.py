"""
BY ISMAILOV SARVARBEK N47 GROUP
"""


# ITERATOR

# Fibonacci raqamlarini yaratish uchun iterator klassi yaratamiz.
class FibonacciIterator:
    def __init__(self, max_value=None):
        self.a, self.b = 0, 1
        self.max_value = max_value

    def __iter__(self):  # Iterator ob'ektining o'zini qaytaradi.
        return self

    def __next__(self):  # Fibonacci raqamlarini ketma-ketlikda qaytaradi.
        if self.max_value is not None and self.a > self.max_value:
            raise StopIteration
        ret = self.a
        self.a, self.b = self.b, self.a + self.b
        return ret


# Fibonacci raqamlarini chop etish.
fibonacci = FibonacciIterator(100)  # Iteratorni 100 gacha bo'lgan qiymatda olish. Qiymat ixtiyoriy kiritilishi mumkin.
for num in fibonacci:
    print(num)


# GENERATOR
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# Generatorni yaratamiz
fib_gen = fibonacci_generator()

# Fibonacci raqamlarini chop etamiz
for i in fib_gen:
    print(next(fib_gen))


# .send()
def countdown(start):
    current = start
    while current > 0:
        received = (yield current)
        current = received if received is not None else current - 1


gen = countdown(15)
print(next(gen))
print(gen.send(10))
print(next(gen))
print(gen.send(8))
print(next(gen))


# .throw
def my_generator():
    while True:
        try:
            received = yield
            print("Received:", received)
        except ValueError as e:
            print("ValueError received:", e)


gen = my_generator()
next(gen)  # Generatorni boshlaymiz

# .throw() metodi orqali ValueError yuboramiz
gen.throw(ValueError("Oops!"))  # "Oops!" ni chop etadi

# Keyingi qiymatni generatsiya qilishi uchun qaytadan .send() ni ishlatamiz
gen.send("Hello")  # "Hello" ni chop etadi

gen.close()  # generatorni yopadi
print(next(gen))