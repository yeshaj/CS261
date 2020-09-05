# Course: CS261 - Data Structures
# Student Name: Yesha Jhala
# Assignment: Assignment 2 Part 1 Dynamic_Array
# Description: Implement a Dynamic Array class. Number of objects stored in the array
# at any given time will be between 0 and 100,000 inclusive


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.size = 0
        self.capacity = 4
        self.data = [None] * self.capacity

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self.size) + "/" + str(self.capacity)
        out += " " + str(self.data[:self.size])
        return out

    def resize(self, new_capacity: int) -> None:
        """
        Sets new storage list to given capacity's data attribute that contains same elements in same index
        """
        # if zero or less than the current size then will guard against
        if (new_capacity == 0) or (new_capacity < self.size):
            return

        # new_data will create capacity with use of new_capacity
        new_data = [None] * new_capacity

        for i in range(self.size):
            new_data[i] = self.data[i]

        # capacity and data now set to new capacity and data
        self.capacity = new_capacity
        self.data = new_data

        return

    def append(self, value: object) -> None:
        """
        Will double capacity if the storage is full and adds given value to next index that is free
        """
        # double capacity if storage is full
        if self.is_full():
            self.resize(self.capacity * 2)

        # set the values
        self.data[self.size] = value
        self.size += 1

        return

    def insert_at_index(self, index: int, value: object) -> None:
        """
        If valid index given, inserts the given value into the data
        attribute list at the given index, shifting existing values
        one index higher if necessary, and doubling the data attribute
        list capacity if it is full.  Raises a DynamicArrayException
        if invalid index value given.
        """
        # Guard against invalid index
        if (index < 0) or (index > self.size):
            raise DynamicArrayException

        # Check if storage is full and double capacity if true
        if self.is_full():
            self.resize(self.size * 2)

        # Shift elements to make room at index for the new value.
        # This is a noop if index is appending to the end of the
        # current data attribute list
        for current_index in range(self.size, index, -1):
            self.data[current_index] = self.data[current_index - 1]

        # Set value at the given index and increment size
        self.data[index] = value
        self.size       += 1

        return

    def get_at_index(self, index: int) -> object:
        """
        If valid index given, returns object at the given index
        in the data attribute list. If invalid index is given,
        raises a DynamicArrayException
        """
        # Guard against invalid index
        if (index < 0) or (index > self.size - 1):
            raise DynamicArrayException

        # Return the value at the given index
        return self.data[index]

    def remove_at_index(self, index: int) -> None:
        """
        If given a valid index, removes the value at the index and shifts
        remaining values at indexes higher down one.  If invalid index given
        raises a DynamicArrayException
        """
        # Guard against invalid index
        if (index < 0) or (index > self.size - 1):
            raise DynamicArrayException

        # If current size is less than one quarter of current capacity and
        # the capacity is greater than 10, reduce maximum capacity to either
        # twice the current size if the current size is 5 or more, or reduce
        # to the minimum size of 10
        if (self.size < (0.25 * self.capacity)) and self.capacity > 10:
            if self.size < 5:
                self.resize(10)
            else:
                self.resize(self.size * 2)

        # Iterate the data attribute list starting at the index of the value
        # to be removed and shift the next value into the current index.
        # If iteration has reached the last value set it to None
        for i in range(index, self.size):
            if i == (self.size - 1):
                self.data[i] = None
            else:
                self.data[i] = self.data[i + 1]

        # Decrement size after removing value
        self.size -= 1

        return

    def is_empty(self) -> bool:
        """
        Returns True if data attribute list is empty, False if not
        """
        return self.size == 0

    def length(self) -> int:
        """
        Returns the number of elements in the data attribute list
        """
        return self.size

    def slice(self, start_index: int, quantity: int) -> object:
        """
        If valid start_index and quantity given, returns a new DynamicArray
        object containing the values for the given index segment in the
        data attribute list. If invalid start_index or quantity given,
        raises a DynamicArrayException
        """
        # Guard against invalid start_index
        if (start_index < 0) or (start_index > self.size - 1):
            raise DynamicArrayException

        # Guard against invalid quantity
        if (quantity < 0) or (quantity > (self.size - start_index)):
            raise DynamicArrayException

        # Initialize a new DynamicArray
        new_array = DynamicArray()

        # Iterate the data attribute list starting at the start_index
        # appending the values to the new array until up until the
        # quantity requested (the index before start_index + quantity)
        for i in range(start_index, (start_index + quantity)):
            new_array.append(self.data[i])

        return new_array

    def reverse(self) -> None:
        """
        Reverses the order of the elements in the data attribute list
        """
        # If size is 1 or 0 there is nothing to reverse
        if self.size <= 1:
            return

        # Initialize a front and back pointer
        front_index = 0
        back_index  = self.size - 1

        # While the front pointer is less than half of the current size
        # continue swapping elements from the index of the front pointer
        # with the elements from the index of the back pointer
        while front_index < (self.size / 2):
            # Temporarily store the front and back values to be swapped
            front_val = self.get_at_index(front_index)
            back_val  = self.get_at_index(back_index)

            # Remove and replace front index value with back
            self.remove_at_index(front_index)
            self.insert_at_index(front_index, back_val)

            # Remove and replace back index value with front, either using
            # the append method if target index is at the end of the elements
            # in the data attributes list, or insert_at_index if not at the end
            self.remove_at_index(back_index)
            if back_index == self.size:
                self.append(front_val)
            else:
                self.insert_at_index(back_index, front_val)

            # Iterate the pointers closer to the middle
            front_index += 1
            back_index  -= 1

        return

    def sort(self) -> None:
        """
        Sorts in place the data attribute list from least to most
        using insertion sort
        """
        # If size is less than or equal to one just return
        if self.size <= 1:
            return

        # Begin sorting at index 1
        current_index = 1

        # Work from left to right sorting the data attribute list
        while current_index < self.size:
            # Start comparing with the index just to the left of
            # the current index and set sorting to true
            comparison_index = current_index - 1
            sorting          = True

            # While sorting is still taking place
            while sorting:
                # Set the value of the current index
                current_val = self.get_at_index(current_index)

                # If the current value is less than the value in the
                # comparison index and the comparison index is 0, we
                # have reached the beginning and that is where the
                # current value should be set, removed from it's old
                # position and set sorting to False as we're done
                # with this value
                if current_val < self.get_at_index(comparison_index):
                    if comparison_index == 0:
                        self.remove_at_index(current_index)
                        self.insert_at_index(0, current_val)
                        sorting = False
                    # If the comparison index is not 0, continue checking left
                    else:
                        comparison_index -= 1
                # If the current value is greater than or equal to the
                # value at the comparison index, remove it from it's
                # current index and place it 1 index ahead of the
                # comparison index and set sorting to False
                else:
                    self.remove_at_index(current_index)
                    self.insert_at_index(comparison_index + 1, current_val)
                    sorting = False

            # Increment current index
            current_index += 1

        return

    def merge(self, another_list: object) -> None:
        """
        Appends the given DynamicArray values to the end of the data
        attribute list
        """
        # Iterate the given list values and append
        for i in range(another_list.length()):
            self.append(another_list.get_at_index(i))

        return

    def is_full(self) -> bool:
        """
        Returns True if the data attribute has no free space,
        False if there is free space remaining
        """
        if self.size == self.capacity:
            return True

        return False


