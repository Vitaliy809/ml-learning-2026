# n = int(input("Введіть число для функції Фібоначі:"))

# def fibonacci(n):
#     if n == 0:
#         return []
    
#     if n <= 1:
#         return[0]
    
#     fib = [0,1]

#     for i in range(2,n):
#         new_number = fib[i-1] + fib[i-2]
#         fib.append(new_number)
#     return fib

# print(fibonacci(n))


# def is_prime(n):
    # if n < 2:
    #     return False
    # if n == 2:
    #     return True
    # if n % 2 == 0:
    #     return False
    
    # for i in range(3, int(n**0.5) + 1, 2):
    #     if n % i == 0:
    #         return False
    
#     return True

# # Тести
# print(is_prime(2))   # True
# print(is_prime(7))   # True
# print(is_prime(10))  # False
# print(is_prime(13))  # True
# print(is_prime(9))   # False


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def fizzbuzz_prime(n):
    for i in range(1, n + 1):       # перебираємо всі числа
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        elif is_prime(i):            # is_prime — окрема функція
            print("Prime")
        else:
            print(i)

n = int(input("Введіть число: "))
fizzbuzz_prime(n)

