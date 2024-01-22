from collections import defaultdict

def group_strings(strings):
    groups = defaultdict(list)  # Словарь для хранения групп

    # Группируем слова по наборам букв и размерности
    for word in strings:
        key = (frozenset(word), len(word))
        groups[key].append(word)

    # Преобразуем словарь с группами в список списков
    result = [group for group in groups.values()]

    return result

# Примеры использования
def main():
    strings = ["qwe", "ewq", "asd", "dsa", "dsas", "qwee", "zxc", "cxz", "xxz", "z", "s", "qweasdzxc", "zzxc"]
    output = group_strings(strings)
    print(output)
    
    strings = ["a", "a", ""]
    output = group_strings(strings)
    print(output)
if __name__ == "__main__":
    main()
