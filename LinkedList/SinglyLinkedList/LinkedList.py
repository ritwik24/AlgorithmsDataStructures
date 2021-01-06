class Node:

    def __init__(self, data: int = None, next_node: "Node" = None):
        self.data = data
        self.next_node = next_node

    def set_data(self, data):
        self.data = data

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next_node(self):
        return self.next_node

    def has_next(self) -> bool:
        """
        returns true if node points to next node else false
        """
        return self.next_node is not None


class LinkedList(object):

    def __init__(self):
        self.length = 0
        self.head = None

    def _increase_length(self) -> None:
        self.length += 1

    def _decrease_length(self) -> None:
        self.length -= 1

    def get_length(self) -> int:
        return self.length

    def traverse(self) -> str:
        """
        traverse entire linked list and append data in str,
        time complexity = O(n), for scanning the list of size n
        space complexity = O(1), for creating a temporary variable
        """
        data = ""
        current = self.head
        while current is not None:
            data += f"{current.get_data()} "
            current = current.get_next_node()
        return data

    def insert_at_beginning(self, data: int) -> None:
        """
        insert an element at the beginning of the list,
        time complexity = O(1), as only 1 pointer gets modified
        space complexity = O(1), for creating a temporary variable
        """
        new_node = Node(data)
        new_node.set_next_node(self.head)
        self.head = new_node
        self._increase_length()

    def insert_at_end(self, data: int) -> None:
        """
        insert an element at the end of the list,
        time complexity = O(n), for scanning the list of size n
        space complexity = O(1), for creating a temporary variable
        """
        current = self.head
        new_node = Node(data)
        if current is not None:
            while current.next_node is not None:
                current = current.get_next_node()
            current.set_next_node(new_node)
        else:
            new_node.set_next_node(self.head)
            self.head = new_node
        self._increase_length()

    def insert_after_position(self, data: int, position: int) -> None:
        """
        insert an element at the desired position of the list,
        time complexity = O(n), since in worst case we may insert at the end
        space complexity = O(1), for creating a temporary variable
        """
        if self.get_length() < position:
            return
        elif self.get_length() == 0:
            return self.insert_at_beginning(data)
        elif self.get_length() == position:
            return self.insert_at_end(data)
        else:
            current = self.head
            new_node = Node(data)
            for _ in range(position - 1):
                current = current.get_next_node()
            new_node.set_next_node(current.get_next_node())
            current.set_next_node(new_node)
            self._increase_length()

    def delete_at_beginning(self) -> None:
        """
        delete an element from the beginning of the list,
        time complexity = O(1), only moving the pointer
        space complexity = O(1), for creating a temporary variable
        :return item deleted otherwise None
        """
        current = self.head
        if current is None:
            return None
        else:
            self.head = self.head.get_next_node()
            temp = current.get_data()
            del current
            self._decrease_length()
            return temp

    def delete_at_end(self) -> None:
        """
        delete an element from the end of the list,
        time complexity = O(n), since we are scanning the entire list
        space complexity = O(1), for creating a temporary variable
        :return item deleted otherwise None
        """
        previous = self.head
        current = self.head
        if current is None:
            return None
        else:
            while current.has_next():
                previous = current
                current = current.get_next_node()
            previous.set_next_node(None)
            temp = current.get_data()
            del current
            self._decrease_length()
            return temp

    def delete_after_position(self, position: int) -> None:
        """
        delete an element from the desired position in the list,
        time complexity = O(n), since in worst case we may insert at the end
        space complexity = O(1), for creating a temporary variable
        :return item deleted otherwise None
        """
        if self.get_length() < position:
            return
        elif self.get_length() == 0:
            return self.delete_at_beginning()
        elif self.get_length() == position:
            return self.delete_at_end()
        else:
            previous = self.head
            current = self.head
            for _ in range(position - 1):
                previous = current
                current = current.get_next_node()
            previous.set_next_node(current.get_next_node())
            current.set_next_node(None)
            temp = current.get_data()
            del current
            self._decrease_length()
            return temp
