def check_brackets(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()

    return len(stack) == 0

def longest_valid_substring(s):
    stack = []
    start = 0
    max_length = 0
    longest_substring = None

    for i, char in enumerate(s):
        if char in '({[':
            stack.append(i)
        elif stack:
            stack.pop()
            if stack:
                length = i - stack[-1]
            else:
                length = i - start + 1

            if length > max_length:
                max_length = length
                longest_substring = s[start:i+1]
        else:
            start = i + 1

    return longest_substring if longest_substring else False
def main():
    s = input("Введите строку скобок: ")
    if check_brackets(s):
            print("True")
    else:
        longest_substring = longest_valid_substring(s)
        if longest_substring:
            print(longest_substring)
        else:
            print("False")
if __name__ == "__main__":
    main()
