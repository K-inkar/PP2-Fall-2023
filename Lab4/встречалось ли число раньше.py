a = {}
 
list =input().split()

for num in list:
    
    if num in a:
        print("YES")
    else:
        print("NO")
        
        a[num]=True
        