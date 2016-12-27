def zero_matrix(matrix):
    zero_rows = {}
    zero_cols = {}
    for r, row in enumerate(matrix):
        for c, ele in enumerate(row):
            if ele == 0:
                zero_rows[r] = r
                zero_cols[c] = c

    row_len = len(matrix[0])
    col_len = len(matrix)
    for r in zero_rows:
        for c in range(0, row_len):
            matrix[r][c] = 0

    for c in zero_cols:
        for r in range(0, col_len):
            matrix[r][c] = 0

    return matrix

m1 = [[0, 1, 1], [1, 1, 0], [1, 1, 1]]
res1 = [[0, 0, 0], [0, 0, 0], [0, 1, 0]]

print(zero_matrix(m1) == res1)
