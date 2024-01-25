def roman_to_arabic(s):
    Roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0

    for i in range(len(s)):
        if i > 0 and Roman[s[i]] > Roman[s[i - 1]]:
            result += Roman[s[i]] - 2 * Roman[s[i - 1]]
        else:
            result += Roman[s[i]]

    return result

def main():
    s = input()
    result = roman_to_arabic(s)
    print(result)
if __name__ == "__main__":
    main()
