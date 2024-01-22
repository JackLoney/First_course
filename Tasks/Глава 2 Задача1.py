def longest_substring(string):
    # Инициализируем переменные
    longest = ""
    zapomnim = ""

    # Проходимся по каждому символу в строке
    for bukva in string:
        # Если символ уже встречался, обновляем zapomnim
        if bukva in zapomnim:
            zapomnim = zapomnim[zapomnim.index(bukva) + 1:]

        # Добавляем текущий символ в zapomnim
        zapomnim += bukva

        # Обновляем longest, если zapomnim длиннее
        if len(zapomnim) > len(longest):
            longest = zapomnim

    return print(longest)

def main():
    Slovo = input()
    longest_substring(Slovo)
if __name__ == "__main__":
    main()
