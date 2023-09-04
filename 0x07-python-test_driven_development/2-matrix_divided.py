#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Return a new matrix with items divided by div
    """
    new_mat = []
    ncol = []
    length = len(matrix[0])
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    for row in matrix:
        if length != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for item in row:
            if type(item) not in [int, float]:
                raise TypeError("matrix must be a matrix"
                                "(list of lists) of integers/floats")
            ncol.append(round(item / div, 2))
        new_mat.append(ncol.copy())
        ncol.clear()
    return (new_mat)

if __name__ == '__main__':
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
