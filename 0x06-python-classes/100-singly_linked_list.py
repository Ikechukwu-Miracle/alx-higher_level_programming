#!/usr/bin/python3
"""Defines class for a singly linked list"""

class Node:
    """Represents a node a singly_linked list"""


    def __init__(self, data, next_node=None):
        """Initializes the Node.

        Args:
        data(int): the data part of the node
        next_node(Node): link to the next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets and sets the data for the node"""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Gets and sets the next node for the node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """ Reprents a singly-linked list"""


    def __init__(self):
        """initializes a singly-linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node to the singly-linked list.

        The node is sorted and inserted into the list at the
        correct odered numerical position.

        Args:
        value(Node): the new node
        """
        new = Node(value)
        if self.__head is None or self.__head.data >= value:
            new.next_node = self.__head
            self.__head = new
        else:
            curr = self.__head
            while curr.next_node is not None and curr.next_node.data < value:
                curr = curr.next_node
            new.next_node = curr.next_node
            curr.next_node = new

    def __str__(self):
        """Defines the representation of a singly-linked list for print()"""
        nodes = []
        curr = self.__head
        while curr is not None:
            nodes.append(str(curr.data))
            curr = curr.next_node
        return "\n".join(nodes)
