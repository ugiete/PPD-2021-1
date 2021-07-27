from xmlrpc.server import SimpleXMLRPCServer

class Server():
    """RPC Server
    """

    def __init__(self, host: str = "localhost", port: int = 8000) -> None:
        self._table = dict()
        self._server = SimpleXMLRPCServer((host, port), allow_none = True)

        self._server.register_multicall_functions()
        self._server.register_function(self.__get, "get")
        self._server.register_function(self.__put, "put")
        self._server.register_function(self.__show, "show")

        print(f"Listening on port {host}:{port}...")
        self._server.serve_forever()

    def __get(self, k: str) -> int:
        """Get value from key

        Args:
            k (int): Key

        Returns:
            int: value
        """
        try:
            print(f"Retrieve {self._table[k]} from {k}")
            return self._table[k]
        except:
            print(f"No {k} key")
            return None
    
    def __put(self, v: int) -> str:
        """Insert new value in hash table

        Args:
            v (int): Value to be added

        Returns:
            int: Generated key
        """
        v_salt = v + 0.5
        k = str(hash(v_salt))

        self._table[k] = v

        print(f"Put {v} on {k}")
        return k
    
    def __show(self) -> str:
        """Show all hash table

        Returns:
            str: Stringify hash table
        """
        return str(self._table)