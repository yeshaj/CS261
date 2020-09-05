# Course: CS261 - Data Structures
# Student Name: Yesha Jhala
# Assignment: Assignment 2 Part 2 Bag_Da
# Description: Implement a Bag ADT class

from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of bag in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self.da.size) + " elements. "
        out += str(self.da.data[:self.da.size])
        return out

    def add(self, value: object) -> None:
        """
        Add element to the bag
        """
        self.da.append(value)

    def remove(self, value: object) -> bool:
        """
        Will remove element from bag
        """
        # remove elements if found after iterating bag
        for index in range(self.da.size):
            if self.da.data[index] == value:
                self.da.remove_at_index(index)
                return True

        # if object was not found and removed then return false
        return False

    def count(self, value: object) -> int:
        """
        Will count objects through bag
        """
        # iterate through elements manually and count elements matching value
        count = 0
        for index in range(self.da.size):
            if self.da.data[index] == value:
                count += 1

        return count

    def clear(self) -> None:
        """
        Clear the contents of the Bag
        """
        for index in range(self.da.size - 1, -1, -1):
            self.da.remove_at_index(index)

    def size(self) -> int:
        """
        Return the number of elements currently in the Bag
        """
        return self.da.size

    def equal(self, second_bag: object) -> bool:
        """
        Indicates whether the current Bag is equal to the second Bag object
        """
        # handle case where size of bags differs
        if self.size() != second_bag.size():
            return False

        # iterate through elements in self and determine whether they exist in second_bag
        for index_1 in range(self.size()):
            exists = False
            index_2 = 0
            while exists == False and index_2 < second_bag.size():
                if self.da.data[index_1] == second_bag.da.data[index_2]:
                    exists = True
                else:
                    index_2 += 1

            if not exists:
                return False

        # all tests have passed, so return True
        return True


# BASIC TESTING
if __name__ == "__main__":
    pass

    # # add example 1
    # bag = Bag()
    # print(bag)
    # values = [10, 20, 30, 10, 20, 30]
    # for value in values:
    #     bag.add(value)
    # print(bag)

    # # remove example 1
    # bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    # print(bag)
    # print(bag.remove(7), bag)
    # print(bag.remove(3), bag)
    # print(bag.remove(3), bag)
    # print(bag.remove(3), bag)
    # print(bag.remove(3), bag)

    # # count example 1
    # bag = Bag([1, 2, 3, 1, 2, 2])
    # print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))

    # # clear example 1
    # bag = Bag([1, 2, 3, 1, 2, 3])
    # print(bag)
    # bag.clear()
    # print(bag)

    # # size example 1
    # bag = Bag([10, 20, 30, 40])
    # print(bag.size(), bag.remove(30), bag.size())
    # bag.clear()
    # print(bag.size())

    # # equal example 1
    # bag1 = Bag([1, 2, 3, 4, 5, 6])
    # bag2 = Bag([6, 5, 4, 3, 2, 1])
    # bag3 = Bag([1, 2, 3, 4, 5])
    # bag_empty = Bag()
    #
    # print(bag1, bag2, bag3, bag_empty, sep="\n")
    # print(bag1.equal(bag2), bag2.equal(bag1))
    # print(bag1.equal(bag3), bag3.equal(bag1))
    # print(bag2.equal(bag3), bag3.equal(bag2))
    # print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    # print(bag_empty.equal(bag_empty))
    # print(bag1, bag2, bag3, bag_empty, sep="\n")