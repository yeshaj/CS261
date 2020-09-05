# Course: CS 261 - Data Structures
# Student Name: Yesha Jhala
# Assignment: Assignment 1 Part 4 Swap Pairs
# Description: Will receive a one dimensional list of integers and a return a new list of the same length where pairs of elements are swapped
# (a[0] swapped with a[1], a[2]swapped with a[3] etc).


def swap_pairs(arr: []) -> []:
    """
    takes integer and returns new integer with each swapped pair
    :param arr: the array of integers
    :return: swapped pairs and the new integers
    """
    if not arr:
        return []
    new_array = list(arr)
    length = len(new_array)
    for i in range(0, length, 2):
        if i == length - 1:
            break
        else:
            temp = new_array[i]
            new_array[i] = new_array[i + 1]
            new_array[i + 1] = temp
            return new_array
