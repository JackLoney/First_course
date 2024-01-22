def Palindrome(num):
    str_num = str(num)
    reverse_str_num = str_num[::-1]
    return str_num == reverse_str_num

num = int(input("Введите целое число: "))
print(Palindrome(num))
