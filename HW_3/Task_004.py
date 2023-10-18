import re
from collections import Counter

def count_words(text):
    # Удаление знаков препинания и приведение к нижнему регистру
    cleaned_text = re.sub(r'[^\w\s\']', '', text.lower())
    
    # Разделение строки на слова
    words = re.findall(r'\b\w+\b', cleaned_text)
    
    # Удаление апострофов из слов типа dont, its, didnt итд
    cleaned_words = [word.replace("'", "") for word in words]
    
    # Подсчет частоты встречаемости слов
    word_counts = Counter(cleaned_words)
    
    # Возвращение 10 самых частых слов
    top_10_words = word_counts.most_common(10)
    
    return top_10_words

text = 'Hello world. Hello Python. Hello again.'


result = count_words(text)
print(result)