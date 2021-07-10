from sys import argv
from random import seed
from time import time
from src.process import process_sort
from src.utils import generate_list, plot_averages, plot_deviation
from src.thread import thread_sort

if __name__ == '__main__':
    params = argv[1:]
    is_process_sort = params == [] or params[0].lower() != '--thread'

    seed(time())

    LENGTH = 5000000
    INITIAL_LIST = generate_list(LENGTH)

    if is_process_sort:
        results = process_sort(INITIAL_LIST, LENGTH)
        label = "Processos"
    else:
        results = thread_sort(INITIAL_LIST, LENGTH)
        label = "Threads"
    
    plot_deviation(results['std'], label)
    plot_averages(results['mean'], label)