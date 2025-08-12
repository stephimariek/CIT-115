#Deposit input
while True:
    try:
        fDeposit = float(input("What is the Original Deposit (positive value): "))
        if fDeposit <= 0:
            print("Input must be a positive numeric value")
        else:
            break
    except ValueError:
        print("Input must be a positive numeric value")

#Interest rate input
while True:
    try:
        fInterest_Rate = float(input("What is the Interest Rate (positive value): "))
        if fInterest_Rate <= 0:
            print("Input must be a positive numeric value")
        else:
            break
    except ValueError:
        print("Input must be a positive numeric value")

#Number of months input
while True:
    try:
        iMonths = int(input("What is the Number of Months (positive value): "))
        if iMonths <= 0:
            print("Input must be a positive numeric value")
        else:
            break
    except ValueError:
        print("Input must be a positive numeric value")

#Goal amount input
while True:
    try:
        fGoal = float(input("What is the Goal Amount (can enter 0 but not negative)): "))
        if fGoal < 0:
            print("Input must 0 or greater")
        else:
            break
    except ValueError:
        print("Input must 0 or greater")

#Conversion
fMonthly_Rate = (fInterest_Rate / 100) / 12

#Month Loop
for i in range(1, iMonths + 1):
    fInterest = fDeposit * fMonthly_Rate
    fDeposit += fInterest
    print(f"Month: {i} Account Balance is: $ {fDeposit:,.2f}")

#Goal Loop
if fGoal > 0:
    while fDeposit < fGoal:
        fInterest = fDeposit * fMonthly_Rate
        fDeposit += fInterest
        iMonths += 1
    print(f"It will take: {iMonths} months to reach the goal of $ {fGoal:,.2f}")

