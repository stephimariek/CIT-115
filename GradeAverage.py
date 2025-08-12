#Input

sName = input("Name the person that we are calculating the grades for: ")

iTest1 = int(input("What is test score 1? "))
iTest2 = int(input("What is test score 2? "))
iTest3 = int(input("What is test score 3? "))
iTest4 = int(input("What is test score 4? "))


#Y or N

sDrop = input("Do you wish to drop the lowest grade Y or N? ")

if sDrop != "Y" and sDrop != "N":
    print("Enter Y or N to drop the lowest grade.")
    exit()

#Make sure test scores are > 0

if iTest1 < 0 or iTest2 < 0 or iTest3 < 0 or iTest4 < 0:
    print("Test scores must be greater than 0.")
    exit()
    
#Calculations

if sDrop == "Y":
    if iTest1 < iTest2 and iTest1 < iTest3 and iTest1 < iTest4:
        iToal = iTest2 + iTest3 + iTest4
    elif iTest2 < iTest1 and iTest2 < iTest3 and iTest2 < iTest4:
        iTotal = iTest1 + iTest3 + iTest4
    elif iTest3 < iTest1 and iTest3 < iTest2 and iTest3 < iTest4:
        iTotal = iTest1 + iTest2 + iTest4
    else:
        iTotal = iTest1 + iTest2 + iTest3
    fAverage = float(iTotal / 3)

else:
    iTotal = iTest1 + iTest2 + iTest3 + iTest4
    fAverage = float(iTotal / 4)


#Letter Grade

if fAverage >= 97.0:
    sGrade = "A+"
elif fAverage >= 94.0:
    sGrade = "A"
elif fAverage >= 90.0:
    sGrade = "A-"
elif fAverage >= 87.0:
    sGrade = "B+"
elif fAverage >= 84.0:
    sGrade = "B"
elif fAverage >= 80.0:
    sGrade = "B-"
elif fAverage >= 77.0:
    sGrade = "C+"
elif fAverage >= 74.0:
    sGrade = "C"
elif fAverage >= 70.0:
    sGrade = "C-"
elif fAverage >= 67.0:
    sGrade = "D+"
elif fAverage >= 64.0:
    sGrade = "D"
elif fAverage >= 60.0:
    sGrade = "D-"
    
else:
    sGrade = "F"

#Output
    
print(f"{sName} test average is: {fAverage: .1f}")
print(f"Letter grade for the test is: {sGrade}")


