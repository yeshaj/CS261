# Yesha Jhala
# CS 261
# Assignment 3 Part 1
# Description: Implement Deque and Bag ADT interfaces with a Singly Linked List data structure


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class SLNode:
    """
    Singly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with front and back sentinels
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.head = SLNode(None)
        self.tail = SLNode(None)
        self.head.next = self.tail

        # populate SLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        if self.head.next != self.tail:
            cur = self.head.next.next
            out = out + str(self.head.next.value)
            while cur != self.tail:
                out = out + ' -> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def add_front(self, value: object) -> None:
        """
        Places new node immediately after front sentinel
        """

        new_node = SLNode(value)
        new_node.next = self.head.next
        self.head.next = new_node

    def add_back(self, value: object) -> None:
        """
        Places new node immediately prior to back sentinel
        """

        new_node = SLNode(value)
        new_node.next = self.tail

        insert_after = self.head
        while insert_after.next != self.tail:
            insert_after = insert_after.next

        insert_after.next = new_node

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Inserts new SLNode object at specified index
        """
        if index < 0:
            raise SLLException

        new_node = SLNode(value)

        insert_after = self.head
        for i in range(index):
            if insert_after.next == self.tail:
                raise SLLException
            insert_after = insert_after.next

        new_node.next = insert_after.next
        insert_after.next = new_node

    def remove_front(self) -> None:
        """
        Removes node immediately following LinkedList.head
        """
        if self.head.next == self.tail:
            raise SLLException

        to_remove = self.head.next
        self.head.next = to_remove.next

    def remove_back(self) -> None:
        """
        Removes node immediately prior to LinkedList.tail
        """
        if self.head.next == self.tail:
            raise SLLException

        current = self.head.next
        prior = self.head
        while current.next != self.tail:
            current = current.next
            prior = prior.next

        prior.next = current.next

    def remove_at_index(self, index: int) -> None:
        """
        Removes SLNode at specified index in LinkedList
        """
        if index < 0:
            raise SLLException

        if self.head.next == self.tail:
            raise SLLException

        current = self.head.next
        prior = self.head
        i = 0
        while i != index:
            if current.next == self.tail:
                raise SLLException
            current = current.next
            prior = prior.next
            i += 1

        prior.next = current.next

    def get_front(self) -> object:
        """
        Returns first non-head node value without removal
        """
        if self.head.next == self.tail:
            raise SLLException

        return self.head.next.value

    def get_back(self) -> object:
        """
        Returns last non-tail node value without removal
        """
        if self.head.next == self.tail:
            raise SLLException

        last_node = self.head.next
        while last_node.next != self.tail:
            last_node = last_node.next

        return last_node.value

    def remove(self, value: object) -> bool:
        """
        Removes first node containing value argument and indicates if successful
        """
        if self.head.next == self.tail:
            return False

        current = self.head.next
        prior = self.head
        while current != self.tail and current.value != value:
            current = current.next
            prior = prior.next

        if current == self.tail:
            return False

        prior.next = current.next
        return True

    def count(self, value: object) -> int:
        """
        Counts number of non-head/tail elements that have value property matching argument
        """
        count = 0
        current = self.head
        while current.next != self.tail:
            current = current.next
            if current.value == value:
                count += 1
        return count

    def slice(self, start_index: int, size: int) -> object:
        """
        Returns a new LinkedList based on arguments passed
        """
        if start_index < 0:
            raise SLLException

        if self.head.next == self.tail:
            raise SLLException

        index = 0
        current = self.head.next
        while index != start_index and current.next != self.tail:
            current = current.next
            index += 1

        if index != start_index:
            raise SLLException

        new_LL = LinkedList()
        for count in range(size):
            new_LL.add_back(current.value)
            # handle case where offset is out of range
            if current.next == self.tail and count < size - 1:
                raise SLLException
            current = current.next

        return new_LL

    def is_sorted(self) -> int:
        """
        Indicates whether LinkedList is sorted
        """
        if self.length() < 2:
            return 1

        strictly_ascending = True
        strictly_descending = True
        current = self.head.next
        prior = self.head
        while current.next != self.tail:
            current = current.next
            prior = prior.next
            # handle case where pair of nodes is not strictly ascending
            if current.value <= prior.value:
                strictly_ascending = False
            # handle case where pair of nodes is not strictly descending
            if current.value >= prior.value:
                strictly_descending = False

        # return indicator to user based on findings in while-loop
        if strictly_ascending:
            return 1
        elif strictly_descending:
            return 2
        else:
            return 0

    def length(self) -> int:
        """
        Returns number of non-head/tail nodes in LinkedList
        """
        # iterate through LinkedList while counting each node once
        count = 0
        current = self.head
        while current.next != self.tail:
            current = current.next
            count += 1
        return count

    def is_empty(self) -> bool:
        """
        Indicates whether LinkedList is empty
        """
        if self.head.next == self.tail:
            return True
        else:
            return False
