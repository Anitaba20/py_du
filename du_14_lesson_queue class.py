# du_27.01.26_create a queue class for character values
# IsEmpty – check if the queue is empty;
# IsFull – check if the queue is full;
# Enqueue – add an element to the queue;
# Dequeue – delete an element from the queue;
# Show – display all queue elements on the screen.
# When the app starts, display a menu that a user can use to choose the desired operation.

class Queue:
    def __init__(self):
        self.elements = []

    def isEmpty(self):
        return len(self.elements) == 0

    def isFull(self):
        return False

    def enqueue(self, element):
        self.elements.append(element)
        print("Element added")

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            removed = self.elements.pop(0)
            print(removed)

    def show(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print(self.elements)


queue = Queue()

while True:
    print("\nMenu:")
    print("1 IsEmpty")
    print("2 IsFull")
    print("3 Enqueue")
    print("4 Dequeue")
    print("5 Show")
    print("6 Exit")

    option = input("Option: ")

    if option == "1":
        print(queue.isEmpty())

    elif option == "2":
        print(queue.isFull())

    elif option == "3":
        element = input("Enter element: ")
        queue.enqueue(element)

    elif option == "4":
        queue.dequeue()

    elif option == "5":
        queue.show()

    elif option == "6":
        print("Exit")
        break