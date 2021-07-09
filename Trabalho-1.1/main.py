from numpy import mean, std
from random import randint, seed
from time import time
from threading import Thread

def generate_list(length: int) -> list:
    """Generate a list with given length with random integer values in the interval [0, length]

    Args:
        length (int): List length

    Returns:
        list: List generated with random values
    """

    return [randint(0, length + 1) for _ in range(length)]

def order_list(partition: list) -> None:
    """Sort a non-empty partition with Python's standard sort algorithm for lists

    Args:
        partition (list): Partition that will be sorted
    """
    partition.sort()

if __name__ == "__main__":
    seed(time())

    SIZE = 50000000
    initial_list = generate_list(SIZE)
    results = {
        'mean': [],
        'std': []
    }

    for k in [1, 2, 4, 8]:
        k_timestamps = []

        for _ in range(10):
            out_list = initial_list[:]
            active_threads = k

            start = time()
            while active_threads > 0:
                jobs = []

                for i in range(active_threads):
                    elements_per_thread = SIZE // active_threads
                    partition = out_list[elements_per_thread * i : elements_per_thread * (i+1)]

                    thread = Thread(target=order_list(partition))
                    jobs.append(thread)

                for j in jobs:
                    j.start()

                for j in jobs:
                    j.join()
                
                active_threads = active_threads // 2

            end = time() - start
            print(end)
            k_timestamps.append(end)
        
        results['mean'].append(mean(k_timestamps))
        results['std'].append(std(k_timestamps))
        print(k_timestamps)
        print("*********************\n")
