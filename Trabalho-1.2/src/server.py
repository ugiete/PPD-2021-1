from xmlrpc.server import SimpleXMLRPCServer

class Server():
    """RPC Server
    """

    def __init__(self, host: str = "localhost", port: int = 8000) -> None:
        self._table = dict()
        self._server = SimpleXMLRPCServer((host, port), allow_none = True)

        self._server.register_function(self.__get, "get")
        self._server.register_function(self.__put, "put")
        self._server.register_function(self.__show, "show")

        print(f"Listening on {host}:{port}...")
        try:
            self._server.serve_forever()
        except KeyboardInterrupt:
            print("Server Interrupted")
            exit(0)

    def __get(self, k: str) -> int:
        """Get value from key

        Args:
            k (int): Key

        Returns:
            int: value
        """
        try:
            return self._table[k]
        except:
            return None
    
    def __put(self, v: int) -> str:
        """Insert new value in hash table

        Args:
            v (int): Value to be added

        Returns:
            str: Generated key
        """
        v_salt = v + 0.5
        k = str(hash(v_salt))

        self._table[k] = v

        return k
    
    def __show(self) -> str:
        """Show all hash table

        Returns:
            str: Stringify hash table
        """
        return str(self._table)