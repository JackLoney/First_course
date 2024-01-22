def get_pins(observed):
    neighbors = {'1': ['1', '2', '4'], '2': ['1', '2', '3', '5'], '3': ['2', '3', '6'],
                 '4': ['1', '4', '5', '7'], '5': ['2', '4', '5', '6', '8'], '6': ['3', '5', '6', '9'],
                 '7': ['4', '7', '8'], '8': ['5', '7', '8', '9', '0'], '9': ['6', '8', '9'], '0': ['0', '8']}
    result = []

    for digit in observed:
        if digit in neighbors:
            result.append(neighbors[digit])

    combinations = [""]
    for digits in result:
        new_combinations = []
        for digit in digits:
            for combination in combinations:
                new_combinations.append(combination + digit)
        combinations = new_combinations

    return combinations
def main():
    a = input()
    print(get_pins(a))
if __name__ == "__main__":
    main()
