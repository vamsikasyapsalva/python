a = input()

a = list(a)

a = list(map(int,a))
b = []

for i in range(len(a)):
    if  i % 2 != 0:
        b.append(a[i])
        
def t(a):
    return a*a
    
s = list(map(t,b))

s = list(map(str,s))

print(''.join(s))
