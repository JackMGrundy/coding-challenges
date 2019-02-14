from collections import OrderedDict

q = OrderedDict()
q["a"] = 1
q["b"] = 2
a = q.popitem()

print(q)
print(a)