# BASIC TESTING
if __name__ == "__main__":
    pass

    #resize - example 1
    da = DynamicArray()
    print(da.size, da.capacity, da.data)
    da.resize(10)
    print(da.size, da.capacity, da.data)
    da.resize(2)
    print(da.size, da.capacity, da.data)
    da.resize(0)
    print(da.size, da.capacity, da.data)

    # # resize - example 2
    # da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    # print(da)
    # da.resize(20)
    # print(da)
    # da.resize(4)
    # print(da)

    # # append - example 1
    # da = DynamicArray()
    # print(da.size, da.capacity, da.data)
    # da.append(1)
    # print(da.size, da.capacity, da.data)
    # print(da)

    # # append - example 2
    # da = DynamicArray()
    # for i in range(9):
    #     da.append(i + 101)
    #     print(da)
    #
    # # append - example 3
    # da = DynamicArray()
    # for i in range(600):
    #     da.append(i)
    # print(da.size)
    # print(da.capacity)

    # # insert_at_index - example 1
    # da = DynamicArray([100])
    # print(da)
    # da.insert_at_index(0, 200)
    # da.insert_at_index(0, 300)
    # da.insert_at_index(0, 400)
    # print(da)
    # da.insert_at_index(3, 500)
    # print(da)
    # da.insert_at_index(1, 600)
    # print(da)

    # # insert_at_index example 2
    # da = DynamicArray()
    # try:
    #     da.insert_at_index(-1, 100)
    # except Exception as e:
    #     print("Exception raised:", type(e))
    # da.insert_at_index(0, 200)
    # try:
    #     da.insert_at_index(2, 300)
    # except Exception as e:
    #     print("Exception raised:", type(e))
    # print(da)

    # # insert at index example 3
    # da = DynamicArray()
    # for i in range(1, 10):
    #     index, value = i - 4, i * 10
    #     try:
    #         da.insert_at_index(index, value)
    #     except Exception as e:
    #         print("Can not insert value", value, "at index", index)
    # print(da)

    # # get_at_index - example 1
    # da = DynamicArray([10, 20, 30, 40, 50])
    # print(da)
    # for i in range(4, -1, -1):
    #     print(da.get_at_index(i))

    # # get_at_index example 2
    # da = DynamicArray([100, 200, 300, 400, 500])
    # print(da)
    # for i in range(-1, 7):
    #     try:
    #         print("Index", i, ": value", da.get_at_index(i))
    #     except Exception as e:
    #         print("Index", i, ": exception occured")

    # # remove_at_index - example 1
    # da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    # print(da)
    # da.remove_at_index(0)
    # print(da)
    # da.remove_at_index(6)
    # print(da)
    # da.remove_at_index(2)
    # print(da)

    # # remove_at_index - example 2
    # da = DynamicArray([1024])
    # print(da)
    # for i in range(17):
    #     da.insert_at_index(i, i)
    # print(da.size, da.capacity)
    # for i in range(16, -1, -1):
    #     da.remove_at_index(0)
    # print(da)

    # # remove_at_index - example 3
    # da = DynamicArray()
    # print(da.size, da.capacity)
    # [da.append(1) for i in range(100)]          # step 1 - add 100 elements
    # print(da.size, da.capacity)
    # [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 69 elements
    # print(da.size, da.capacity)
    # da.remove_at_index(0)                      # step 3 - remove 1 element
    # print(da.size, da.capacity)
    # da.remove_at_index(0)                       # step 4 - remove 1 element
    # print(da.size, da.capacity)
    # [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    # print(da.size, da.capacity)
    # da.remove_at_index(0)                       # step 6 - remove 1 element
    # print(da.size, da.capacity)
    # da.remove_at_index(0)                       # step 7 - remove 1 element
    # print(da.size, da.capacity)
    #
    # for i in range(14):
    #     print("Before remove_at_index(): ", da.size, da.capacity, end="")
    #     da.remove_at_index(0)
    #     print(" After remove_at_index(): ", da.size, da.capacity)

    # # is_empty - example 1
    # da = DynamicArray()
    # print(da.is_empty(), da)
    # da.append(100)
    # print(da.is_empty(), da)
    # da.remove_at_index(0)
    # print(da.is_empty(), da)

    # # length - example 1
    # da = DynamicArray()
    # print(da.length())
    # for i in range(10000):
    #     da.append(i)
    # print(da.length())
    # for i in range(9999, 5000, -1):
    #     da.remove_at_index(i)
    # print(da.length())

    # # slice example 1
    # da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    # da_slice = da.slice(1, 3)
    # print(da, da_slice, sep="\n")
    # da_slice.remove_at_index(0)
    # print(da, da_slice, sep="\n")

    # slice example 2
    # da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    # print("SOUCE:", da)
    # slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3)]
    # for i, cnt in slices:
    #     print("Slice", i, "/", cnt, end="")
    #     try:
    #         print(" --- OK: ", da.slice(i, cnt))
    #     except:
    #         print(" --- exception occurred.")

    # # merge example 1
    # da = DynamicArray([1, 2, 3, 4, 5])
    # da2 = DynamicArray([10, 11, 12, 13])
    # print(da)
    # da.merge(da2)
    # print(da)

    # merge example 2
    # da = DynamicArray([1, 2, 3])
    # da2 = DynamicArray()
    # da3 = DynamicArray()
    # da.merge(da2)
    # print(da)
    # da2.merge(da3)
    # print(da2)
    # da3.merge(da)
    # print(da3)

    # # reverse example 1
    # da = DynamicArray([4, 5, 6, 7, 8, 9])
    # print(da)
    # da.reverse()
    # print(da)
    # da.reverse()
    # print(da)

    # # reverse example 2
    # da = DynamicArray()
    # da.reverse()
    # print(da)
    # da.append(100)
    # da.reverse()
    # print(da)

    # # sort example 1
    # da = DynamicArray([1, 10, 2, 20, 3, 30, 4, 40, 5])
    # print(da)
    # da.sort()
    # print(da)
