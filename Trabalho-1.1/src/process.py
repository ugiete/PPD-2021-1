from numpy import mean, std
from time import time
from multiprocessing import Process
from .utils import order_list

def process_sort(initial_list: list, length: int) -> dict:
    """Parallel sort with processs

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
            active_processes = k

            start = time()
            while active_processes > 0:
                jobs = []

                for i in range(active_processes):
                    elements_per_process = length // active_processes
                    partition = out_list[elements_per_process * i : elements_per_process * (i+1)]

                    process = Process(target=order_list(partition))
                    jobs.append(process)

                for j in jobs:
                    j.start()

                for j in jobs:
                    j.join()
                
                active_processes = active_processes // 2

            end = time() - start
            k_timestamps.append(end)
        
        results['mean'].append(mean(k_timestamps))
        results['std'].append(std(k_timestamps))
    
    return results
