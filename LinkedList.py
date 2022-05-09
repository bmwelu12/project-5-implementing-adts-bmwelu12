# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 1: Linked List
#
# NAME:         BREDA MWELU
# ASSIGNMENT:   Project 5: Implementing ADTs

from Node import Node

class LinkedList(object):
    def __init__(self, list=None):
        self.head = None
        if list is not None:
            for item in list:
                self.add(item)

# Returns the data in the head node, and None otherwise
    def get_head(self):
        if list is not None:
            current = self.head
            return current.data
        return None


    # Function to add a new node
    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    # Returns True if data is in the list, or False otherwise
    def search(self, data):
        new_node = self.head
        while (new_node is not None):
            if (new_node.data == data):

                return True
            new_node = new_node.next_node

        return False

    # searches for data in the list, removes it if found and returns it,
    def delete(self, data):
        new_node = self.head

        prev = None
        while (new_node is not None):
            if new_node.data == data:
                if new_node == self.head:
                    self.head = new_node.next_node
                else:
                    prev.next_node = new_node.next_node

                return data
            prev = new_node
            new_node = new_node.next_node



        return None



    def print(self):
        n = self.head
        while n is not None:
            print(n.get_data(), "=>", end=" ")
            n = n.get_next()
        print("NULL")

    # Checks if the list is empty
    def is_empty(self):
        if self.head is None:
         return True
        return False


    # Clears the list
    def clear(self):
        while (self.head is not None):
           self.head = self.head.next_node

        return None

def main():
    l = list(range(1, 5))
    l.reverse()
    ll = LinkedList(l)
    ll.print()
    print("Search 4: ", ll.search(4))
    print("Search 5: ", ll.search(5))
    print("Delete 5: ", ll.delete(5))
    print("Delete 4: ", ll.delete(4))
    ll.print()
    print("Delete 1: ", ll.delete(1))
    ll = LinkedList()
    ll.add(15)

    ll.add(16)

    ll.add(17)
    ll.print()
    print(ll.search(15))
    print(ll.delete(17))
    ll.print()

# Don't run main on import
if __name__ == "__main__":
    main()

