def check_brackets(s):
    brackets = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for char in s:
        if char in brackets.keys():
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False
    
    return len(stack) == 0

def longest_brackets(s):
    remember = int()
    remember_max = ''
    if check_brackets(s):
        return True
    else:
        for i in range(1, len(s)-1):
            for j in range (i+1, len(s)):
                if check_brackets(s[i:j]):
                    if remember < len(s[i:j]):
                        remember = len(s[i:j])
                        remember_max = s[i:j]
    return remember_max
def main():
    a = input('Введите строку скобок: ')
    print(longest_brackets(a))
if __name__ == "__main__":
    main()
