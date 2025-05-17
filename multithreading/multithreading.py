# Multithreading Example Basic

import threading

def thread1():
    print("Welcome Thread 1 :")

def thread2():
    print("Welcome Thread 2 :")

if __name__ == "__main__":
    t1 = threading.Thread(target=thread1)
    t2 = threading.Thread(target=thread2)
    t1.start()
    t2.start()

    # waits for the threads to complete
    t1.join()
    t2.join()
    print("Done!")