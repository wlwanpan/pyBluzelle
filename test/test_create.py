import pyBluzelle
b = pyBluzelle.create_connection("127.0.0.1", 51011, "137a8403-52ec-43b7-8083-91391d4c5e67")
res = b.create("kk","1234")
print(res)
res = b.create("gg","1234")
print(res)
res = b.keys()
print(res)
res = b.read("gg")
print(res)
res = b.has("gg")
print(res)
res = b.delete("gg")
print(res)
res = b.keys()
print(res)
res = b.read("gg")
print(res)
res = b.delete("kk")
print(res)