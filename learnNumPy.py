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


# a = np.array([1, 2, 3, 4, 5])
# b = np.array([10, 20, 30, 40, 50])

# print(a + b)
# print(a * b)
# print(a ** 2)
# print(np.mean(b))
# print(np.sum(a))



# matrix = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])

# print(matrix.shape)
# print(matrix[0])
# print(matrix[:,1])
# print(matrix[0,1])
# print(np.sum(matrix))


# numbers = np.array([3, 7, 2, 9, 1, 5, 8, 4])

# mask = numbers > 4
# mask2 = numbers % 2 == 0

# print(numbers[mask])
# print(numbers[mask2])
# print(np.sum(mask))

# np.zeros(5)           # [0. 0. 0. 0. 0.]
# np.ones(5)            # [1. 1. 1. 1. 1.]
# np.arange(0, 10, 2)   # [0 2 4 6 8] — як range()
# np.linspace(0, 1, 5)  # [0. 0.25 0.5 0.75 1.] — рівні проміжки
# np.random.randint(0, 10, 5)  # 5 випадкових чисел від 0 до 10


# print(np.zeros(5))
# print(np.arange(0,22,2))
# print(np.linspace(0,1,6))
# array = np.random.randint(1,100,5)
# print(array)
# print(np.mean(array))

# array = np.arange(1,10)
# matrix = array.reshape(3,3)

# print(array.shape)
# print(matrix.shape)
# print(np.sum(matrix, axis=1))
# print(np.sum(matrix, axis=0))


grades = np.array([
    [85, 92, 78],
    [90, 88, 95],
    [70, 75, 80],
    [95, 98, 92]
])
mask = grades > 90
averages = np.mean(grades, axis=1)
best = np.argmax(averages)  


print(grades.shape)
print(np.mean(grades, axis = 1))
print(np.mean(grades, axis=0))
print(grades[mask])
print(f"Найкращий студент: #{best + 1}")
