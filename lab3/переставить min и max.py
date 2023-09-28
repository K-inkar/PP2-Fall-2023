lst = [int(x) for x in input().split()]
min_index = lst.index(min(lst))
max_index = lst.index(max(lst))
lst[min_index], lst[max_index] = lst[max_index], lst[min_index]
for element in lst:
    print(element, end=' ')