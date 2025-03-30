class Node:
    def __init__(self):
        self.data = None
        self.next_el = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.__size = 0

    def __len__(self):
        return self.__size

    def __str__(self):
        if self.head is None:
            return ""
        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.data))
            current = current.next_el
        return " ".join(elements)
    def __getitem__(self, item):
        if self.__size == 0:
            raise ValueError('The list is empty')
        if item >= self.__size or item < 0:
            raise IndexError('Index out of range')
        current_index = 0
        current = self.head
        while current_index != item:
            current = current.next_el
            current_index += 1
        return current.data

    def append(self, value):
        node = Node()
        if self.head is None:
            self.head = node
            self.head.data = value
        else:
            current = self.head
            while current.next_el is not None:
                current = current.next_el
            current.next_el = node
            current.next_el.data = value
        self.__size += 1

    def clear(self):
        self.head = None
        self.__size = 0

    def insert(self, index, value):
        if index < 0 or index > self.__size:
            raise IndexError('Index out of range')
        current_index = 0
        node = Node()
        node.data = value
        if self.head is None:
                self.head = node
        elif index == 0:
            node.next_el = self.head
            self.head = node
        else:
            current = self.head
            while current_index != index-1:
                current = current.next_el
                current_index += 1

            node.next_el = current.next_el
            current.next_el = node
        self.__size += 1

    def remove(self, index):
        if index > self.__size or index < 0:
            raise IndexError('Index out of range')
        if self.__size == 0:
            raise ValueError('The list is empty')
        if index == 0:
            self.head = self.head.next_el
        else:
            current_index = 0
            current = self.head
            while current_index != index-1 and current.next_el is not None:
                current = current.next_el
                current_index += 1
            if current.next_el is None:
                raise IndexError('Index out of range')
            current.next_el = current.next_el.next_el
        self.__size -= 1


my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.remove(0)
print(my_list)