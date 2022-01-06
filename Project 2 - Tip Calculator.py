# If the bill was $150.00, split between 5 people, with 12% tip. 
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Assign values to variables with input from user 
print("Welcome to Julie's tip calculator!\n")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))

# Convert tip in percentage 
tip_percent = tip / 100 
tip_percent += 1

# Split the bill 
bill_per_person = (bill / people) * tip_percent
bill_round_up = round(bill_per_person, 2)
bill_final = "{:.2f}".format(bill_round_up) # to ensure the two decimal places are included at the end 

# End message 
message = f"Each person should pay: ${bill_final}.\n"
print(message)
print("Thank you for using Julie's Tip Calculator!")
