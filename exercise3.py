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
# def largest_number(lst):
#     largest = lst[0]
#     for i in lst:
#         if i > largest:
#             largest = i
#     return largest

# print(largest_number([1,2,4,7,5,3,5,]))

##Question 3
# def shortest_string(lst):
#     shortest = lst[0]
#     for i in lst:
#         if len(i) < len(shortest):
#             shortest = i
#     return shortest

# print(shortest_string(['long', 'longer', 'short', 'the', 'to']))

##Question 4
def longest_string(lst):
    longest = lst[0]
    for i in lst:
        if len(i) > len(longest):
            longest = i
    return longest

print(longest_string(['long', 'longer', 'short', 'the', 'to']))