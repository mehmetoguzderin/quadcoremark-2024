import time
import threading
import multiprocessing

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def calc_fibonacci_thread(num, results, index):
    results[index] = fibonacci(num)

def calc_primes_thread(limit, results, index):
    primes = []
    for i in range(limit):
        if is_prime(i):
            primes.append(i)
    results[index] = primes

def benchmark():
    num_threads = 4 # multiprocessing.cpu_count()
    print(f"Running benchmark with {num_threads} threads...")

    fib_numbers = [35, 34, 33, 32, 31, 30, 29, 28, 27, 26][:num_threads]
    prime_limits = [10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000][:num_threads]

    threads = []
    results = [None] * num_threads

    start_time = time.time()

    for i in range(num_threads):
        if i % 2 == 0:
            thread = threading.Thread(target=calc_fibonacci_thread, args=(fib_numbers[i // 2], results, i))
        else:
            thread = threading.Thread(target=calc_primes_thread, args=(prime_limits[i // 2], results, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    total_time = end_time - start_time

    print(f"Benchmark completed in {total_time:.2f} seconds")
    # print("Results:", results)

if __name__ == "__main__":
    benchmark()
