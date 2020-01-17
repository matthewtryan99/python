def smallest_number(lst):
    smallest = lst[0]
    for i in lst:
        if i < smallest:
            smallest = i
    return smallest

print(smallest_number([1,2,4,7,5,3,5,]))