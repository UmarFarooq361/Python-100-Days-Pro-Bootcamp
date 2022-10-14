print("Welcome to the tip calculator.")
bill= float(input("What was your total bill ? $"))
percent= int(input("What percentage tip would you like to give ? 10 , 12 , 15 ?"))
people= int(input("How many people to split the bill ? "))

bill_tip = bill*percent/100

total_bill = bill+bill_tip
each_will_pay = round(total_bill/people, 2)
print(f"Each person will pay ${each_will_pay}")