a = input().split(',')
a = list(map(int,a))
n1 = []
n2 = ''
for i in range(len(a)):
    if i not in range(a.index(5),a.index(8)+1):
        n1.append(a[i])
        
n1 = sum(n1)

for i in range(a.index(5),a.index(8)+1):
    a[i] = str(a[i])
    n2 += a[i]
    
print(n1+int(n2))
