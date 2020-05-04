a = 'HelLoWOrld'
a = a.lower()


b = []
c = []

a = sorted(a)

print(a)

for i,j,k in zip(a[::],a[1::],a[2::]):
    if (i == j == k:
        b.append(i+j+k)
        a.remove(i)
        a.remove(j)
        a.remove(k)
        
for i,j in zip(a[::],a[1::]):
    if i==j:
        b.append(i+j)
        a.remove(i)
        a.remove(j)
        
for i in a:
    b.append(i)
    

    

        

        
b = sorted(b)
print(b)
for i,j in zip(b[::],b[::-1]):
    c.append(i)
    c.append(j)
    
r = ''.join(c[:len(b)])
print(r)

    

