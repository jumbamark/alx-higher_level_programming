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
        ptr = self.__head

        while ptr is not None:
            rtn += str(ptr.data)
            if ptr.next_node is not None:
                rtn += "\n"
            ptr = ptr.next_node

        return rtn

    def sorted_insert(self, value):
        """Inserts a node in a sorted linked list."""
        ptr = self.__head

        while ptr is not None:
            if ptr.data > value:
                break
            ptr_prev = ptr
            ptr = ptr.next_node

        newNode = Node(value, ptr)
        if ptr == self.__head:
            self.__head = newNode
        else:
            ptr_prev.next_node = newNode
