# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 3: Queue-LL
#
# NAME:         BREDA MWELU
# ASSIGNMENT:   Project 5: Implementing ADTs

from Node import Node

class QueueLL(object):
    def __init__(self, list=None):
        self.front = None
        self.tail = None
        if list is not None:
            for item in list:
                self.enq(item)
# Returns the data at the front of the queue
    def get_front(self):
        if  list is not None:
            current = self.front
            return current.data
        return None

# Returns data at the back of the queue
    def get_tail(self):
        if list is not None:
            temp = self.tail
            return temp.data
        return None

# returns the data on the front of the queue and removes it, otherwise returns None if the queue is empty
    def deq(self):
        if self.front is None:
            return
        temp = self.front
        self.front = self.front.next_node
        if self.front is None:
            self.tail = None
        return temp.data
# adds a new Node with data to the tail of the queue
    def enq(self, data=None):
        newnode = Node(data)
        if self.tail is None:
            if self.front is None:
                self.front = newnode
                self.tail = newnode
                return
        else:
            self.tail.next_node = newnode
            self.tail = newnode

        return self.tail

    def print(self):
        n = self.front
        while n is not None:
            print(n.get_data(), "=>", end=" ")
            n = n.get_next()
        print("NULL")

# Returns true if the queue is empty
    def is_empty(self):

        return self.tail is None and self.front is None
# Make the queue empty
    def clear(self):
        while self.front and self.tail is not None:
            self.tail = None
            self.front= None

        return self.tail and self.front


def main():
    s = QueueLL()
    s.print()
    print("Is empty?", s.is_empty())
    for i in range(1, 7):
        s.enq(i)
    s.print()
    print("Peek:", s.peek())
    print("Deq: ", s.deq())
    s.print()
    print("Is empty?", s.is_empty())

# Don't run main on import
if __name__ == "__main__":
    main()

