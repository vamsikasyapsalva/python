import itertools
a = input().split(',')
b = int(input())
a = list(map(int,a))
c = 0

for i in itertools.combinations(a,4):
    if sum(i) == b:
        c += 1
        
print(c)
