principal = float(input("Enter Principal amount (P) :"))
rate = float(input("Enter annual interest Rate (R) :"))
time = float(input("Enter Time in years (T) :"))


simple_interest = (principal * rate * time) / 100
total_amount = principal + simple_interest

print(f"Simple Interest (SI): {simple_interest}")
print(f"Total Amount Payable: {total_amount}")