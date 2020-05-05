def pal(a):
    if a[::]== a[::-1]:
        print(len(a))
    else:
        b = a[::-1]
        c = int(a)+int(b)
        c = str(c)
        pal(c)

a = input()
pal(a)
    
