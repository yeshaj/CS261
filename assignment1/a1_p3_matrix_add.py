# Course: CS 261 - Data Structures
# Student Name: Yesha Jhala
# Assignment: Assignment 1 Part 3 Matrix Addition
# Description: Will receive two two-dimensional matrices and return the result when they are added together.
# If matrices have different dimensions, the function should return None.


def matrix_add(a: [[]], b: [[]]) -> [[]]:
    """
    add the two matrices together and return result
    :param a: 2 dimensional matrix
    :param b: 2 dimensional matrix
    :return: the result when added together
    """

    # create a zero matrix
    matrix = [[0] * len(a[m]) for m in range(len(a))]

    # this will check if matrix a and matrix b are going to have the same length
    if len(a) == len(b):

        # set if both are equal number of rows otherwise false
        output = [True if len(row_m1) == len(row_m2) else False for row_m1 in b for row_m2 in a]

        # if the outputs are true for all
        if all(output):
            for i in range(0, len(a)):
                for j in range(0, len(a[i])):
                    matrix[i][j] = a[i][j] + b[i][j]
            return matrix
        else:
            return None
        # will return None if different lengths for both matrices
    else:
        return None


#if __name__ == "__main__" :
#    m1 = [[1, 2, 3], [2, 3, 4]]  # input lists

#    m2 = [[5, 6, 7], [8, 9, 10]]

#    m3 = [[1, 2], [3, 4], [5, 6]]

#    print(matrix_add(m1, m2))

#    print(matrix_add(m1, m3))

#    print(matrix_add(m1, m1))

#    print(matrix_add([[]], [[]]))

#    print(matrix_add([[]], m1))