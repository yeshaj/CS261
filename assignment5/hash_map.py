# Yesha Jhala
# August 8th, 2020
# CS 261 Assignment 5 Part 1
# Description: This hash map uses a hash table of buckets, each containing a linked list of hash links

from a5_include import *


def hash_function_1(key: str) -> int:
    """
    Sample Hash function #1 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash = 0
    for letter in key:
        hash += ord(letter)
    return hash


def hash_function_2(key: str) -> int:
    """
    Sample Hash function #2 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash, index = 0, 0
    index = 0
    for letter in key:
        hash += (index + 1) * ord(letter)
        index += 1
    return hash


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Init new HashMap based on DA with SLL for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.buckets = DynamicArray()
        for _ in range(capacity):
            self.buckets.append(LinkedList())
        self.capacity = capacity
        self.hash_function = function
        self.size = 0

    def __str__(self) -> str:
        """
        Return content of hash map t in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self.buckets.length()):
            list = self.buckets.get_at_index(i)
            out += str(i) + ': ' + str(list) + '\n'
        return out

    def clear(self) -> None:
        """
        Clears the contents of the HashMap
        """
        # iterate through HashMap.buckets and replace current LL with empty LL
        for index in range(self.capacity):
            self.buckets.set_at_index(index, LinkedList())

        # update size property to zero
        self.size = 0

    def get(self, key: str) -> object:
        """
        Returns the value associated with the given key
        """
        hash_val = self.hash_function(key)
        da_index = hash_val % self.capacity

        if self.buckets.length() == 0:
            return False

        target_ll = self.buckets.get_at_index(da_index)

        if target_ll.contains(key) is None:
            return None

        if target_ll.contains(key) is not None:
            return target_ll.contains(key).value

    def put(self, key: str, value: object) -> None:
        """
        Updates the key / value pair in the HashMap
        """
        hash_val = self.hash_function(key)
        da_index = hash_val % self.capacity

        if self.buckets.get_at_index(da_index).contains(key) is not None:
            self.buckets.get_at_index(da_index).remove(key)
            self.buckets.get_at_index(da_index).insert(key, value)
            return

        if self.buckets.get_at_index(da_index).contains(key) is None:
            self.buckets.get_at_index(da_index).insert(key, value)
            self.size += 1

    def remove(self, key: str) -> None:
        """
        Removes the given key and its associated value from the HashMap
        """
        hash_val = self.hash_function(key)
        da_index = hash_val % self.capacity

        if self.buckets.get_at_index(da_index).remove(key):
            self.size -= 1

    def contains_key(self, key: str) -> bool:
        """
        Returns True if the given key is in the HashMap, False otherwise
        """
        hash_val = self.hash_function(key)
        da_index = hash_val % self.capacity

        if self.buckets.length() == 0:
            return False

        current_ll = self.buckets.get_at_index(da_index)

        if current_ll.contains(key) is None:
            return False

        if current_ll.contains(key) is not None:
            return True

    def empty_buckets(self) -> int:
        """
        Returns the number of empty buckets in the hash table
        """
        count = 0
        for index in range(self.buckets.length()):
            if self.buckets.get_at_index(index).length() == 0:
                count += 1
        return count

    def table_load(self) -> float:
        """
        Returns the current HashMap table load factor
        """
        return float(self.size / self.capacity)

    def resize_table(self, new_capacity: int) -> None:
        """
        Changes the capacity of the internal HashMap table
        """
        if new_capacity < 1:
            return

        new_da = DynamicArray()
        for _ in range(new_capacity):
            new_da.append(LinkedList())

        for index in range(self.capacity):
            current_ll = self.buckets.get_at_index(index)
            for node in current_ll:
                hash_val = self.hash_function(node.key)
                new_da_index = hash_val % new_capacity
                new_da.get_at_index(new_da_index).insert(node.key, node.value)

        self.buckets = new_da
        self.capacity = new_capacity

    def get_keys(self) -> DynamicArray:
        """
        Returns a DynamicArray that contains all keys stored in my HashMap
        """
        return_da = DynamicArray()

        for index in range(self.capacity):
            current_ll = self.buckets.get_at_index(index)
            for node in current_ll:
                return_da.append(node.key)

        return return_da
