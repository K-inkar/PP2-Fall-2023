list1 = [int(i) for i in input().split()]
list2 = [int(i) for i in input().split()]

set = len(set(list1) & set(list2))

print(set)