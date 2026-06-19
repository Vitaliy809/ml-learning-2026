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


# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def fizzbuzz_prime(n):
#     for i in range(1, n + 1):       # перебираємо всі числа
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         elif is_prime(i):            # is_prime — окрема функція
#             print("Prime")
#         else:
#             print(i)

# n = int(input("Введіть число: "))
# fizzbuzz_prime(n)



# numbers = [3, 7, 2, 9, 1, 5]
# max_number = 0

# for i in numbers:
   
#     if i > max_number:
#         max_number = i

# print(max_number)


# numbers = [1, 2, 3, 4, 5]

# new_list = []
# for i in range(len(numbers) - 1, -1, -1):
#     new_list.append(numbers[i])  

# print(new_list)

# numbers = [1, 2, 2, 3, 1, 4, 3]
# new_list = []
# for i in numbers:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)


# numbers = [3, 7, 2, 9, 1, 5]
# sum_numbers = 0
# average_numbers = 0
# count = 0
# for i in numbers:
#     sum_numbers += i
#     count += 1
#     average_numbers = sum_numbers / count
    
    
# print(average_numbers)


   
    
# numbers = [3, 7, 2, 9, 1, 5]
# max_numbers = 0


# for i in numbers:
#     if max_numbers < i:
#         max_numbers = i

# second_max = 0
# for i in numbers:
#     if i != max_numbers and i > second_max:
#         second_max = i
# print(second_max)

# word_enter = input("Enter word is Palindrom: ")

# def palindrom_check(word):
#     reversed_list = []
#     for i in range(len(word) - 1, -1, -1):
#         reversed_list.append(word[i])
    
#     reversed_word = "".join(reversed_list)
#     return reversed_word == word  # True або False

# print(palindrom_check(word_enter))
    


# grades = [5, 3, 4, 5, 2, 3, 5, 4, 3, 2]

# grades_student = {}

# for i in grades: 
#     if i not in grades_student:
#         grades_student[i] = 1
#     else:
#         grades_student[i] += 1

# print(grades_student)


# data = {"a": 1, "b": 2, "c": 3}    
# new_data = {}

# for key, value in data.items():
#     new_data[value] = key


# print(new_data)


# text = "apple banana apple orange banana apple"

# count_word = {}
# popular_word = ""
# max_count = 0


# for i in text.split():
#     if i not in count_word:
#         count_word[i] = 1
#     else:
#         count_word[i] += 1

# for key, value in count_word.items():
#     if value > max_count:
#         max_count = value
#         popular_word = key

# print(popular_word)


# numbers = [3, 7, 2, 9, 1, 5]


# def get_min(numbers):
#     result = numbers[0]
#     for i in numbers:
#         if i < result:
#             result = i
#     return result



# def get_max(numbers):
#     result = numbers[0]
#     for i in numbers:
#         if i > result:
#             result = i
#     return result
            

# def get_range(numbers):
#     range_element = get_max(numbers) - get_min(numbers)
#     return range_element

# print(get_min(numbers))
# print(get_max(numbers))
# print(get_range(numbers))


# word = input("Введи слово: ")
# word2= input("Введи слово анаграму до першого: ")

# def anagram(word, word1):
#     word_anagram1 = []
#     word_anagram2 = []
#     for i in word:
#         word_anagram1.append(i)
#     for i in word2:
#         word_anagram2.append(i)
#     anagram_boolean = sorted(word_anagram1) == sorted(word_anagram2)
#     if anagram_boolean == True:
#         return "це анаграма"
#     else:
#         return "це не анаграма"

# print(anagram(word,word2))


# def anagram(word, word1):
#     return sorted(word) == sorted(word1)


# class Stack:
#     def __init__(self):
#         self.data = []

#     def push(self, item):
#         self.data.append(item)
    
#     def pop(self):
#         return self.data.pop()

#     def peek(self):
#         return self.data[-1]

#     def is_empty(self):   
#         return len(self.data) == 0  
#     def size(self):
#         return len(self.data)
    
# s = Stack()
# s.push(1)
# s.push(2)
# s.push(3)
# print(s.pop()) 
# print(s.peek())  
# print(s.size())  


class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)
    
    def peek(self):
        return self.data[0]
    
    def is_empty(self):
        return len(self.data) == 0
    
    def size(self):
        return len(self.data)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  # 1 (перший!)
print(q.peek())     # 2
print(q.size())     # 2  
        



        

    

    


    

        

    

        
    


        


    


