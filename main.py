# defining time periods in days
time_dictionary = {
    "days_dict": {
        "week": 7,
        "month": 30,
        "quarter": 90,  # 3 months times 30 days
        "year": 365
    },
    "week_dict": {
        "week": 1,
        "month": 4,
        "quarter": 12,
        "year": 52
    }
}

## simple interest formula, A = P(1+rt)
## P is the principal
## r = interest rate PER YEAR as a decimal
## t = time in YEARS elapsed
## simple interest WITH principal

# keeping variables empty for later appending by assigning None
principal = None
interest_rate = None
time = None
total_amount = None

## SIMPLE INTEREST VS COMPOUND COMPARISON

print("Simple Interest Account")
principal = (int(input("Enter the principal amount in $: ")))
interest_rate = (int(input("Enter the interest rate without the percentage sign: ")))
time = input("Enter the interest rate time unit (year, quarter, month, week, day): ")

# calculate simple interest
total_amount = principal*(1 + interest_rate)
print(total_amount)