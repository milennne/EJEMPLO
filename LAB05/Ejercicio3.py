import random

class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None  

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None 

    def is_empty(self):
        return self.front is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty!")
        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return value

    def size(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count

def hot_potato(players, max_passes):
    queue = Queue()

    for name in players:
        queue.enqueue(name)

    while queue.size() > 1:
        passes = random.randint(1, max_passes)
        print(f"\n🎲 Number of passes this round: {passes}")

        for _ in range(passes):
            player = queue.dequeue()
            queue.enqueue(player)
            print(f"👉 {player} passed the potato")

        eliminated = queue.dequeue()
        print(f"💥 {eliminated} is eliminated!")

    winner = queue.dequeue()
    print(f"\n🏆 The winner is: {winner}")
    return winner

max_passes = 6
players_list = ["Noa", "Fuentes", "Coronel", "Angie", "Elliot"]

hot_potato(players_list, max_passes)
