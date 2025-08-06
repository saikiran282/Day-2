l=[5,12,8,9,11,15]
high=l[0]
high2=l[0]
for i in range(len(l)):
    if l[i]>high:
        high=l[i]
    elif high2<l[i]<high :
        high2=l[i]
if high!=high2:
    print(high)
    print(high2)
elif high==high2:
    print(high)
else:
    print(l)



