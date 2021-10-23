# Grace Foster
# ITP100
# EXERCISE: 04
# rcheck.py
# -----------------------------
print("----------------------------------------------------------------")
print("--                       Check Calculator                     --")
print("----------------------------------------------------------------")
print(f'This script calculates a restaurant check by including the tax and tip.')
print("----------------------------------------------------------------")
tax_rate = 18
tip_rate = float(input("Enter your tip percent (example 0.17): "))
print(f'Tax rate is: {tax_rate}%')
print(f'Tip Percent is: {round(tip_rate * 100)}%')
print("----------------------------------------------------------------")
check_amount = float(input("Enter the amount of the check: "))
tax_amount = (check_amount/100) * tax_rate
tip_amount = check_amount * tip_rate
total_amount = check_amount + tax_amount + tip_amount
print("----------------------------------------------------------------")
print(f'The total check is ${round(total_amount, 2):.2f} which includes ${round(tax_amount, 2):.2f} tax amount and ${round(tip_amount, 2):.2f} tip.')
