###Medium Questions
##Question 1
# input_word = input("Input a word: ")
# input_list = list(input_word)
# my_dict = {}

# for i in range(len(input_list)):
#     if input_list[i] not in my_dict:
#         my_dict[input_list[i]] = 1
#     else:
#         my_dict[input_list[i]] += 1

# print(my_dict)

# ##Small Question 2
# ramit = {
# 'name': 'Ramit',
# 'email': 'ramit@gmail.com',
# 'interests': ['movies', 'tennis'],
# 'friends': [
#     {
#     'name': 'Jasmine',
#     'email': 'jasmine@yahoo.com',
#     'interests': ['photography', 'tennis']
#     },
#     {
#     'name': 'Jan',
#     'email': 'jan@hotmail.com',
#     'interests': ['movies', 'tv']
#     }
# ]
# }
#  print(ramit['email'])
#  print(ramit['interests'][0])
#  print(ramit['friends'][0]['email'])
#  print(ramit['friends'][1]['interests'][1])

##Small Question 3
# def friend_count(diction):
#     diction['friend_count'] = 0
#     for i in range(len(diction['friends'])):
#         diction['friend_count'] += 1
#     return diction

# new_dict = friend_count(ramit)

# print(new_dict['friend_count'])

##Question 2
# input_word = input("Input a sentence: ")
# input_list = input_word.split()
# my_dict = {}

# for i in range(len(input_list)):
#     if input_list[i] not in my_dict:
#         my_dict[input_list[i]] = 1
#     else:
#         my_dict[input_list[i]] += 1

# print(my_dict)

##Question 3
input_word = input("Input a sentence: ")
input_list = input_word.split()
my_dict = {}

for i in range(len(input_list)):
    if input_list[i] not in my_dict:
        my_dict[input_list[i]] = 1
    else:
        my_dict[input_list[i]] += 1

dict_tuple = my_dict.items()
test_value = 0
test_key = ''
new_lst = [[0,0],[0,0],[0,0]]
i = 0



# for key, value in dict_tuple:
#     if key != new_lst[0][0] or key != new_lst[1][0] or key != new_lst[2][0]:
#         if value >= test_value and i < 3:
#             test_value = value
#             test_key = key
#             i += 1
#         elif i >= 3:
#             break
#         new_lst[i - 1][0] = test_key
#         new_lst[i - 1][1] = test_value
#     test_value = 0


    # new_lst.append([test_key, test_value])

# print(new_lst[:3])

# def top_words(tple, i):
#     for key, value in tple:
#         if key != new_lst[i][0] or key != new_lst[1][0] or key != new_lst[2][0]:
#             if value >= test_value and i < 3:
#                 test_value = value
#                 test_key = key
#                 i += 1
#             elif i >= 3:
#                 break
#             new_lst[i - 1][0] = test_key
#             new_lst[i - 1][1] = test_value
#         test_value = 0