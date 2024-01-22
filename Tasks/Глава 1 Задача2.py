def reverse_8bit(num: str):
    if num < 0:
        num_without = str(-num)
    else:
        num_without = str(num)
    reversed_num = int(num_without[::-1]) # Переворачиваем значение

    if int(num) < 0: # Если исходное число отрицательное, меняем знак перевернутого числа
        reversed_num = -reversed_num
    
    if reversed_num < -128 or reversed_num > 127:
        return "no solution"
    
    return reversed_num
def main():
    num = int(input("Введите целое число со знаком: "))
    print(reverse_8bit(num))
if __name__ == "__main__":
    main()
