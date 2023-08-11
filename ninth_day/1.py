#using mutltithreading
import threading
import time

def greet(name):
    time.sleep(1)
    print(f"Hello {name}")

def greet_with_multithreading(names):
    threads = []
    for name in names:
        thread = threading.Thread(target=greet, args=(name,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    names = ["Alice", "Bob", "Charlie", "David"]
    greet_with_multithreading(names)


#using multiporccesing
import multiprocessing
import time

def greet(name):
    time.sleep(1)
    print(f"Hello {name}")

def greet_with_multiprocessing(names):
    processes = []
    for name in names:
        process = multiprocessing.Process(target=greet, args=(name,))
        processes.append(process)
        process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()

if __name__ == "__main__":
    names = ["Alice", "Bob", "Charlie", "David"]
    greet_with_multiprocessing(names)
