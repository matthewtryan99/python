###Medium Questions
##Question 1
input_word = input("Input a word: ")
input_list = list(input_word)
my_dict = {}

for i in range(len(input_list)):
    if input_list[i] not in my_dict:
        my_dict[input_list[i]] = 1
    else:
        my_dict[input_list[i]] += 1

print(my_dict)