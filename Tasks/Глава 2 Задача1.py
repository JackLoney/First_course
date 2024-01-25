def longest_substring(string):
    # Инициализируем переменные
    longest = ""
    remember = ""

    # Проходимся по каждому символу в строке
    for letter in string:
        # Если символ уже встречался, обновляем remember
        if letter in remember:
            remember = remember[remember.index(letter) + 1:]

        # Добавляем текущий символ в remember
        remember += letter

        # Обновляем longest, если remember длиннее
        if len(remember) > len(longest):
            longest = remember

    return print(longest)

def main():
    Word = input()
    longest_substring(Word)
if __name__ == "__main__":
    main()
