# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 5: Queue-Array
#
# NAME:         BREDA MWELU
# ASSIGNMENT:   Technical HW: Implementing ADTs

class QueueArray(object):
    def __init__(self, size=5):
        self.array = [0 for i in range(size)]
        self.front = -1
        self.tail = -1

    def get_front(self):
        return self.array[0]

# Returns data at the back of the queue
    def get_tail(self):
        return self.array[-1]

# Returns the data at the front of the queue
    def deq(self):
        if not self.is_empty():
            deq_data = self.array[0]
            self.array = self.array[1:]
            return deq_data
        return None

# Adds data to the front of the queue
    def enq(self, data=None):
        for i in range(len(self.array) - 1, -1, -1):
            if i == 0:
                self.array[i] = data
                return
        self.array += [data]

    def print(self):
        for i in range(self.front, self.front + self.size(), 1):
            print(self.array[i % len(self.array)], "=>", end=" ")
        print("NULL")

# Returns true if queue is empty
    def is_empty(self):
        if self.array[0] == 0:
            return True
        return False

# Makes the queue empty
    def clear(self):
        self.front = 0

# Returns true if the queue is empty
    def is_full(self):
        l = self.size()
        return l >= len(self.array)

# Returns the size of the queue
    def size(self):
        if self.front == -1:
            return 0
        l = self.tail - self.front + 1
        if self.tail < self.front:
            l = len(self.array) - self.front + self.tail + 1
        return l


def main():
    s = QueueArray()
    s.print()
    print("Is empty?", s.is_empty())
    for i in range(1, 4):
        s.enq(i)
        #print("Size:", s.size())
        #s.print()
    s.print()
    print("Deq: ", s.deq())
    print("Deq: ", s.deq())
    s.print()
    for i in range(5, 11):
        s.enq(i)
        #print("Size:", s.size())
        #s.print()
    print("Front:", s.get_front())
    print("Tail: ", s.get_tail())
    print("Deq:  ", s.deq())
    s.print()
    print("Is empty?", s.is_empty())
    print("Size:", s.size())


# Don't run main on import
if __name__ == "__main__":
    main()

