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

##Question 2
ramit = {
'name': 'Ramit',
'email': 'ramit@gmail.com',
'interests': ['movies', 'tennis'],
'friends': [
    {
    'name': 'Jasmine',
    'email': 'jasmine@yahoo.com',
    'interests': ['photography', 'tennis']
    },
    {
    'name': 'Jan',
    'email': 'jan@hotmail.com',
    'interests': ['movies', 'tv']
    }
]
}
print(ramit['email'])
print(ramit['interests'][0])
print(ramit['friends'][0]['email'])
print(ramit['friends'][1]['interests'][1])