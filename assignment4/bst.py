# Course: CS261 - Data Structures
# Student Name: Yesha Jhala
# Assignment: Assignment 4
# Description: Implementation of the binary search tree


class Stack:
    """
    Class implementing STACK ADT.
    Supported methods are: push, pop, top, is_empty
    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """

    def __init__(self):
        """ Initialize empty stack based on Python list """
        self._data = []

    def push(self, value: object) -> None:
        """ Add new element on top of the stack """
        self._data.append(value)

    def pop(self) -> object:
        """ Remove element from top of the stack and return its value """
        return self._data.pop()

    def top(self) -> object:
        """ Return value of top element without removing from stack """
        return self._data[-1]

    def is_empty(self):
        """ Return True if the stack is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "STACK: { " + ", ".join(data_str) + " }"


class Queue:
    """
    Class implementing QUEUE ADT.
    Supported methods are: enqueue, dequeue, is_empty
    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """

    def __init__(self):
        """ Initialize empty queue based on Python list """
        self._data = []

    def enqueue(self, value: object) -> None:
        """ Add new element to the end of the queue """
        self._data.append(value)

    def dequeue(self) -> object:
        """ Remove element from the beginning of the queue and return its value """
        return self._data.pop(0)

    def is_empty(self):
        """ Return True if the queue is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "QUEUE { " + ", ".join(data_str) + " }"


