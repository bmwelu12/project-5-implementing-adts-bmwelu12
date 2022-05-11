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
        if self.front == -1:
            return None
        return self.array[self.front]

    # Returns data at the back of the queue
    def get_tail(self):
        if self.front == -1:
            return None
        return self.array[self.tail]

    # Returns the data at the front of the queue
    def deq(self):
        if self.front == -1:
            return None
        data = self.array[self.front]
        self.front += 1
        return data

# Adds data to the front of the queue
    def enq(self, data=None):
        if self.front == -1:
            self.front = 0
            self.tail = 0
            self.array[0] = data
        elif self.tail == len(self.array) - 1:
            self.array.append(data)
            self.tail += 1
        else:
            self.array[self.tail + 1] = data
            self.tail += 1

    def print(self):
        for i in range(self.front, self.front + self.size(), 1):
            print(self.array[i % len(self.array)], "=>", end=" ")
        print("NULL")

# Returns true if queue is empty
    def is_empty(self):
        return self.front == -1 or self.front > self.tail

# Makes the queue empty
    def clear(self):
        self.front = -1
        self.tail = -1

    # Returns true if the queue is empty
    def is_full(self):
        s = self.size()
        return s >= len(self.array)

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

