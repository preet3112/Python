# SI = P*N*R/100
principal=int(input("Enter the amount borrowed"))
years = float(input("Enter the period in years"))
rate = float(input("Enter rate of interest"))

interest = principal * years * rate /100

print("Simple interest on the principal amount "+str(principal)+" for a period of "+str(years)+" years at the rate of "+str(rate)+"% is: $"+str(interest))
#F Strings
print(f"Simple interest on the principal amount {principal} for a period of {years} years at the rate of {rate}% is: ${interest}")
