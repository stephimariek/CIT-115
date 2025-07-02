print("Steph's Temp Converter!")

fTemp = float(input("Enter a temperature: "))
    
sConversion = input("Is the temp F for Fahrenheit or C for Celsius? ")

if sConversion == "F" or sConversion == "f":
    sMessage = "Celsius"
    if fTemp > 212:
        print("Temp can not be > 212") 
    else:
        Celsius = (5.0 / 9) * (fTemp - 32)
        print(f"The {sMessage} equivalent is {Celsius: .1f}")
elif sConversion == "C" or sConversion == "c":
    sMessage = "Farenheit"
    if fTemp > 100:
        print("Temp can not be >100") 
    else:
        Farenheit = ((9.0 / 5.0) * fTemp) + 32
        print(f"The {sMessage} equivalent is {Farenheit: .1f}")
        
else:
    print("You must enter a F or C")
    
   
