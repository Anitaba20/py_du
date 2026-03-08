import threading

numbers = [1, 2, 5, 4, 3, 0]

def find_largest():
    largest = max(numbers)
    print("Najväčšie číslo je:", largest)

def find_smallest():
    smallest = min(numbers)
    print("Najmenšie číslo je:", smallest)

thread1 = threading.Thread(target=find_largest)
thread2 = threading.Thread(target=find_smallest)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Zoznam čísel:", numbers)