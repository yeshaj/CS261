# Yesha Jhala
# CS 261
# Assignment 3 Part 3
# Description: Implementation of a stack built off of a singly linked list structure, and keep track of max value of stack for O(1) getter method.


from sll import *


class StackException(Exception):
    """
    Custom exception to be used by MaxStack Class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MaxStack:
    def __init__(self):
        """
        Init new MaxStack based on Singly Linked Lists
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.sll_val = LinkedList()
        self.sll_max = LinkedList()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "MAX STACK: " + str(self.sll_val.length()) + " elements. "
        out += str(self.sll_val)
        return out

    def push(self, value: object) -> None:
        """
        Adds node containing value to top of the stack
        """
        self.sll_val.add_front(value)

        if self.sll_max.is_empty():
            self.sll_max.add_front(value)

        current_max = self.sll_max.get_front()
        if value > current_max:
            self.sll_max.add_front(value)
        else:
            self.sll_max.add_front(current_max)

    def pop(self) -> object:
        """
        Removes top element from stack and returns its value
        """
        if self.sll_val.is_empty():
            raise StackException

        self.sll_max.remove_front()

        top_value = self.sll_val.get_front()
        self.sll_val.remove_front()
        return top_value

    def top(self) -> object:
        """
        Returns value of the top of the stack in a non-destructive manner
        """
        if self.sll_val.is_empty():
            raise StackException

        return self.sll_val.get_front()

    def is_empty(self) -> bool:
        """
        Indicates whether MaxStack is empty
        """
        return self.sll_val.is_empty()

    def size(self) -> int:
        """
        Returns the number of elements in the MaxStack
        """
        return self.sll_val.length()

    def get_max(self) -> object:
        """
        Returns maximum value currently stored in MaxStack
        """
        if self.is_empty():
            raise StackException

        return self.sll_max.get_front()

