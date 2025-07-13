import random

lst = [random.choice([_ for _ in range(1,11)]) for _ in range(5)]
lst2 = [random.choice([_ for _ in range(10,31)]) for _ in range(10)]

res = lst + lst2

print(res)