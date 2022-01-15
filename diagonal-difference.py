def diagonalDifference(arr):
    # Find out dimensions of matrix.
    rows = len(arr)
    columns = len(arr[0])
    matrix_dimension = rows % columns
    diagonal_1 = [arr[i][i] for i in range(len(arr))]
    diagonal_2 = [arr[i][len(arr) - i - 1] for i in range(len(arr))]
    print("Rows: {}, Columns: {} and Matrix Dimension".format(rows, columns, matrix_dimension))
    print("Diagonal - 1: {}".format(diagonal_1))
    print("Diagonal - 2: {}".format(diagonal_2))
    return abs(sum(diagonal_1) - sum(diagonal_2))

print(diagonalDifference([[1,2,3], [4,5,6], [9,8,9]]))