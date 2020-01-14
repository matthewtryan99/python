# Question 1
total_bill_amount = float(input("Enter the amount of the bill: "))
service = ""
tip_percent = 0

while True:
    service = input("Was the service good, fair, or bad: ").lower()
    if service == "good" or service == "fair" or service == "bad":
        break

if service == "good":
    tip_percent = .2
elif service == "fair":
    tip_percent = .15
else:
    tip_percent = .1

tip_amount = total_bill_amount * tip_percent
final_bill = tip_amount + total_bill_amount

# print(tip_amount)
# print(final_bill)

#Question 2
should_split = ''

while should_split != 'y' and should_split != 'n':
    should_split = input('Would you like to split the check?(y/n): ').lower()

if should_split == 'y':
    how_many = int(input("how many people?: "))
else:
    print(tip_amount)
    print(final_bill)

each_person_pays = final_bill / how_many

print("Each person pays: ", each_person_pays)