# Course: CS 261 - Data Structures
# Student Name: Yesha Jhala
# Assignment: Assignment 1 Part 2 Min-Max
# Description: Will receive a one dimensional list of integers and return a tuple with two values - minimum and maximum values in the input list


def min_max(arr: []) -> ():
    """
    return tuple with two values - minimum and maximum
    :param arr: one dimensional list of integers
    :return: tuple with min and max
    """
    minimum = 100000
    maximum = - 100000
    j = 0
    for i in arr:
        if i < minimum:
            minimum = i
        if i > maximum:
            maximum = i
        j = j + 1  # increment size counter
    if j != 0:
        return minimum, maximum

    return None, None




#if __name__ == "__main__":    # example 1
#    print(min_max([23, 2, 3, 4, 5]))