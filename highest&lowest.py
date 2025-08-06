l=[5,12,8,9,11,15]
high=l[0]
low=l[0]
for i in range(len(l)):
    if l[i]>high:
        
        high=l[i]
    elif low>l[i] :
       
        low=l[i]
print(low)
print(high)
print(max(l))
print(min(l))



