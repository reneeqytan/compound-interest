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
    },
    "years_dict": {
        "week": 1 / 52,
        "month": 1 / 12,
        "quarter": 1 / 4,
        "day": 1 / 365,
        "year": 1,
    }
}

## simple interest formula, A = P(1+rt)
## P is the principal
## r = interest rate PER YEAR as a decimal
## t = time in YEARS elapsed
## simple interest WITH principal

# keeping variables empty for later appending by assigning None
principal = None
interest_rate_percentage = None
time_unit = None  # how often interest is added e.g. year, week, etc.
time_elapsed = None  # how much time passes in the units of time_unit, e.g. 4, 5
time_period = None  # time elapsed and time unit multiplied, provides a final time e.g. 4 years, 5 month etc.
total_amount = None

## SIMPLE INTEREST VS COMPOUND COMPARISON

print("Simple Interest Account")
principal = (int(input("Enter the principal amount in $: ")))
interest_rate_percentage = (int(input("Enter the interest rate without the percentage sign: ")))
time_unit = input("Enter the interest rate time unit (year, quarter, month, week, day): ")
time_elapsed = int(input("Enter the number of the previous time unit the interest will be calculated for: "))

# calling dictionary values which were preassigned. getting the years_dict cause it's annual calculation
if time_unit == "year":
    time_period = time_dictionary["years_dict"]["year"] * time_elapsed # the number of years elapsed calculation to get the final time period
elif time_unit == "quarter":
    time_period = time_dictionary["years_dict"]["quarter"] * time_elapsed
elif time_unit == "month":
    time_period = time_dictionary["years_dict"]["month"] * time_elapsed
elif time_unit == "week":
    time_period = time_dictionary["years_dict"]["week"] * time_elapsed
elif time_unit == "day":
    time_period = time_dictionary["years_dict"]["day"] * time_elapsed

interest_rate_decimal = interest_rate_percentage / 100  # converting the interest rate % to a decimal by dividing 100

# calculate simple interest, following formula of A = P(1 + rt)
total_amount = round(principal * (1 + interest_rate_decimal * time_period), 2)  # rounding to 2 dec places cause cents
print(total_amount)
