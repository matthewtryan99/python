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

print(tip_amount)
print(final_bill)