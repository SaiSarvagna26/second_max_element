a=list(map(int,input().split()))
maxi=a[0]
list_a=[]

if len(a)<=1:
    print(-1)
else:
    
    for i in a:
        if i>maxi:
            maxi=i
    k=maxi
    for j in a:
        if j!=k:
            list_a=list_a+[j]
        
    sec_max_list_a=list_a[0]
    for i in list_a:
        if i>sec_max_list_a:
            sec_max_list_a=i
    print(sec_max_list_a)
