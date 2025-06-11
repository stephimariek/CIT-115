# Ask for class or work length in minutes.
# Determine hours and minutes length

# Declare a constant of 60 minutes in a hour: 
nMINUTES_IN_HOUR = 60

#1. Input:
iMinutes = int(input("How many minutes is your class or work shift in whole numbers: "))

# 3. Compute

# 3.1 get hours using integer division:

iHours = int(iMinutes / 60)

# 3.2 get minutes using modulus division to get remainder
#     as a whole number:

iLeftover = int(iMinutes % 60)

# 4. Output:

print(iMinutes, "minutes is:", iHours, "hour(s) and", iLeftover, "minutes")


      
