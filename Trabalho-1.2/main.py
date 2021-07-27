from src.client import Client

c = Client()

k1 = c.put(50)
k2 = c.put(150)

print(k1)
print(k2)

print(c.get(k1))
print(c.get(k2))
print(c.get("asdsad"))