text = input("Enter text: ")

def word_count(text):
    count_word = 0
    for i in text.split():
        count_word +=  1
    return count_word

def unique_words(text):
    list_unique_words = []
    for i in text.split():
        if i not in list_unique_words:
            list_unique_words.append(i)
    return len(list_unique_words)

def popular_word(text):
    count_word = {}
    max_count = 0
    popular_in_text_word = ""
    for i in text.split():
        if i not in count_word:
            count_word[i] = 1
        else:
              count_word[i] += 1
    for key, value in count_word.items(): 
        if value > max_count:
            max_count = value
            popular_in_text_word = key
    return popular_in_text_word

def average_lenght(text):
    count = []
    sum_word = 0
    for i in text.split():
        count.append(len(i))
    for i in count:
        sum_word += i
    result = sum_word / word_count(text)
    return result

def count_sentence(text):
    count = 0
    for i in text:
        if i == ".":
            count += 1
    return count
    
print(f"Слів всього: {word_count(text)}")
print(f"Унікальних слів: {unique_words(text)}")
print(f"Найчастіше слово: '{popular_word(text)}'")
print(f"Середня довжина: {average_lenght(text):.1f}")
print(f"Кількість речень: {count_sentence(text)}")


        
        
