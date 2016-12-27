# 1   2   3
# 4   5   6
# 7   8   9 

# 7   4   1
# 8   5   2
# 9   6   3

def rotate_matrix(matrix):
    N = len(matrix)
    for layer in range(N // 2):
        start, end = layer, N - layer - 1
        for i in range(start, end):
            top_left = matrix[start][i]
            top_right = matrix[i][end]
            bot_right = matrix[end][-i - 1]
            bot_left = matrix[-i - 1][start]
            
            matrix[start][i] = bot_left
            matrix[i][end] = top_left
            matrix[end][-i - 1] = top_right
            matrix[-i - 1][start] = bot_right

    return matrix

m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16, 17]]
m3 = [[1, 2], [3, 4]]

print(rotate_matrix(m1))
print(rotate_matrix(m2))
print(rotate_matrix(m3))
