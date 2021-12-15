# Grace Foster
# ITP 100-01
# Program 01 - Annual Rainfall
# rainfall.py
# -------------------------------------------------

linz = '---' * 20
print("Calculate total and average rain for a 12 month period")
print(linz)

total_rainfall = 0.0
average_rainfall = 0.0

for months in range(12):
    while True:
        try:
            total_rainfall = total_rainfall + float(input(f'Enter the rainfall amount for month {months + 1}: '))
            months = float(total_rainfall)
            average_rainfall = total_rainfall / 12
            break

        except ValueError:
            continue

linz = "---" * 19
print(linz)

print("For 12 months")
print(f'\tTotal rainfall:\t\t\t\t{total_rainfall:,.2f} inches')
print(f'\tAverage monthly rainfall:\t{average_rainfall:,.2f} inches')

linz = "---" * 18
print(linz)
print("The Program Successfully Terminated")
