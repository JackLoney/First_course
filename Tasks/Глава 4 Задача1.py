def find_closest_sum(nums, target):
    nums.sort()
    n = len(nums)
    closest_sum = float('inf')
    closest_combination = []

    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            left = j + 1
            right = n - 1
            while left < right:
                current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                if current_sum == target:
                    return [nums[i], nums[j], nums[left], nums[right]]
                elif abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                    closest_combination = [nums[i], nums[j], nums[left], nums[right]]

                if current_sum < target:
                    left += 1
                else:
                    right -= 1

    return closest_combination



n = int(input("Введите количество элементов в списке: "))
nums = list(map(int, input("Введите целочисленный список длины N: ").split()))
target = int(input("Введите цель: "))

result = find_closest_sum(nums, target)
if result:
    print(result)
    print(sum(result))
else:
    print("Нет комбинации чисел, близкой к цели")

