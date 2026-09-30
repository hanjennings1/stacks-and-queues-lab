import random

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        # Add item to back of the line
        self.items.append(item)


    def dequeue(self):
        # Remove and return item at the front of the line
        if self.is_empty():
            return None
        return self.items.pop(0)


    def peek(self):
        # Look at the front item, without removing it
        if self.is_empty():
            return None
        return self.items[0]


    def is_empty(self):
        # True when no one is in line/length=0
        return len(self.items) == 0


    def select_and_announce_winner(self):
        """
        Randomly selects a winner from the queue.
        Dequeues all items up to and including the winner.
        Returns the name of the winning customer.
        """
        # Nobody in line: no winner
        if self.is_empty():
            return None

        # Picking random person in line as winner
        winner = random.choice(self.items)

        # Remove people at front until the winner is at front
        while not self.is_empty():
            customer = self.dequeue()
            if customer == winner:
                break

        print(f"The winner is {winner}!")
        return winner
