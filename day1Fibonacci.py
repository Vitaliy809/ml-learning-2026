n = int(input("Введіть число для функції Фібоначі:"))

def fibonacci(n):
    if n == 0:
        return []
    
    if n <= 1:
        return[0]
    
    fib = [0,1]

    for i in range(2,n):
        new_number = fib[i-1] + fib[i-2]
        fib.append(new_number)
    return fib

print(fibonacci(n))