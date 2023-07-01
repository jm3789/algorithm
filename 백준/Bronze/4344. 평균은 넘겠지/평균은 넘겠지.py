num= int(input())

def mobumrate():
    a= input().split()
    a= list(map(int, a))
    b= a[1:]
    average= sum(b)/len(b)
    mobum=0
    for j in range(0, a[0]):
        if b[j] > average:
           mobum+=1
    return mobum/a[0]*100
 
for _ in range(1, num+1):
    m= mobumrate()
    print("{:.3f}%".format(round(m, 3)))
