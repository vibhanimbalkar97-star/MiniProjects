#rent calculator in python 

## Inputs we need from the user
# Total rent
# Total food ordered for snacking
# Electricity units spend
# Charge per unit 
# Persons living in room/flat

## Output
# Total amount you've to pay is

rent = int(input("Enter the total rent ="))
food = int(input("Enter total food order for snacking ="))
electricity_spend = int(input("Enter electricity units spend ="))
charge_per_unit = int(input("Enter charge per unit ="))
persons = int(input("Persons living in room/flat ="))

total_bill = electricity_spend * charge_per_unit
 
total_amount = (rent + food + total_bill)  // persons
print("Total amount you've to pay is =", total_amount)

