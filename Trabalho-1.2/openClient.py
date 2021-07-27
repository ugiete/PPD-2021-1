from src.client import Client
import asyncio

c = Client(port=9999)

k1 = c.put(50)
k2 = c.put(150)

print(k1)
print(k2)

print(c.get(k1))
print(c.get(k2))
print(c.get("asdsad"))

print(c.show())