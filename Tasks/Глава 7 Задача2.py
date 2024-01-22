def roman_to_arabic(s):
    Slovarik = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0

    for i in range(len(s)):
        if i > 0 and Slovarik[s[i]] > Slovarik[s[i - 1]]:
            result += Slovarik[s[i]] - 2 * Slovarik[s[i - 1]]
        else:
            result += Slovarik[s[i]]

    return result



s = "MCMXCIV"
result = roman_to_arabic(s)
print(result)
