import time
import multiprocessing

# Function for finding nth Fibonacci number without multiprocessing
def fibonacci_without_multiprocessing(n):
    if n <= 0:
        return None
    if n == 1:
        return 0
    if n == 2:
        return 1

    prev, curr = 0, 1
    for _ in range(n - 2):
        time.sleep(0.001)  # Simulate some processing time
        prev, curr = curr, prev + curr

    return curr
# Function for finding nth Fibonacci number with multiprocessing
def fibonacci(n):
    if n <= 0:
        return None
    if n == 1:
        return 0
    if n == 2:
        return 1

    prev, curr = 0, 1
    for _ in range(n - 2):
        time.sleep(0.001)  # Simulate some processing time
        prev, curr = curr, prev + curr

    return curr
def run_without_multiprocessing():
    numbers = [5, 7, 3, 10]
    start_time = time.time()
    results = [fibonacci_without_multiprocessing(num) for num in numbers]
    end_time = time.time()
    print(f"Results without multiprocessing: {results}")
    print(f"Time taken without multiprocessing: {end_time - start_time:.4f} seconds")

def run_with_multiprocessing():
    numbers = [5, 7, 3, 10]
    start_time = time.time()
    with multiprocessing.Pool() as pool:
        results = pool.map(fibonacci, numbers)
    end_time = time.time()
    print(f"Results with multiprocessing: {results}")
    print(f"Time taken with multiprocessing: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    run_without_multiprocessing()
    run_with_multiprocessing()
