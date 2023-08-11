import time
import threading

# Function for finding factorial without multithreading
def factorial_without_multithreading(n):
    result = 1
    for i in range(1, n + 1):
        time.sleep(0.001)  # Simulate some processing time
        result *= i
    return result

# Function for finding factorial with multithreading
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        time.sleep(0.001)  # Simulate some processing time
        result *= i
    return result

def run_without_multithreading():
    numbers = [5, 7, 3, 10]
    start_time = time.time()
    results = [factorial_without_multithreading(num) for num in numbers]
    end_time = time.time()
    print(f"Results without multithreading: {results}")
    print(f"Time taken without multithreading: {end_time - start_time:.4f} seconds")

def run_with_multithreading():
    numbers = [5, 7, 3, 10]
    start_time = time.time()
    threads = [threading.Thread(target=lambda: factorial(num)) for num in numbers]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    end_time = time.time()
    print(f"Time taken with multithreading: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    run_without_multithreading()
    run_with_multithreading()
