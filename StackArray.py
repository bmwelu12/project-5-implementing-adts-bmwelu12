# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 4: Stack-Array
#
# NAME:         BREDA MWELU
# ASSIGNMENT:   Project 5: Implementing ADTs

class StackArray(object):
    def __init__(self, size=5):
        self.array = [0 for i in range(size)]
        self.top = -1

    # returns the data on the top of the stack, and None otherwise
    def peek(self):
        if self.is_empty():
            return None
        return self.array[-1]

# returns the data on the top of the stack
    def pop(self):
        if not self.is_empty():
            last = self.array[-1]
            del self.array[-1]
            self.top -=1
            return last
        else:
            return None

# puts data on the top of the stack
    def push(self, data=None):
        self.array.append(data)
        self.top += 1


    def print(self):
        for i in range(self.top, -1, -1):
            print(self.array[i], "=>", end=" ")
        print("NULL")
# returns True if the stack is empty, or False otherwise
    def is_empty(self):
        return self.size() == 0

    def is_full(self):
        return self.top == len(self.array) - 1

    def clear(self):
        self.array = [None for i in range(self.size())]
        self.top = -1

    def size(self):
        return self.top + 1


def main():
    s = StackArray()
    s.print()
    print("Is empty?", s.is_empty())
    for i in range(1, 10):
        s.push(i)
    s.print()
    print("Peek:", s.peek())
    print("Pop: ", s.pop())
    s.print()
    print("Is empty?", s.is_empty())

# Don't run main on import
if __name__ == "__main__":
    main()