class TreeNode:
    """
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value  # to store node's data
        self.left = None  # pointer to root of left subtree
        self.right = None  # pointer to root of right subtree

    def __str__(self):
        return str(self.value)


class BST:
    def __init__(self, start_tree=None) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of BST in human-readable form using in-order traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self.root, values)
        return "TREE in order { " + ", ".join(values) + " }"

    def _str_helper(self, cur, values):
        """
        Helper method for __str__. Does in-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # base case
        if cur is None:
            return
        # recursive case for left subtree
        if cur.left:
            self._str_helper(cur.left, values)
        # store value of current node
        values.append(str(cur.value))
        # recursive case for right subtree
        if cur.right:
            self._str_helper(cur.right, values)

    def add(self, value: object) -> None:
        """
        Inserts value property of new node into binary search tree
        """
        if self.root is None:
            self.root = TreeNode(value)
            return

        child = self.root
        parent = None

        while child is not None:
            parent = child
            if value < child.value:
                child = child.left
            else:
                child = child.right

        if value < parent.value:
            parent.left = TreeNode(value)
        else:
            parent.right = TreeNode(value)

    def contains(self, value: object) -> bool:
        """
        Indicates whether value is present
        """
        current = self.root
        while current is not None:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right

        return False

    def get_first(self) -> object:
        """
        Returns value stored at root node
        """
        if self.root is None:
            return None

        return self.root.value

    def remove(self, value: object) -> bool:
        """
        Removes first node with value property matching value argument
        """
        left_bool = False
        node_found = False
        parent = None
        to_remove = self.root
        while to_remove is not None and not node_found:
            if value == to_remove.value:
                node_found = True
            elif value < to_remove.value:
                parent = to_remove
                to_remove = to_remove.left
                left_bool = True
            else:
                parent = to_remove
                to_remove = to_remove.right
                left_bool = False

        if not node_found:
            return False

        if to_remove == self.root:
            self.remove_first()
            return True

        if self.is_leaf(to_remove) and left_bool:
            parent.left = None
            return True
        if self.is_leaf(to_remove) and not left_bool:
            parent.right = None
            return True

        if to_remove.right is None and left_bool:
            parent.left = to_remove.left
            return True
        if to_remove.right is None and not left_bool:
            parent.right = to_remove.left
            return True

        left_bool_2 = False
        replace_node = to_remove.right
        replace_parent = to_remove
        while replace_node.left is not None:
            replace_parent = replace_node
            replace_node = replace_node.left
            left_bool_2 = True

        if left_bool_2:
            replace_parent.left = replace_node.right
        if not left_bool_2:
            replace_parent.right = replace_node.right

        if left_bool:
            parent.left = replace_node
            replace_node.left = to_remove.left
            replace_node.right = to_remove.right
            return True
        if not left_bool:
            parent.right = replace_node
            replace_node.left = to_remove.left
            replace_node.right = to_remove.right
            return True

    def remove_first(self) -> bool:
        """
        Removes root node from BST
        """
        if self.root is None:
            return False

        if self.is_leaf(self.root):
            self.root = None
            return True

        if self.root.right is None:
            self.root = self.root.left
            return True

        replace_node = self.root.right
        replace_parent = self.root
        left_bool = False
        while replace_node.left is not None:
            replace_parent = replace_node
            replace_node = replace_node.left
            left_bool = True

        if left_bool:
            replace_parent.left = replace_node.right
        else:
            replace_parent.right = replace_node.right

        replace_node.left = self.root.left
        replace_node.right = self.root.right
        self.root = replace_node
        return True

    def pre_order_traversal(self) -> Queue:
        """
        Performs pre-order traversal of BST
        """
        q = Queue()

        if self.root is None:
            return q

        self.pre_order_helper(self.root, q)
        return q

    def pre_order_helper(self, node: object, q: object) -> None:
        """
        Recursive helper function to pre_order_traversal()
        """
        q.enqueue(node)

        if node.left is not None:
            self.pre_order_helper(node.left, q)

        if node.right is not None:
            self.pre_order_helper(node.right, q)

    def in_order_traversal(self) -> Queue:
        """
        Performs in-order traversal of BST
        """
        q = Queue()

        if self.root is None:
            return q

        self.in_order_helper(self.root, q)
        return q

    def in_order_helper(self, node: object, q: object) -> None:
        """
        Recursive helper function to in_order_traversal()
        """
        if node.left is not None:
            self.in_order_helper(node.left, q)

        q.enqueue(node)

        if node.right is not None:
            self.in_order_helper(node.right, q)

    def post_order_traversal(self) -> Queue:
        """
        Performs post-order traversal of BST
        """
        q = Queue()

        if self.root is None:
            return q

        self.post_order_helper(self.root, q)
        return q

    def post_order_helper(self, node: object, q: object) -> None:
        """
        Recursive helper function to post_order_traversal()
        """
        if node.left is not None:
            self.post_order_helper(node.left, q)

        if node.right is not None:
            self.post_order_helper(node.right, q)

        q.enqueue(node)

    def by_level_traversal(self) -> Queue:
        """
        Performs by-level traversal of BST
        """
        working_q = Queue()
        final_q = Queue()

        if self.root is None:
            return final_q

        working_q.enqueue(self.root)

        while not working_q.is_empty():
            working_node = working_q.dequeue()
            if working_node is not None:
                final_q.enqueue(working_node)
                working_q.enqueue(working_node.left)
                working_q.enqueue(working_node.right)

        return final_q

    def is_full(self) -> bool:
        """
        Indicates whether BST is full
        """
        if self.root is None:
            return True

        if self.root.left is None and self.root.right is None:
            return True

        return self.is_full_helper(self.root)

    def is_full_helper(self, node: object) -> bool:
        """
        Recursive helper function for is_full()
        """
        if self.is_leaf(node):
            return True

        if node.left is None and node.right is not None:
            return False
        if node.left is not None and node.right is None:
            return False

        return True and self.is_full_helper(node.left) and self.is_full_helper(node.right)

    def is_complete(self) -> bool:
        """
        Determines whether BST is complete
        """
        if self.root is None:
            return True

        if self.is_perfect():
            return True

        q = Queue()
        q.enqueue(self.root)

        need_leaves = False
        while not q.is_empty():
            node = q.dequeue()

            if not need_leaves:
                if node.left is None and node.right is not None:
                    return False

                elif self.is_leaf(node):
                    need_leaves = True

                elif node.left is not None and node.right is None:
                    need_leaves = True
                    q.enqueue(node.left)

                if not need_leaves and node.left is not None and node.right is not None:
                    q.enqueue(node.left)
                    q.enqueue(node.right)

            elif need_leaves:
                if not self.is_leaf(node):
                    return False

        return True

    def is_perfect(self) -> bool:
        """
        Determines whether BST is perfect
        """
        if self.root is None:
            return True

        height = self.height()
        return self.is_perfect_helper(self.root, 0, height)

    def is_perfect_helper(self, node: object, iter: int, iter_limit: int) -> bool:
        """
        Recursive helper function for is_perfect()
        """
        if iter == iter_limit:
            return True

        if node.left is None or node.right is None:
            return False

        return self.is_perfect_helper(node.left, iter + 1, iter_limit) and self.is_perfect_helper(node.right, iter + 1,
                                                                                                  iter_limit)

    def size(self) -> int:
        """
        Returns the number of TreeNodes in BST
        """
        if self.root is None:
            return 0

        return self.size_helper(self.root)

    def size_helper(self, node: object) -> int:
        """
        Recursive helper function for size()
        """
        count = 1

        if node.left is not None:
            count += self.size_helper(node.left)

        if node.right is not None:
            count += self.size_helper(node.right)

        return count

    def height(self) -> int:
        """
        Returns height of BST
        """
        if self.root is None:
            return -1

        return self.height_helper(self.root)

    def height_helper(self, node: object) -> int:
        """
        Recursive helper function for height()
        """
        if self.is_leaf(node):
            return 0

        if node.left is not None and node.right is None:
            return 1 + self.height_helper(node.left)
        if node.left is None and node.right is not None:
            return 1 + self.height_helper(node.right)

        if self.height_helper(node.left) > self.height_helper(node.right):
            return 1 + self.height_helper(node.left)
        else:
            return 1 + self.height_helper(node.right)

    def count_leaves(self) -> int:
        """
        Counts number of nodes in BST that have no children
        """
        if self.root is None:
            return 0

        return self.count_leaves_helper(self.root)

    def count_leaves_helper(self, node: object) -> int:
        """
        Recursive helper function for count_leaves()
        """
        if self.is_leaf(node):
            return 1

        if node.left is not None and node.right is None:
            return self.count_leaves_helper(node.left)
        if node.left is None and node.right is not None:
            return self.count_leaves_helper(node.right)

        return self.count_leaves_helper(node.left) + self.count_leaves_helper(node.right)

    def count_unique(self) -> int:
        """
        Counts number of nodes with unique values
        """
        if self.root is None:
            return 0

        q = Queue()
        return self.count_unique_helper(self.root, q)

    def count_unique_helper(self, node: object, q: object) -> int:
        """
        Recursive helper function for count_unique()
        """
        temp_q = Queue()
        new_value = True
        while not q.is_empty() and new_value:
            current_node = q.dequeue()
            temp_q.enqueue(current_node)
            if node.value == current_node.value:
                new_value = False

        while not temp_q.is_empty():
            current_node = temp_q.dequeue()
            q.enqueue(current_node)

        current_add = 0
        if new_value:
            q.enqueue(node)
            current_add = 1

        if self.is_leaf(node):
            return current_add

        if node.left is not None and node.right is None:
            return current_add + self.count_unique_helper(node.left, q)
        if node.left is None and node.right is not None:
            return current_add + self.count_unique_helper(node.right, q)

        return current_add + self.count_unique_helper(node.left, q) + self.count_unique_helper(node.right, q)

    def is_root(self, node: object) -> bool:
        """
        Indicates whether TreeNode passed as argument is root
        """
        if node == self.root:
            return True
        else:
            return False

    def is_leaf(self, node: object) -> bool:
        """
        Indicates whether TreeNode passed as argument is a leaf
        """
        if node.left is None and node.right is None:
            return True
        else:
            return False
