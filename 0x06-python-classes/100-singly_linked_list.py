#!/usr/bin/python3
"""class Node that defines a node of a singly linked list"""


class Node:
    """Represents Node of a singly linked list
    """

    def __init__(self, data, next_node=None):
        """Initializes the data of the node.
        Args:
            data (int) : data of the node
            next_node (:obj: `Node` or None): next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the data from the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data into a node"""
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next_node"""
        if type(value) != Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""class SinglyLinkedList that defines a singly linked list
"""


class SinglyLinkedList:
    """Singly linked list.
    Private instance attribute: head
    Simple instantiation
    Public instance method: def sorted_insert(self, value).
    """
    def __init__(self):
        """Initializes the linked list."""
        self.head = None

    def __str__(self):
        """Print statement in the main file."""
        rtn = ""
        node = self.head

        while node:
            rtn += str(node.data)
            rtn += "\n"
            node = node.next_node
        return rtn

    def sorted_insert(self, value):
        """Inserts a node in a sorted linked list."""
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        if value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        node = self.head
        while node.next_node and node.next_node.data < value:
            node = node.next_node
        new_node.next_node = node.next_node
        node.next_node = new_node
