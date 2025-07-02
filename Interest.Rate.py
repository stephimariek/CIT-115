#Input
PV = float(input("Enter the starting principal: "))
R = float(input("Enter the annual interest rate: ")) / 100
M = float(input("How many times per year is the interest compounded? "))
T = int(input("For how many years will the account earn interest? "))



#Calculations

fTotal = float(PV*(1+(R/M))**(M*T))



#Output

print(f"At the end of {T} years you will have $ {fTotal: ,.2f}")
