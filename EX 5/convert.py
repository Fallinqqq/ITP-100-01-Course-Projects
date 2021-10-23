# Grace Foster
# ITP 100-01
# EXERCISE 05A
# convert.py
# -----------------------------------------------------

def convert_feet(feet_to_convert):
    result = feet_to_convert * 12
    return result


def convert_inches(inches_to_convert):
    result = inches_to_convert * 2.54
    return result


print("------------------------------------------------")
print("Simple feet to inches to centimeters converter.")
print("------------------------------------------------")

feet = int(input("Please enter the number of feet: "))

print("------------------------------------------------")
inches = convert_feet(feet)
print(f' {feet} feet = {inches} inches')

print("------------------------------------------------")
centimeters = convert_inches(inches)
print(f' {inches:.2f} inches = {centimeters} centimeters')

print("------------------------------------------------")
print("The program has completed normally.")
print("------------------------------------------------")
