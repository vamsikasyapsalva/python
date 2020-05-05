s = input()
l = []
d = { 'a':"", 'b':"", 'c':"", 'd':"", 'e':"", 'f':"", 'g':"", 'h':"", 'i':"", 'j':"", 'k':"", 'l':"",
         'm':"", 'n':"", 'o':"", 'p':"", 'q':"", 'r':"", 's':"", 't':"", 'u':"", 'v':"", 'w':"", 'x':"",
             'y':"", 'z':""}
for each in s:
    d[each.lower()] += each
for each in sorted(d.keys()):
    if(d[each] != ""):
        l.append(d[each])
while(len(l)>1):
    print(l.pop(0),end="")
    print(l.pop(-1),end="")
if(len(l)>0):
    print(l.pop(0))
