# Grace Foster
# CVC292.ITP 100.02RA.FA21
# Assignment Exercise:03
# Program	initials.py

# The purpose of this program is to get the initials from a persons full name.

full_name = input("Enter your full name:")
names = full_name.split(' ')

first_name = names[0]
first_letter = first_name[0]


middle_name = names[1]
middle_letter = middle_name[0]


last_name = names[2]
last_letter = last_name[0]

print(f'{first_letter.upper()}.{middle_letter.upper()}.{last_letter.upper()}')
