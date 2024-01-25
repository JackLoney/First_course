def Turn_matrix(matrix):
    n = len(matrix[0])
    result = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            result[j][n-i-1] = matrix[i][j]
    
    return result

def main():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(Turn_matrix(matrix))  # [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    print(Turn_matrix(matrix))  # [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
if __name__ == "__main__":
    main()
