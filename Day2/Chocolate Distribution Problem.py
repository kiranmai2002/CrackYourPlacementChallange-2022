l=[]
for i in range(n):
    a=int(input(""))
    l.append(a)
m=int(input("Enter no. of students"))
if m>len(l):
     print("not possible")
else:
    l.sort()
    print(l)
    if(m<len(l)):
        min=l[m-1]-l[0]
        k=0
        for i in range(1,len(l)-m+1):
            if(l[i+m-1]-l[i]<min):
                min=l[i+m-1]-l[i]
                k=i
    print("Min Difference:", min)
    print(l[k:k+m])
