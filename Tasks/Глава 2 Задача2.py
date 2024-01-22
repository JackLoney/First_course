def reverse_word_order(string):
    # Разделение строки на список слов и удаление пустых элементов
    words = string.split()
    # Обратное упорядочивание списка слов и объединение в строку через пробел
    reversed_string = ' '.join(words[::-1])
    reversed_string = reversed_string.capitalize()
    return reversed_string

def main():
    a = input()
    print(reverse_word_order(a))
if __name__ == "__main__":
    main()
