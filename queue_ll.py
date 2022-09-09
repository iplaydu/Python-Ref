from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return not self.items

    def enqueue(self, items):
        self.items.append(items)

    def dequeue(self):
        return self.items.popleft()

    def size(self):
        return(len(self.items))

    def peek(self):
        return self.items[0]

    def __str__(self):
        return str(self.items)

    
if __name__ == "__main__":
    q = Queue()
    print(q)
    print(q.is_empty())
    q.enqueue("J")
    q.enqueue("o")
    q.enqueue("s")
    q.enqueue("h")
    q.enqueue("u")
    q.enqueue("a")
    print(q)
    # q.dequeue()
    # q.dequeue()
    print(q.dequeue())
    print(q.dequeue())    
    print(q.size())
    print(q.peek())
    print(q)