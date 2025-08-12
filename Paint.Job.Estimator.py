import math

def main():
    #User input w/ validation
    fSquareFeet = getFloatInput("Enter wall space in square feet: ", .01)
    fPaintPrice = getFloatInput("Enter paint price per gallon: ", .01)
    fFeetPerGallon = getFloatInput("Enter feet per gallon: ", .01)
    fLaborHoursPerGallon = getFloatInput("How many labor hours per gallon: ", .01)
    fLaborChargePerHour = getFloatInput("Labor charge per hour: ", .01)
    sState = input("What state is the job in?: ")
    sCustomerLastName = input("Customer Last Name: ")

    #Calculations
    iTotalGallons = getGallonsOfPaint(fSquareFeet, fFeetPerGallon)
    fLaborHours = getLaborHours(fLaborHoursPerGallon, iTotalGallons)
    fLaborCost = getLaborCost(fLaborHours, fLaborChargePerHour)
    fPaintCost = getPaintCost(iTotalGallons, fPaintPrice)
    fSalesTaxRate = getSalesTax(sState)
    fTaxAmount = (fPaintCost + fLaborCost) * fSalesTaxRate
    fTotalCost = showCostEstimate(fPaintCost, fLaborCost, fSalesTaxRate)


    #Print Output
    print(f"Gallons of paint: {iTotalGallons}")
    print(f"Hours of labor: {fLaborHours:.1f}")
    print(f"Paint charges: ${fPaintCost:,.2f}")
    print(f"Labor charges: ${fLaborCost:,.2f}")
    print(f"Tax: ${fTaxAmount:.2f}")
    print(f"Total cost: ${fTotalCost:,.2f}")

    #File Name
    sFileName = sCustomerLastName + "_PaintJobOutput.txt"

    #File Output
    Paint = open('_PaintJobOutput.txt', 'w')
    Paint.write(f"Gallons of paint: {iTotalGallons}\n")
    Paint.write(f"Hours of labor: {fLaborHours:.1f}\n")
    Paint.write(f"Paint charges: ${fPaintCost:.2f}\n")
    Paint.write(f"Labor charges: ${fLaborCost:.2f}\n")
    Paint.write(f"Tax: ${fTaxAmount:.2f}\n")
    Paint.write(f"Total cost: ${fTotalCost:.2f}\n")
    Paint.close()

    #Confirm file creation
    print(f"File: {sFileName} was created.")

# Validation function > minNumberAllowed
def getFloatInput(sPrompt, fMinNumberAllowed):
    fValue = -1
    while fValue < fMinNumberAllowed:
        try:
            fValue = float(input(sPrompt))
            if fValue < fMinNumberAllowed:
                print("Input must be a numeric value greater or equal to:", fMinNumberAllowed)
        except ValueError:
            print("Input must be a numeric value greater or equal to:", fMinNumberAllowed)
    return fValue

# Gallons of paint needed to the next whole number
def getGallonsOfPaint(fSquareFeet, fFeetPerGallon):
    return math.ceil(fSquareFeet / fFeetPerGallon)

# Calculate total labor hours
def getLaborHours(fLaborHoursPerGallon, iTotalGallons):
    return fLaborHoursPerGallon * iTotalGallons

# Calculate total labor cost
def getLaborCost(fLaborHours, fLaborChargePerHour):
    return fLaborHours * fLaborChargePerHour

# Calculate total paint cost
def getPaintCost(iTotalGallons, fPaintPrice):
    return iTotalGallons * fPaintPrice

#Tax rate based on state
def getSalesTax(sState):
    fTaxRate = 0
    if sState == "CT":
        fTaxRate = .06
    elif sState == "MA":
        fTaxRate = .0625
    elif sState == "ME":
        fTaxRate = .085
    elif sState == "NH":
        fTaxRate = .0
    elif sState == "RI":
        fTaxRate = .07
    elif sState == "VT":
        fTaxRate = .06     
    return fTaxRate

#Return total cost including tax
def showCostEstimate(fPaintCost, fLaborCost, fSalesTaxRate):
    fSubtotal = fPaintCost + fLaborCost
    fTotal = fSubtotal + (fSubtotal * fSalesTaxRate)
    return fTotal

main()
