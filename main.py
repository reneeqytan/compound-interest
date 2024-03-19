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
#principal = None
#interest_rate_percentage = None
#time_unit = None  # how often interest is added e.g. year, week, etc.
#time_elapsed = None  # how much time passes in the units of time_unit, e.g. 4, 5
#time_period = None  # time elapsed and time unit multiplied, provides a final time e.g. 4 years, 5 month etc.
#total_amount = None

## SIMPLE INTEREST VS COMPOUND COMPARISON

print("Simple Interest Account")
principal_si = (int(input("Enter the principal amount in $: ")))
interest_rate_percentage_si = (int(input("Enter the interest rate without the percentage sign: ")))
time_unit_si = input("Enter the interest rate time unit (year, quarter, month, week, day): ")
time_elapsed = int(input("Enter the number of the previous time unit the interest will be calculated for: "))

# calling dictionary values which were preassigned. getting the years_dict cause it's annual calculation

def define_time_period():
    if time_unit_si == "year":
        time_period_si = time_dictionary["years_dict"]["year"] * time_elapsed # the number of years elapsed calculation to get the final time period
    elif time_unit_si == "quarter":
        time_period_si = time_dictionary["years_dict"]["quarter"] * time_elapsed
    elif time_unit_si == "month":
        time_period_si = time_dictionary["years_dict"]["month"] * time_elapsed
    elif time_unit_si == "week":
        time_period_si = time_dictionary["years_dict"]["week"] * time_elapsed
    elif time_unit_si == "day":
        time_period_si = time_dictionary["years_dict"]["day"] * time_elapsed
    return time_period_si

interest_rate_decimal = interest_rate_percentage_si / 100  # converting the interest rate % to a decimal by dividing 100

time_period_si = define_time_period()

# calculate simple interest, following formula of A = P(1 + rt)
total_amount = round(principal_si * (1 + interest_rate_decimal * time_period_si), 2)  # rounding to 2 dec places cause cents
print(total_amount)

### COMPOUND INTEREST CALCULATION

## compound interest = P(1 + r/n)^nt
## r = interest rate (as a decimal)
## n = number of times interest applied per time period (time period usually means year)
## t = number of time periods elapsed

# need a new variable for n...

print("Compound Interest Account")
principal = int(input("Enter the principal amount in $: "))
interest_rate_percentage = float(input("Enter the interest rate (enter 7% as 7): "))
time_unit = input("Enter the interest rate time unit (year, quarter, month, week, day): ")
compounding_period_unit = input("Enter the compounding period time unit (year, quarter, month, week, day, custom): ")
projection_time_unit = input("Enter the projection time unit (year, quarter, month, week, day): ")
projection_time = int(input("Future projection timeframe for both accounts. Enter the amount of time to project into the future: "))


# Convert interest rate to a decimal
interest_rate_decimal = interest_rate_percentage / 100

# Define time period based on the selected time unit and projection time
def define_time_period(time_unit, time_elapsed):
    if time_unit == "year":
        return time_elapsed
    elif time_unit == "quarter":
        return time_elapsed * 3
    elif time_unit == "month":
        return time_elapsed
    elif time_unit == "week":
        return time_elapsed / 4
    elif time_unit == "day":
        return time_elapsed / 30

# Define compounding period based on the selected compounding period unit
def define_compounding_period(compounding_period_unit):
    if compounding_period_unit == "year":
        return 1
    elif compounding_period_unit == "quarter":
        return 4
    elif compounding_period_unit == "month":
        return 12
    elif compounding_period_unit == "week":
        return 52
    elif compounding_period_unit == "day":
        return 365
    elif compounding_period_unit == "custom":
        return int(input("Enter custom compounding periods per year: "))

# Define projection period based on the selected projection time unit
def define_projection_period(projection_time, projection_time_unit):
    if projection_time_unit == "year":
        return projection_time
    elif projection_time_unit == "quarter":
        return projection_time * 4
    elif projection_time_unit == "month":
        return projection_time
    elif projection_time_unit == "week":
        return projection_time / 4
    elif projection_time_unit == "day":
        return projection_time / 30

# Calculate compound interest using the formula: A = P(1 + r/n)^(nt)
time_period = define_time_period(time_unit, projection_time)
compounding_period = define_compounding_period(compounding_period_unit)
projection_period = define_projection_period(projection_time, projection_time_unit)

total_amount = round(principal * (1 + interest_rate_decimal / compounding_period) ** (compounding_period * time_period), 2)

print("Total amount after compound interest:", total_amount)

# Summarize input data for Simple Interest Account
print("\nSI Account:")
print(f"  Principal (P): ${principal_si}")
print(f"  Interest Rate (r): {interest_rate_percentage_si}% per {time_unit_si}")

# Summarize input data for Compound Interest Account
print("\nCI Account:")
print(f"  Principal (P): ${principal}")
print(f"  Interest Rate (r): {interest_rate_percentage}% per {time_unit}")
print(f"  Compounding Frequency: {compounding_period_unit}")

# Summarize projection timeframe
print("\nProjection Timeframe:")
print(f"  {projection_time} {projection_time_unit}")
