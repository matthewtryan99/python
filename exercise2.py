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
# my_string = "This is my string"
# back_list = []
# my_string_list = list(my_string)
# while len(my_string_list) > 0:
#     last_letter = my_string_list.pop()
#     back_list.append(last_letter)
# back_string = "".join(back_list)
# print(back_string)

###Medium Questions
##Question 1
# list1 = [2, 4, 5]
# list2 = [2, 3, 6]
# answers = []

# for num in range(len(list1)):
#     answer = list1[num] * list2[num]
#     answers.append(answer)
# print(answers)

##Question 2
# list1 = [[1,3], [2,4]]
# list2 = [[5,2], [1,0]]
# new_list = []
# inner_list = []

# for outer in range(len(list1)):
#     for inner in range(2):
#         answer = list1[outer][inner] + list2[outer][inner]
#         inner_list.append(answer)
#     new_list.append(inner_list)
#     inner_list = []
# print(new_list)

##Question 3
# list1 = [[1,3,4, 3], [2,4,2, 4]]
# list2 = [[5,2,5,3], [1,0,2, 4]]
# new_list = []
# inner_list = []


# for outer in range(len(list1)):
#     for inner in range(len(list1[0])):
#         if len(list1[outer]) == len(list2[outer]):
#             answer = list1[outer][inner] + list2[outer][inner]
#             inner_list.append(answer)
#         else:
#             print("Your matrices are not the same size.")
#             break
#     new_list.append(inner_list)
#     inner_list = []
# print(new_list)

##Question 4
# lst = [1, 5, 4, 5, 2, 5, 1, 3, 0, 8, 8, 3, 9]
# new_lst = []
# for i in lst:
#     if i not in new_lst:
#         new_lst.append(i)
# print(lst)
# print(new_lst)

##Question 5
# normal_sentence = "I am a leet programmer".upper()
# leet_list = list(normal_sentence)
# for i in range(len(leet_list)):
#     if leet_list[i] == 'A':
#         leet_list[i] = '4'
#     elif leet_list[i] == 'E':
#         leet_list[i] = '3'
#     elif leet_list[i] == 'G':
#         leet_list[i] = '6'
#     elif leet_list[i] == 'I':
#         leet_list[i] = '1'
#     elif leet_list[i] == 'O':
#         leet_list[i] = '0'
#     elif leet_list[i] == 'S':
#         leet_list[i] = '5'
#     elif leet_list[i] == 'T':
#         leet_list[i] = '7'
# leet_sentence = "".join(leet_list)
# print(leet_sentence.lower())

##Question 6

##Question 7
cipher = "lbh zhfg hayrnea jung lbh unir yrnearq"
cipher_list = list(cipher)
decoded_list = []
for i in cipher_list:
    if i == 'a':
        decoded_list.append('n')
    elif i == 'b':
        decoded_list.append('o')
    elif i == 'c':
        decoded_list.append('p')
    elif i == 'd':
        decoded_list.append('q')
    elif i == 'e':
        decoded_list.append('r')
    elif i == 'f':
        decoded_list.append('s')
    elif i == 'g':
        decoded_list.append('t')
    elif i == 'h':
        decoded_list.append('u')
    elif i == 'i':
        decoded_list.append('v')
    elif i == 'j':
        decoded_list.append('w')
    elif i == 'k':
        decoded_list.append('x')
    elif i == 'l':
        decoded_list.append('y')
    elif i == 'm':
        decoded_list.append('z')
    elif i == 'n':
        decoded_list.append('a')
    elif i == 'o':
        decoded_list.append('b')
    elif i == 'p':
        decoded_list.append('c')
    elif i == 'q':
        decoded_list.append('d')
    elif i == 'r':
        decoded_list.append('e')
    elif i == 's':
        decoded_list.append('f')
    elif i == 't':
        decoded_list.append('g')
    elif i == 'u':
        decoded_list.append('h')
    elif i == 'v':
        decoded_list.append('i')
    elif i == 'w':
        decoded_list.append('j')
    elif i == 'x':
        decoded_list.append('k')
    elif i == 'y':
        decoded_list.append('l')
    elif i == 'z':
        decoded_list.append('m')
    elif i == ' ':
        decoded_list.append(' ')

decoded = ''.join(decoded_list)

print(decoded)