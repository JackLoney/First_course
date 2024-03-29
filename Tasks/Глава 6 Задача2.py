def Subset_main(nums):
    n = len(nums)
    count = 0
    subsets = []

    # Генерируем все подмножества
    for i in range(1, 2**n):
        subset = []
        for j in range(n):
            if (i & (1 << j)) > 0:
                subset.append(nums[j])
        subsets.append(subset)

    # Подсчитываем количество подмножеств без повторяющихся элементов
    for subset in subsets:
        if len(subset) == len(set(subset)):
            count += 1

    return count, subsets

def main():
    list = [1, 2, 3, 4]
    count, subsets = Subset_main(list)
    print("Подмножества:", subsets)
    print("Количество подмножеств:", count)
if __name__ == "__main__":
    main()
