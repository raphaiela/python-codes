import random

a = 0
for i in range(20):
    o = random.randint(0,100)
    if o > a:
        a = o
    print(o, end=" ")
print(a)