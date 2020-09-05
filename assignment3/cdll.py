# Yesha Jhala
# CS 261
# Assignment 3 Part 2
# Description: Implementation of a circular doubly linked list


class CDLLException(Exception):
    """
    Custom exception class to be used by Circular Doubly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DLNode:
    """
    Doubly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        self.next = None
        self.prev = None
        self.value = value


class CircularList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with sentinel
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.sentinel = DLNode(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

        # populate CDLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'CDLL ['
        if self.sentinel.next != self.sentinel:
            cur = self.sentinel.next.next
            out = out + str(self.sentinel.next.value)
            while cur != self.sentinel:
                out = out + ' <-> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def add_front(self, value: object) -> None:
        """
        Immediately after the sentinel, it will add a new node
        """
        # set prev/next properties to the new node
        new_node = DLNode(value)
        new_node.prev = self.sentinel
        new_node.next = self.sentinel.next

        self.sentinel.next = new_node
        new_node.next.prev = new_node

    def add_back(self, value: object) -> None:
        """
        Immediately before the sentinel, it will add a new node
        """
        # set prev/next properties to the new node
        new_node = DLNode(value)
        new_node.prev = self.sentinel.prev
        new_node.next = self.sentinel

        self.sentinel.prev = new_node
        new_node.prev.next = new_node

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Will insert new node at specified index in CircularList
        """
        # handle the cases if index is less than 0
        if index < 0:
            raise CDLLException

        current = self.sentinel
        count = 0
        while count != index:
            current = current.next
            count += 1
            if current == self.sentinel:
                raise CDLLException

        new_node = DLNode(value)
        new_node.next = current.next
        new_node.prev = current

        current.next = new_node
        new_node.next.prev = new_node

    def remove_front(self) -> None:
        """
        Node will be removed immediately following the sentinel
        """

        if self.sentinel.next == self.sentinel:
            raise CDLLException

        self.sentinel.next.next.prev = self.sentinel
        self.sentinel.next = self.sentinel.next.next

    def remove_back(self) -> None:
        """
        Node will be removed immediately prior to the sentinel
        """
        if self.sentinel.next == self.sentinel:
            raise CDLLException

        self.sentinel.prev.prev.next = self.sentinel
        self.sentinel.prev = self.sentinel.prev.prev

    def remove_at_index(self, index: int) -> None:
        """
        Removes node at indicated index
        """
        if index < 0:
            raise CDLLException

        current = self.sentinel
        count = 0
        while count != index:
            current = current.next
            count += 1
            if current.next == self.sentinel:
                raise CDLLException

        current.next.next.prev = current
        current.next = current.next.next

    def get_front(self) -> object:
        """
        Value of node returned immediately following the sentinel
        """
        # handle case where CircularList is empty
        if self.sentinel.next == self.sentinel:
            raise CDLLException

        return self.sentinel.next.value

    def get_back(self) -> object:
        """
        Value of node returned immediately prior to the sentinel
        """
        # handle case where CircularList is empty
        if self.sentinel.next == self.sentinel:
            raise CDLLException

        return self.sentinel.prev.value

    def remove(self, value: object) -> bool:
        """
        Removes first node with matching value property
        """
        if self.sentinel.next == self.sentinel:
            return False

        node_to_remove = self.sentinel.next
        index = 0
        while node_to_remove.value != value and node_to_remove != self.sentinel:
            node_to_remove = node_to_remove.next
            index += 1

        if node_to_remove == self.sentinel:
            return False

        self.remove_at_index(index)
        return True

    def count(self, value: object) -> int:
        """
        Counts number of nodes with value property matching value argument
        """

        count = 0
        current = self.sentinel
        while current.next != self.sentinel:
            current = current.next
            if current.value == value:
                count += 1
        return count

    def slice(self, start_index: int, size: int) -> object:
        """
        Returns a new CircularList that is a subset of the current CircularList
        """
        if start_index < 0 or start_index > self.length() - 1:
            raise CDLLException

        if start_index + size - 1 > self.length() - 1:
            raise CDLLException

        if self.sentinel.next == self.sentinel:
            raise CDLLException

        current = self.sentinel.next
        index = 0
        while index != start_index:
            current = current.next
            index += 1

        new_CL = CircularList()
        for count in range(size):
            new_CL.add_back(current.value)
            current = current.next
        return new_CL

    def is_sorted(self) -> int:
        """
        Indicates whether CircularList node´s value properties are strictly
        ascending or descending
        """
        if self.length() < 2:
            return 1

        strictly_ascending = True
        strictly_descending = True
        current = self.sentinel.next.next
        prior = self.sentinel.next
        while current != self.sentinel:
            # handle case where prior and current are not strictly ascending
            if current.value <= prior.value:
                strictly_ascending = False

            # handle case where prior and current are not strictly descending
            if current.value >= prior.value:
                strictly_descending = False

            # iterate to next set of adjacent nodes
            current = current.next
            prior = prior.next

        if strictly_ascending:
            return 1
        elif strictly_descending:
            return 2
        else:
            return 0

    def swap_pairs(self, index1: int, index2: int) -> None:
        """
        Swaps two nodes located at different indices
        """
        if self.is_empty():
            raise CDLLException

        if index1 < 0 or index1 > self.length() - 1:
            raise CDLLException

        if index2 < 0 or index2 > self.length() - 1:
            raise CDLLException

        if index1 == index2:
            return

        # iterate through list in search of nodes to swap
        node_1 = self.sentinel.next
        node_1_index = 0
        node_2 = self.sentinel.next
        node_2_index = 0
        node_1_found = False
        node_2_found = False
        while not (node_1_found and node_2_found):
            if not node_1_found and node_1_index != index1:
                node_1 = node_1.next
                node_1_index += 1
            if not node_1_found and node_1_index == index1:
                node_1_found = True
            if not node_2_found and node_2_index != index2:
                node_2 = node_2.next
                node_2_index += 1
            if not node_2_found and node_2_index == index2:
                node_2_found = True

        # handle case where node_1.next == node_2
        if node_1.next == node_2:
            node_1.next = node_2.next
            node_2.prev = node_1.prev
            node_2.next = node_1
            node_1.prev = node_2
            node_2.prev.next = node_2
            node_1.next.prev = node_1

        # handle case where node_2.next == node_1
        elif node_2.next == node_1:
            node_2.next = node_1.next
            node_1.prev = node_2.prev
            node_1.next = node_2
            node_2.prev = node_1
            node_1.prev.next = node_1
            node_2.next.prev = node_2

        # handle case where node_1 and node_2 are not adjacent
        else:
            # remove node_1 from CircularList and point both pointers to its previous
            node_1.prev.next = node_1.next
            node_1.next.prev = node_1.prev
            node_1.next = node_1.prev

            # remove node_2 from CircularList and point both pointers to its previous
            node_2.prev.next = node_2.next
            node_2.next.prev = node_2.prev
            node_2.next = node_2.prev

            # swap prev pointers for both nodes
            node_1.prev = node_2.prev
            node_2.prev = node_1.next

            # swap next pointers for both nodes
            node_1.next = node_1.prev
            node_2.next = node_2.prev

            # re-insert node_1 into the list where node_2 used to live
            node_1.next = node_1.next.next
            node_1.next.prev = node_1
            node_1.prev.next = node_1

            # re-insert node_2 into the list where node_1 used to live
            node_2.next = node_2.next.next
            node_2.next.prev = node_2
            node_2.prev.next = node_2

    def reverse(self) -> None:
        """
        Reverses the order of the nodes in a CircularList
        """
        # create convenient variables to reference nodes to swap and their indices
        node_1 = self.sentinel.next
        node_2 = self.sentinel.prev
        index_1 = 0
        index_2 = self.length() - 1

        # iterate through Circular list swapping nodes until nodes converge
        while index_1 < index_2:
            new_node_1 = node_1.next
            new_node_2 = node_2.prev

            # handle case where node_1.next == node_2
            if node_1.next == node_2:
                node_1.next = node_2.next
                node_2.prev = node_1.prev
                node_2.next = node_1
                node_1.prev = node_2
                node_2.prev.next = node_2
                node_1.next.prev = node_1

            # handle case where node_2.next == node_1
            elif node_2.next == node_1:
                node_2.next = node_1.next
                node_1.prev = node_2.prev
                node_1.next = node_2
                node_2.prev = node_1
                node_1.prev.next = node_1
                node_2.next.prev = node_2

            # handle case where node_1 and node_2 are not adjacent
            else:
                # remove node_1 from CircularList and point both pointers to its previous
                node_1.prev.next = node_1.next
                node_1.next.prev = node_1.prev
                node_1.next = node_1.prev

                # remove node_2 from CircularList and point both pointers to its previous
                node_2.prev.next = node_2.next
                node_2.next.prev = node_2.prev
                node_2.next = node_2.prev

                # swap prev pointers for both nodes
                node_1.prev = node_2.prev
                node_2.prev = node_1.next

                # swap next pointers for both nodes
                node_1.next = node_1.prev
                node_2.next = node_2.prev

                # re-insert node_1 into the list where node_2 used to live
                node_1.next = node_1.next.next
                node_1.next.prev = node_1
                node_1.prev.next = node_1

                # re-insert node_2 into the list where node_1 used to live
                node_2.next = node_2.next.next
                node_2.next.prev = node_2
                node_2.prev.next = node_2

            # iterate to next set of nodes to swap and update indices
            node_1 = new_node_1
            node_2 = new_node_2
            index_1 += 1
            index_2 -= 1

    def sort(self) -> None:
        """
        Sorts the CircularList in non-descending order
        """
        if self.length() < 2:
            return

        outer_loop = self.length() - 1
        while outer_loop > 0:
            inner_loop = 0
            current = self.sentinel.next
            following = current.next
            while inner_loop < outer_loop:
                if following.value < current.value:
                    current.next = following.next
                    following.prev = current.prev
                    following.next = current
                    current.prev = following
                    current.next.prev = current
                    following.prev.next = following
                    following = current.next
                    inner_loop += 1
                else:
                    current = following
                    following = current.next
                    inner_loop += 1

            outer_loop -= 1

    def length(self) -> int:
        """
        Returns number of nodes in CircularList
        """
        count = 0
        current = self.sentinel
        while current.next != self.sentinel:
            current = current.next
            count += 1
        return count

    def is_empty(self) -> bool:
        """
        Indicates whether CircularList has zero non-sentinel nodes
        """
        return self.sentinel.next == self.sentinel

