# Flooring calculator

# 1.Input both the Length and Width:

nLength = float(input("What is the length: "))

nWidth = float(input("What is the width: "))

# 2. Calculate
# 2.1 Area is Length x Width

nArea = float(nLength * nWidth)

# 2.2 Scrap is 10% of the calculated area:

nScrap = float(nArea * 0.10)

# 2.2 Total is Area + Scrap

nTotal = float(nArea + nScrap)

#2.3 Total Square Yards

nYards = float(nTotal / 9)


# 3. Output:
#    Area of the room:
#    Scrap value:
#    Total of Area + Scrap:
#    Total Square Yards which is Total / 9
print("Area of the room:      " + format(nArea,'15,.1f'))
print("Scrap value:           " + format(nScrap,'15,.1f'))
print("Total of Area + Scrap: " + format(nTotal,'15,.1f'))
print("Total Sqaure Yards:    " + format(nYards,'15,.1f'))
