# Grace Foster
# ITP 100-01
# EXERCISE 05B
# tuition.py
# -------------------------------------------------

print("College Tuition Increase Calculator")
print("---------------------------------------")

tuition = int(input("Enter The Current Annual Tuition (as int): $"))
per_year = int(input("Enter the % of increase per year (as int): %"))
num_years = int(input("Enter the number of years to project: "))

print("---------------------------------------")
print("Year\tProjected Tuition (per semester)")
print("---------------------------------------")

for year in range(num_years):
    print(f'{year + 1}\t\t${tuition:,.2f}')
    tuition_percentage = (tuition/100) * per_year
    tuition = tuition + tuition_percentage

print("\nProgram Terminated Properly")
