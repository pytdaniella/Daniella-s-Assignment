
# tax_calculator.py
# This program calculates U.S. federal personal income tax for the year 2009
# based on filing status and taxable income.

def calculate_tax(status, income):
    tax = 0

    # Tax brackets for each filing status
    brackets = {
        0: [(8350, 0.10), (33950, 0.15), (82250, 0.25), (171550, 0.28), (372950, 0.33), (float('inf'), 0.35)],  # Single
        1: [(16700, 0.10), (67900, 0.15), (137050, 0.25), (208850, 0.28), (372950, 0.33), (float('inf'), 0.35)], # Married filing jointly
        2: [(8350, 0.10), (33950, 0.15), (68525, 0.25), (104425, 0.28), (186475, 0.33), (float('inf'), 0.35)], # Married filing separately
        3: [(11950, 0.10), (45500, 0.15), (117450, 0.25), (190200, 0.28), (372950, 0.33), (float('inf'), 0.35)] # Head of household
    }

    previous_limit = 0

    for limit, rate in brackets[status]:
        if income > limit:
            tax += (limit - previous_limit) * rate
            previous_limit = limit
        else:
            tax += (income - previous_limit) * rate
            break

    return tax


# Main program
print("U.S. Federal Personal Income Tax Calculator (2009)")
print("Filing Status Options:")
print("0 - Single filer")
print("1 - Married filing jointly or qualified widow(er)")
print("2 - Married filing separately")
print("3 - Head of household")

status = int(input("Enter your filing status (0-3): "))
income = float(input("Enter your taxable income: $"))

tax = calculate_tax(status, income)

print(f"\nYour total tax is: ${tax:.2f}")
