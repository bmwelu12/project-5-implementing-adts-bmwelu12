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
        if self.is_empty():
            return None
        else:
            return self.array[self.front]


# Returns data at the back of the queue
    def get_tail(self):
        if self.is_empty():
            return None
        else:
           return self.array[self.tail]

# Returns the data at the front of the queue
    def deq(self):
        if self.is_empty():
            return None
        else:
            x = self.array[self.front]
            self.front =+ 1
            return x

# Adds data to the front of the queue
    def enq(self, data=None):
        if self.is_empty():
            self.front = 0
            self.tail = 0
            self.array[0] = data
        if self.is_full():
            temp_array =[None for i in range(2 * self.size())]
            size = self.size()
            for i in range(size):
                x = i + self.front
                temp_array[i] =self.array[x % len(self.array)]
            self.array = temp_array
            self.front = 0
            self.tail =size-1
        else:
            self.tail += 1
            self.array[self.tail % len(self.array)] = data


    def print(self):
        for i in range(self.front, self.front + self.size(), 1):
            print(self.array[i % len(self.array)], "=>", end=" ")
        print("NULL")

# Returns true if queue is empty
    def is_empty(self):

        return self.size() == 0
# Makes the queue empty
    def clear(self):
        self.array = [None for i in range(self.size())]
        self.front = -1
        self.tail = -1
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

