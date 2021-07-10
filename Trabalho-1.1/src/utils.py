from random import randint
import matplotlib.pyplot as plt

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

def plot_metrics(results: dict, label: str) -> None:
    """Plot timestamp results

    Args:
        results (dict): [description]
        label (str): [description]
    """
    k = [1, 2, 4, 8]
    plt.plot(k, results['mean'], 'bo--')
    plt.plot(k, results['std'], 'ro--')
    plt.legend(['Média', 'Desvio Padrão'])
    plt.xlabel(label)
    plt.ylabel('Tempo (s)')
    plt.show()