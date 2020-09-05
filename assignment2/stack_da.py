# Course: CS261 - Data Structures
# Student Name: Yesha Jhala
# Assignment: Assignment 2 Part 3 Stack_Da
# Description: Implement a Stack ADT class

from dynamic_array import *


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Stack:
    def __init__(self):
        """
        Init new stack based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "STACK: " + str(self.da.size) + " elements. "
        out += str(self.da.data[:self.da.size])
        return out

# push will add element to top of stack and pop will return the element recently added from stack
    def push(self, value: object) -> None:
        """
        Adds specified element to top of the Stack
        """
        self.da.append(value)

    def pop(self) -> object:
        """
        Removes and returns most recently added element from the Stack
        """
        # handle case where Stack is empty
        if self.da.is_empty():
            raise StackException

        # reference return object with a convenient variable
        return_object = self.da.get_at_index(self.da.size - 1)

        # remove object from top of the stack and return element
        self.da.remove_at_index(self.da.size - 1)
        return return_object

    def top(self) -> object:
        """
        Returns value of top element in Stack
        """
        # handle case where Stack is empty
        if self.da.is_empty():
            raise StackException

        # return highest index element
        return self.da.get_at_index(self.da.size - 1)

    def is_empty(self) -> bool:
        """
        Returns boolean indication of whether Stack is empty
        """
        return self.da.is_empty()

    def size(self) -> int:
        """
        Returns number of elements currently in the Stack
        """
        return self.da.size


# BASIC TESTING
if __name__ == "__main__":
    pass

    # # push example 1
    # s = Stack()
    # print(s)
    # for value in [1, 2, 3, 4, 5]:
    #     s.push(value)
    # print(s)

    # # pop example 1
    # s = Stack()
    # try:
    #     print(s.pop())
    # except Exception as e:
    #     print("Exception:", type(e))
    #
    # for value in [1, 2, 3, 4, 5]:
    #     s.push(value)
    #
    # for i in range(6):
    #     try:
    #         print(s.pop())
    #     except Exception as e:
    #         print("Exception:", type(e))

    # # top example 1
    # s = Stack()
    # try:
    #     s.top()
    # except Exception as e:
    #     print("No elements in stack", type(e))
    # s.push(10)
    # s.push(20)
    # print(s)
    # print(s.top())
    # print(s.top())
    # print(s)

    # # is_empty example 1
    # s = Stack()
    # print(s.is_empty())
    # s.push(10)
    # print(s.is_empty())
    # s.pop()
    # print(s.is_empty())

    # # size example 1
    # s = Stack()
    # print(s.size())
    # for value in [1, 2, 3, 4, 5]:
    #     s.push(value)
    # print(s.size())