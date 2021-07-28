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

def plot_table(timestamps: dict, threadList: list, mList: list) -> None:
    """Plot standard deviation chart

    Args:
        k (list): Threads/Process used
        deviation (list): Standard deviation of the timestamps
        label (str): "Threads" or "Processos"
    """
    plt.plot(threadList, timestamps.values(), 'o-')
    plt.legend(mList, title = 'Total valores', loc='best', bbox_to_anchor=(0.5, 0., 0.5, 0.5))
    plt.xlabel('Número de processos')
    plt.ylabel('Tempo de Execução (s)')
    plt.title('Tempo de Execução por Total de Processos e Valores')
    plt.show()
    