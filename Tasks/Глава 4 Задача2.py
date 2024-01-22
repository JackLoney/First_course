def permute(nums):
    results = []
    backtrack(nums, [], results)
    return results

def backtrack(nums, current, results):
    # Если текущая перестановка содержит все элементы из исходного списка, добавляем ее в результаты
    if len(current) == len(nums):
        results.append(current[:])
    else:
        # Рекурсивно генерируем все возможные перестановки, начиная с текущей позиции
        for num in nums:
            if num not in current:
                current.append(num)
                backtrack(nums, current, results)
                current.pop()
def main():
    # Чтение списка целых чисел из строки ввода
    nums = list(map(int, input().strip().split()))
    
    # Генерация всех возможных перестановок
    permutations = permute(nums)
    
    # Вывод результатов
    for p in permutations:
        print(p)
if __name__ == "__main__":
    main()
