###Medium Questions
##Question 1
# def smallest_number(lst):
#     smallest = lst[0]
#     for i in lst:
#         if i < smallest:
#             smallest = i
#     return smallest

# print(smallest_number([1,2,4,7,5,3,5,]))

##Question 2
def largest_number(lst):
    largest = lst[0]
    for i in lst:
        if i > largest:
            largest = i
    return largest

print(largest_number([1,2,4,7,5,3,5,]))