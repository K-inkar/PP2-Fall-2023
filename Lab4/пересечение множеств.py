ist1 =[int(i) for i in input().split()]
list2 =[int(i) for i in input().split()]

set = sorted(set(list1) & set(list2))

for num in set:
    print(num,  end=' ')