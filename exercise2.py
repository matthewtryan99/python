###Small exercises
##Question 1
# numbers = [1, 2, 3, 4, 5]
# sum = 0
# for num in numbers:
#     sum += num
# print(sum)

##Question 2
# numbers = [4, 6, 2, 9, 5]
# largest = numbers[0]
# for num in numbers:
#     if num > largest:
#         largest = num
# print(largest)

##Question 3
# numbers = [4, 6, 2, 9, 5]
# smallest = numbers[0]
# for num in numbers:
#     if num < smallest:
#         smallest = num
# print(smallest)

#Question 4
# numbers = [4, 6, 2, 9, 5]
# even_list = []
# for num in numbers:
#     if num % 2 == 0:
#         even_list.append(num)
# print(even_list)

#Question 5
# numbers = [(-4), 6, 2, (-9), 5]
# num_over_0 = []
# for num in numbers:
#     if num > 0:
#         num_over_0.append(num)
# print(num_over_0)

#Question 6
# numbers = [8, 5, 2, 12, 5, 13]
# even_list = []
# for num in numbers:
#     if num % 2 == 0:
#         even_list.append(num)
# print(even_list)

##Question 7
# numbers = [4, 6, 2, 9, 5]
# single_factor = 5
# new_list = []
# for num in numbers:
#     new_list.append(num * single_factor)
# print(new_list)

##Question 8
my_string = "This is my string"
back_list = []
my_string_list = list(my_string)
while len(my_string_list) > 0:
    last_letter = my_string_list.pop()
    back_list.append(last_letter)
back_string = "".join(back_list)
print(back_string)
