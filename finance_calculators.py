import math
# let the user see whats on the menu
print("Invesetment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")
# let user choose either investment or bond
user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")
# if user chooses investment then 
# ask the user how much they are depositing
# ask what is there interest rate
# how many years they plan on investing
if user_choice == "investment":
    deposit =  int(input("How much are you  depositing: "))
    interest_rate = int(input("What is your interest rate (just the number not the percentage ): "))
    years_investing = int(input("The number of years they plan on investing: "))
# ask the user to input if they want “simple” or “compound” interest
# output the appropriate amount that they will get back after the given period,at the specified interest rate
    print("Do you  want “simple” or “compound” interest: ")
    interest = input("Enter 'compound' or 'simple' interest:  ")
# this is the compound calculation
    if interest in ["compound"]:
        total_compound = deposit * math.pow ((1 + interest_rate/100),years_investing)
        print(f"Your total investment is R{round(total_compound, 2)}")
# this is the simple calculation 
    elif interest in ["simple"]:
        total_interest = deposit * (1 + interest_rate * years_investing / 100)
        print(f"Your total investment is R{round(total_interest)}")
#  if user chooses bond then
# ask the user what is  present value of the house
# ask the user what is the interest rate
# ask the user the number of months they plan to take to repay the bond.
if user_choice in ["bond"]:
    value_house = int(input("What is the present value of the house: "))
    rate_interest = int(input("What is the interest rate: "))
    repay_bond = int(input("Enter the number of months they plan to take to repay the bond: "))
#  the calculation of the bond repayment formula
    i = (rate_interest/100)/12
    monthly_repayment = (i * value_house) / (1 - math.pow((1 + i), -repay_bond))
    print(f"Your total bond is R{round(monthly_repayment, 2)}")