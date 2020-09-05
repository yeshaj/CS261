# Course: CS 261 - Data Structures
# Student Name: Yesha Jhala
# Assignment: Assignment 1 Part 1 Divisibility
# Description: Will receive 4 integers (​m, n, a, b​) and for each number in the range [​m,n​] (inclusive), it will determine whether it is divisible by ​a​, ​b​, both, or neither.
# It will then return the result as a list of string


def length(s: str) -> int:
    """
    return the length of the string
    """
    count = 0
    for i in s:
        count += 1
    return count


def is_divisible(m: int, n: int, a: int, b: int) -> []:
    """
    will check if a and b are divisible by m and n
    :param m: starting point of the range
    :param n: ending point of the range
    :param a: check if divisible by a
    :param b: check if divisible by b 
    """
    if m > n or a == b or a < 0 or b < 0 or m < 0 or n < 0:
        return "Incorrect input"
    else:
        answer = []
    answer.append("Num\tDiv by " + str(a) + " and/or " + str(b) + "?")
    answer.append("---\t-------------------")
    for i in range(n, m - 1, -1) :
        if (i % a == 0 and i % b == 0) :
            answer.append(str(i) + "\t" + "both")
        elif (i % a == 0) :
            answer.append(str(i) + "\t" + "div by " + str(a))
        elif (i % b == 0) :
            answer.append(str(i) + "\t" + "div by " + str(b))
        else :
            answer.append(str(i) + "\t" + "None")
    return answer

# if __name__ == "__main__":
# example 1
#        print(*is_divisible(2, 7, 2, 3), sep="\n")
#        print(*is_divisible(3,28,6,4),sep="\n")
# example 2
#        print(is_divisible(1, 20, -1, 3))
#        print(is_divisible(20, 0, 100, 200))
#        print(is_divisible(10, 8, 7, 2))
#        print(is_divisible(3, 30, 7, 7))
