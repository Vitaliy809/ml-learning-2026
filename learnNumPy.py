import numpy as np

# numbers = np.array([3, 7, 2, 9, 1, 5])

# print(numbers)
# print(type(numbers))      # що це за тип?
# print(numbers.shape)      # розмір масиву
# print(numbers.dtype)      # тип даних всередині

# # Математика без циклів:
# print(numbers * 2)        # кожен елемент * 2
# print(numbers + 10)       # кожен елемент + 10
# print(np.mean(numbers))   # середнє
# print(np.max(numbers))    # максимум


a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

print(a + b)
print(a * b)
print(a ** 2)
print(np.mean(b))
print(np.sum(a))
