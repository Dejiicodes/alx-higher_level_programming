#!/usr/bin/python3
"""Defines a singly linked list and its nodes."""


class Node:
    """Defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initializes a new node.

        Args:
            data (int): The data for the node.
            next_node (Node): The next node in the list (default is None).
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data of the node.

        Args:
            value (int): The data for the node.

        Raises:
            TypeError: If `value` is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next node.

        Args:
            value (Node): The next node in the list.

        Raises:
            TypeError: If `value` is not a Node or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list."""

    def __init__(self):
        """Initializes a new singly linked list."""
        self.head = None

    def __str__(self):
        """Returns a string representation of the linked list."""
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the list.

        Args:
            value (int): The value to be inserted.
        """
        new_node = Node(value)
        if not self.head or self.head.data >= new_node.data:
            new_node.next_node = self.head
            self.head = new_node
            return
        current = self.head
        while current.next_node and current.next_node.data < new_node.data:
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node


if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.sorted_insert(2)
    sll.sorted_insert(5)
    sll.sorted_insert(3)
    sll.sorted_insert(10)
    sll.sorted_insert(1)
    sll.sorted_insert(-4)
    sll.sorted_insert(-3)
    sll.sorted_insert(4)
    sll.sorted_insert(5)
    sll.sorted_insert(12)
    sll.sorted_insert(3)
    print(sll)
