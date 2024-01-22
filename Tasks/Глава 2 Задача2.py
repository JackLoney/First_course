def reverse_word_order(string):
    # Разделение строки на список слов и удаление пустых элементов
    words = string.split()
    # Обратное упорядочивание списка слов и объединение в строку через пробел
    reversed_string = ' '.join(words[::-1])
    reversed_string = reversed_string.capitalize()
    return reversed_string

# Примеры использования
print(reverse_word_order("пРиВет мИР"))       # Output: "Мир привет"
print(reverse_word_order("  it       was     cool     "))  # Output: "Cool was it"
print(reverse_word_order("good"))             # Output: "Good"
