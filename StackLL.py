# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 2: Stack-LL
#
# NAME:         BREDA MWELU
# ASSIGNMENT:   Project 5: Implementing ADTs

from Node import Node

class StackLL(object):
    def __init__(self, list=None):
        self.top = None
        if list is not None:
            for item in list:
                self.add(item)

    # returns the data on the top of the stack, and None otherwise
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.top.data
    # returns the data on the top of the stack,
    def pop(self):
        if self.top is None:
            return None
        else:
            new_node = self.top.data
            self.top = self.top.next_node
            return new_node

    # adds a new Node with data on the top of the stack
    def push(self, data=None):
        if self.top == None:
            self.top = Node(data)
        else:
            newnode = Node(data)
            newnode.next_node = self.top
            self.top = newnode
        return self.top

# Display the contents of the stack
    def print(self):
        n = self.top
        while n is not None:
            print(n.get_data(), "=>", end=" ")
            n = n.get_next()
        print("NULL")
# returns True if the stack is empty
    def is_empty(self):
        if self.top == None:
            return True
        else:
            return False

# Makes the stack empty
    def clear(self):
        newnode = self.top
        while newnode is not None:
            newnode.next_node = self.top
            self.top = None
            return self.top

def main():
    s = StackLL()
    s.print()
    print("Is empty?", s.is_empty())
    for i in range(1, 7):
        s.push(i)
    print("Peek:", s.peek())
    print("Pop: ", s.pop())
    s.print()
    print("Is empty?", s.is_empty())
    while not s.is_empty():
        print(s.pop())

# Don't run main on import
if __name__ == "__main__":
    main()

