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
# print(ramit['email'])
# print(ramit['interests'][0])
# print(ramit['friends'][0]['email'])
# print(ramit['friends'][1]['interests'][1])

##Question 3
def friend_count(diction):
    diction['friend_count'] = 0
    for i in range(len(diction['friends'])):
        diction['friend_count'] += 1
    return diction

new_dict = friend_count(ramit)

print(new_dict['friend_count'])