from numpy import mean, std
from time import time
from threading import Thread
from .utils import order_list

def thread_sort(initial_list: list, length: int) -> dict:
    """Parallel sort with threads

    Args:
        initial_list (list): List to be ordered
        length (int): Initial length

    Returns:
        dict: Dictionary with mean and standard deviation for elapsed time
    """
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
                    elements_per_thread = length // active_threads
                    partition = out_list[elements_per_thread * i : elements_per_thread * (i+1)]

                    thread = Thread(target=order_list(partition))
                    jobs.append(thread)

                for j in jobs:
                    j.start()

                for j in jobs:
                    j.join()
                
                active_threads = active_threads // 2

            end = time() - start
            k_timestamps.append(end)
        
        results['mean'].append(mean(k_timestamps))
        results['std'].append(std(k_timestamps))
    
    return results
