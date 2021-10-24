# Grace Foster
# ITP 100-01
# EXERCISE: 06
# ageclass.py
# ----------------------------------------------------------------

print("Classification program")
print("-----------------------------------------------")

age = 1
while age > 0:

    age = float(input(f'Enter the age: '))

    if age != 0:

        if age <= 1:
            print("This person is an Infant.")
        elif 2 <= age <= 12:
            print("This person is a Child.")
        elif 13 <= age <= 19:
            print("this person is a Teenager.")
        elif age >= 20:
            print("This person is an Adult.")

print("-----------------------------------------------")
print("The Program Has Ended.")
