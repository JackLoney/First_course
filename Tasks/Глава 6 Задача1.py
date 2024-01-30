def analyze_lists(list1, list2):

    common = list(set(list1) & set(list2))
    
    extra = list(set(list1) ^ set(list2))

    Extraction_list1 = list(set(list1) - set(list2))

    Extraction_list2 = list(set(list2) - set(list1))

    return common, extra, Extraction_list1, Extraction_list2

def main():
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    
    a, b, c, d = analyze_lists(list1, list2)
    print(f'Количество элементов, присутствующих в обоих списках "{len(a)}": {a}')
    print(f'Количество элементов, присутствующих только в одном списке "{len(b)}": {b}') 
    print(f'Количество оставшихся элементов в list1 после извлечения элементов из list2 "{len(c)}": {c}')
    print(f'Количество оставшихся элементов в list2 после извлечения элементов из list1 "{len(d)}": {d}')
if __name__ == "__main__":
    main()
