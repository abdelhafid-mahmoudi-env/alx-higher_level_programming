#!/usr/bin/python3
"""Defines the classes Node and SinglyLinkedList"""

class Node:
    """
    Class that defines properties Node.

    Attributes:
        data: data field of a node.
    """
    def __init__(self, data, next_node=None):
        """Creates new instances of node.

        Args:
            data : data field of a node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the data field instance.

        Returns: the data field of a node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Property setter for data.

        Args:
            value (int): data field of a node.

        Raises:
            TypeError: data must be an integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrives the next_node instance.

        Returns: The next_node instance.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Property setter for Node.

        Args:
            value (None): next node of a Node.

        Raises:
            TypeError: next_node must be a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """
    Class that defines properties of SinglyLinkedList.

    Attributes:
        head: head of the SinglyLinkedList.
    """
    def __init__(self):
        """Creates new instances of SinglyLinkedList .

        Args:
            head: head of the SinglyLinkedList.
        """
        self.__head = None

    def __str__(self):
        """Represents the class objects as a string.

        Returns: The class object represented as a string.
        """
        temp_var = self.__head
        print_node = []
        while temp_var:
            print_node.append(str(temp_var.data))
            temp_var = temp_var.next_node

        return ("\n".join(sorted(print_node, key=int)))

    def sorted_insert(self, value):
        """Inserts a new node at a given position.

        Args:
            value: value.
        """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif value <= self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and value > current.next_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
