# Course: CS261 - Data Structures
# Student Name: Yesha Jhala
# Assignment: Assignment 2 Part 4 Queue_Da
# Description: Implement a Queue ADT class

from dynamic_array import *


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Init new queue based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "QUEUE: " + str(self.da.size) + " elements. "
        out += str(self.da.data[:self.da.size])
        return out

    def enqueue(self, value: object) -> None:
        """
        Adds specified object to the end of the Queue
        """
        self.da.append(value)

    def dequeue(self) -> object:
        """
        Removes and returns value from beginning of the Queue
        """
        # handle case where Queue is empty
        if self.da.is_empty():
            raise QueueException

        # reference first element of the Queue, remove element, and return the element
        beginning_element = self.da.get_at_index(0)
        self.da.remove_at_index(0)
        return beginning_element

    def is_empty(self) -> bool:
        """
        Indicates whether Queue is empty
        """
        return self.da.is_empty()

    def size(self) -> int:
        """
        Returns number of elements in Queue
        """
        return self.da.size


# BASIC TESTING
if __name__ == "__main__":
    pass

    # # enqueue example 1
    # q = Queue()
    # print(q)
    # for value in [1, 2, 3, 4, 5]:
    #     q.enqueue(value)
    # print(q)

    # # dequeue example 1
    # q = Queue()
    # for value in [1, 2, 3, 4, 5]:
    #     q.enqueue(value)
    # print(q)
    # for i in range(6):
    #     try:
    #         print(q.dequeue())
    #     except Exception as e:
    #         print("No elements in queue", type(e))

    # # is_empty example 1
    # q = Queue()
    # print(q.is_empty())
    # q.enqueue(10)
    # print(q.is_empty())
    # q.dequeue()
    # print(q.is_empty())

    # # size example 1
    # q = Queue()
    # print(q.size())
    # for value in [1, 2, 3, 4, 5, 6]:
    #     q.enqueue(value)
    # print(q.size())