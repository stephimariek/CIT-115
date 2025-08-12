#Validate user input
def getFloatInput(prompt):
    while True:
        try:
            UserInput = input(prompt)
            value = float(UserInput)
            
            if value <= 0:
                print("Input a number that is greater than 0.")
            else:
                return value
        except ValueError:
            print("Input a number that is greater than 0.")

#Determine median
def getMedian(values):
    values.sort()  
    n = len(values)
    if n % 2 == 1:
        median = values[n // 2]
    else:
        median = (values[n // 2 - 1] + values[n // 2]) / 2
    return median

#Input user sales value
def main():
    sales = [] 
    
    while True:
        SalePrice = getFloatInput("Enter property sales value: ")
        sales.append(SalePrice)
       
        while True:
            AnotherEntry = input("Enter another value Y or N: ").lower()
            if AnotherEntry in ['y', 'n']:
                break
    
        if AnotherEntry == 'n':
            break

#Sort values    
    sales.sort()

    i = 1
    for price in sales:
        print(f"Property {i} $   {price:,.2f}")
        i += 1

    total_sales = 0
    for price in sales:
        total_sales += price
        
#Calculations    
    min_sale = sales[0]
    max_sale = sales[-1]
    average_sale = total_sales / len(sales)
    median_sale = getMedian(sales)
    commission = total_sales * 0.03

#Output
    print(f"Minimum:    $    {min_sale:,.2f}")
    print(f"Maximum:    $    {max_sale:,.2f}")
    print(f"Total:      $    {total_sales:,.2f}")
    print(f"Average:    $    {average_sale:,.2f}")
    print(f"Median:     $    {median_sale:,.2f}")
    print(f"Commission: $    {commission:,.2f}")

main()
