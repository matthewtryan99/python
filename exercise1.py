# # Question 1
# total_bill_amount = float(input("Enter the amount of the bill: "))
# service = ""
# tip_percent = 0

# while True:
#     service = input("Was the service good, fair, or bad: ").lower()
#     if service == "good" or service == "fair" or service == "bad":
#         break

# if service == "good":
#     tip_percent = .2
# elif service == "fair":
#     tip_percent = .15
# else:
#     tip_percent = .1

# tip_amount = total_bill_amount * tip_percent
# final_bill = tip_amount + total_bill_amount

# print(tip_amount)
# print(final_bill)

# #Question 2
# should_split = ''

# while should_split != 'y' and should_split != 'n':
#     should_split = input('Would you like to split the check?(y/n): ').lower()

# if should_split == 'y':
#     how_many = int(input("how many people?: "))
# else:
#     print(tip_amount)
#     print(final_bill)

# each_person_pays = final_bill / how_many

# print("Each person pays: ", each_person_pays)

# #Question 3
# print("You have 0 coins.")
# coins = 0
# response = ''

# while True:
#     response = input('Do you want another coin?: ').lower()
#     if response == 'yes':
#         coins += 1
#         print(f"You have {coins} coins.")
#     elif response == 'no':
#         break
#     else:
#         print('That is not a yes or no answer.')

# print(f"You have ended with {coins} coins.")

# #Question 4
#(other option is to multiply by the character)
# width = input("Width?")
# height = input("Height?")
# counter = 0
# width_string = ""
# height_string = ""
# height_space = ""

# while counter < int(width):
#     width_string += '*'
#     counter += 1

# counter = 0
# while counter < (int(width) - 2):
#     height_space += ' '
#     counter += 1
# if int(width) == 1 and int(height) == 1:
#     print("*")
# elif int(height) == 1:
#     print(width_string)
# else:
#     counter = 0
#     print(width_string)
#     while counter < (int(height) - 2):
#         height_string = f"*{height_space}*"
#         print(height_string)
#         counter += 1
#     print(width_string)

# #Question 5
# print("""
#    *
#   ***
#  *****
# *******
# """)

#Question 6
first_number = 1
second_number = 1

while first_number <= 10:
    answer = first_number * second_number
    print(f'{first_number} * {second_number} = {answer}')
    if second_number == 10:
        first_number += 1
        second_number = 1
        print("")
    second_number += 1