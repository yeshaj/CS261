# Yesha Jhala
# CS 261
# Assignment 3 Part 4
# Description: Implementation of the Two-Stack Queue ADT class. Also using MaxStack ADT for Queue ADT


from max_stack_sll import *


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Init new Queue based on two stacks
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.s1 = MaxStack()  # use as main storage
        self.s2 = MaxStack()  # use as temp storage

    def __str__(self) -> str:
        """
        Return content of queue in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "QUEUE: " + str(self.s1.size()) + " elements. "
        out += str(self.s1)
        return out

    def enqueue(self, value: object) -> None:
        """
        Adds new node immediately after the head of the LinkedList
        """
        self.s1.push(value)

    def dequeue(self) -> object:
        """
        Removes and returns the value from the beginning of the queue
        """
        if self.s1.is_empty():
            raise QueueException

        value = None
        while not self.s1.is_empty():
            value = self.s1.pop()
            self.s2.push(value)

        self.s2.pop()

        while not self.s2.is_empty():
            temp = self.s2.pop()
            self.s1.push(temp)

        return value

    def is_empty(self) -> bool:
        """
        Indicates whether the Queue is empty (no elements)
        """
        if self.s1.is_empty():
            return True
        else:
            return False

    def size(self) -> int:
        """
        Returns the number of elements in the Queue
        """
        return self.s1.size()
