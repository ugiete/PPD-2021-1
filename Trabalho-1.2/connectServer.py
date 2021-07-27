from src.server import Server
from sys import argv

if __name__ == "__main__":
    port = int(argv[1])

    s = Server(port=port)