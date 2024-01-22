def reverse_8bit(num: str):

    num_without = str(-num)
    reversed_num = int(num_without[::-1]) # Переворачиваем значение

    if int(num) < 0: # Если исходное число отрицательное, меняем знак перевернутого числа
        reversed_num = -reversed_num
    
    if reversed_num < -128 or reversed_num > 127:
        return "no solution"
    

    return reversed_num

num = int(input("Введите целое число со знаком: "))
print(reverse_8bit(num))
