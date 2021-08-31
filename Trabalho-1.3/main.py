from random import sample
from math import pow
from threading import Thread
from multiprocessing.pool import ThreadPool
# import src.mqttPub as pub
# import src.mqttSub as sub

# def ID_random_sort(n: int = 32) -> int:
#     return randint(0, int(pow(2,n))-1)

ID_list = sample(range(int(pow(2,32))),8) # node ID list
print(ID_list)
# for _ in range(0,8):
#     id = ID_random_sort()
#     while id in ID_list:
#         id = ID_random_sort()
#     ID_list.append(id)


def join(nodeID: int) -> None:
    print(nodeID)

pool = ThreadPool(processes=8)
pool.map(func=join, iterable=ID_list, chunksize=1)
pool.close()
pool.join()

pool.terminate()