n = int(input())

for i in range(n):
    st = input()
    
    odd = ''
    even = ''
    
    for j in range(len(st)):
        if(j%2 == 0):
            even += st[j]
        else:
            odd += st[j]

    print(even+' '+odd)