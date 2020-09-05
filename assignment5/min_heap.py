# Yesha Jhala
# August 8th, 2020
# CS 261 Assignment 5 Part 2
# Description: Use a dynamic array to implement the complete binary tree heap in which the value in each internal node
# is smaller than or equal to the values in the children of that node.


from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """
        Adds a new object to the MinHeap maintaining heap property
        """
        self.heap.append(node)

        if self.heap.length() == 1:
            return

        child = self.heap.length() - 1
        parent = (child - 1) // 2
        while self.heap.get_at_index(parent) > self.heap.get_at_index(child) and child != 0:
            self.heap.swap(parent, child)
            child = parent
            parent = (child - 1) // 2

    def get_min(self) -> object:
        """
        Returns an object with a minimum key without removing it from the heap
        """
        if self.heap.length() == 0:
            raise MinHeapException

        return self.heap.get_at_index(0)

    def remove_min(self) -> object:
        """
        Returns an object with a minimum key and removes it from the heap
        """
        if self.heap.length() == 0:
            raise MinHeapException

        self.heap.swap(0, self.heap.length() - 1)
        return_node = self.heap.pop()

        if self.heap.length() == 0:
            return return_node

        p_index = 0
        p_value = self.heap.get_at_index(p_index)
        c1_index = 1
        c2_index = 2
        min_ind = self.min_index(c1_index, c2_index)
        min_val = self.heap.get_at_index(min_ind)

        # loop through tree swapping replacement node with appropriate children
        while not self.out_range(c1_index, c2_index) and p_value > min_val:
            self.heap.swap(p_index, min_ind)
            p_index = min_ind
            p_value = self.heap.get_at_index(p_index)
            c1_index = (2 * p_index) + 1
            c2_index = (2 * p_index) + 2
            min_ind = self.min_index(c1_index, c2_index)
            min_val = self.heap.get_at_index(min_ind)

        # MinHeap has been re-organized, so return original min value
        return return_node

    def build_heap(self, da: DynamicArray) -> None:
        """
        Receives a DynamicArray with objects in any order and builds a proper MinHeap from them
        """
        da2 = DynamicArray()
        for index in range(da.length()):
            da2.append(da.get_at_index(index))

        if da2.length() < 2:
            self.heap = da2
            return

        count = 0
        root_bool = False

        # outer loop should continue until root element has been percolated down
#        while root_bool == False:
        while not root_bool:
            if count == 0:
                p_outer_index = ((da2.length() // 2) - 1)
            else:
                p_outer_index = p_outer_index - 1

            if p_outer_index == 0:
                root_bool = True

            p_index = p_outer_index
            p_value = da2.get_at_index(p_index)
            c1_index = (2 * p_outer_index) + 1
            c2_index = (2 * p_outer_index) + 2
            min_ind = self.min_index_da(c1_index, c2_index, da2)
            min_val = da2.get_at_index(min_ind)

            count += 1

            # loop through tree percolating element down until we take care of the root
            while not self.out_range_da(c1_index, c2_index, da2) and p_value > min_val:
                da2.swap(p_index, min_ind)
                p_index = min_ind
                p_value = da2.get_at_index(p_index)
                c1_index = (2 * p_index) + 1
                c2_index = (2 * p_index) + 2
                min_ind = self.min_index_da(c1_index, c2_index, da2)
                min_val = da2.get_at_index(min_ind)

        self.heap = da2

    # Helper Functions #

    def min_index_da(self, index_1: int, index_2: int, da: object) -> int:
        """
        Returns index with minimum value from two indices
        """
        if index_1 > da.length() - 1 and index_2 < da.length():
            return index_2

        if index_2 > da.length() - 1 and index_1 < da.length():
            return index_1

        if index_2 > da.length() - 1 and index_1 > da.length() - 1:
            return 0

        # define convenient variables to make code more readable
        value_1 = da.get_at_index(index_1)
        value_2 = da.get_at_index(index_2)

        # determine which value to return
        if value_1 < value_2:
            return index_1
        return index_2

    def out_range_da(self, index_1: int, index_2: int, da: object) -> bool:
        """
        Indicates whether both indices are out of range
        """
        if index_1 > da.length() - 1 and index_2 > da.length() - 1:
            return True
        return False

    def min_index(self, index_1: int, index_2: int) -> int:
        """
        Returns index with minimum value from two indices
        """
        if index_1 > self.heap.length() - 1 and index_2 < self.heap.length():
            return index_2

        if index_2 > self.heap.length() - 1 and index_1 < self.heap.length():
            return index_1

        if index_2 > self.heap.length() - 1 and index_1 > self.heap.length() - 1:
            return 0

        value_1 = self.heap.get_at_index(index_1)
        value_2 = self.heap.get_at_index(index_2)

        if value_1 < value_2:
            return index_1
        return index_2

    def out_range(self, index_1: int, index_2: int) -> bool:
        """
        Indicates whether both indices are out of range
        """
        if index_1 > self.heap.length() - 1 and index_2 > self.heap.length() - 1:
            return True
        return False