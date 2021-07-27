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

def plot_deviation(k: list, deviation: list, label: str) -> None:
    """Plot standard deviation chart

    Args:
        k (list): Threads/Process used
        deviation (list): Standard deviation of the timestamps
        label (str): "Threads" or "Processos"
    """
    
    plt.bar(x=k, height=deviation, color='r')
    plt.xlabel(label)
    plt.ylabel('Desvio Padrão (s)')
    plt.show()

def plot_averages(k: list, averages: list, label: str) -> None:
    """Plot mean chart

    Args:
        k (list): Threads/Process used
        averages (list): Timestamps averages
        label (str): "Threads" or "Processos"
    """
    
    plt.plot(k, averages, 'bo-')
    plt.xlabel(label)
    plt.ylabel('Tempo Médio (s)')
    plt.show()