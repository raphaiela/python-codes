import random

n = []
for i in range(20):
    o = random.randint(0,100)
   #print(f'{i+1}° : {o}')
    n.append(o)
    g = sorted(n)
print(g[-1])