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

## SIMPLE INTEREST VS COMPOUND COMPARISON

print("Simple Interest Account")
principal_si = int(input("Enter the principal amount in $: "))
interest_rate_percentage_si = float(input("Enter the interest rate without the percentage sign: "))
time_unit_si = input("Enter the interest rate time unit (year, quarter, month, week, day): ")
time_elapsed_si = int(input("Enter the number of the previous time unit the interest will be calculated for: "))

# Calculate time period based on the selected time unit and time elapsed
if time_unit_si == "year":
    time_period_si = time_dictionary["years_dict"]["year"] * time_elapsed_si
elif time_unit_si == "quarter":
    time_period_si = time_dictionary["years_dict"]["quarter"] * time_elapsed_si
elif time_unit_si == "month":
    time_period_si = time_dictionary["years_dict"]["month"] * time_elapsed_si
elif time_unit_si == "week":
    time_period_si = time_dictionary["years_dict"]["week"] * time_elapsed_si
elif time_unit_si == "day":
    time_period_si = time_dictionary["years_dict"]["day"] * time_elapsed_si

interest_rate_decimal_si = interest_rate_percentage_si / 100  # converting the interest rate % to a decimal by dividing 100

# Calculate simple interest using the formula: A = P(1 + rt)
total_amount_si = round(principal_si * (1 + interest_rate_decimal_si * time_period_si), 2)  # rounding to 2 decimal places

# Summary for Simple Interest Account
summary_si = f"SI Account: P = {principal_si}, r = {interest_rate_percentage_si}% per year"

### COMPOUND INTEREST CALCULATION

print("\nCompound Interest Account")
principal_ci = int(input("Enter the principal amount in $: "))
interest_rate_percentage_ci = float(input("Enter the interest rate (enter 7% as 7): "))
time_unit_ci = input("Enter the interest rate time unit (year, quarter, month, week, day): ")
compounding_period_unit = input("Enter the compounding period time unit (year, quarter, month, week, day, custom): ")
projection_time_unit = input("Enter the projection time unit (year, quarter, month, week, day): ")
projection_time = int(input("Future projection timeframe for both accounts. Enter the amount of time to project into the future: "))

# Convert interest rate to a decimal
interest_rate_decimal_ci = interest_rate_percentage_ci / 100

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
time_period_ci = define_time_period(time_unit_ci, projection_time)
compounding_period = define_compounding_period(compounding_period_unit)
projection_period = define_projection_period(projection_time, projection_time_unit)

total_amount_ci = round(principal_ci * (1 + interest_rate_decimal_ci / compounding_period) ** (compounding_period * time_period_ci), 2)

# Summary for Compound Interest Account
summary_ci = f"CI Account: P = {principal_ci}, r = {interest_rate_percentage_ci}% per year, Compounding Frequency: {compounding_period}"

# Calculating projected amount and interest earned for Simple Interest Account
projected_amount_si = total_amount_si
interest_earned_si = projected_amount_si - principal_si

# Calculating projected amount and interest earned for Compound Interest Account
projected_amount_ci = total_amount_ci
interest_earned_ci = projected_amount_ci - principal_ci

# Output the summary lines
print("\nSummary:")
print(summary_si)
print(summary_ci)

# Output the projected amounts and interest earned
print("\nProjected Amounts and Interest Earned:")
print(f"SI Account projected amount: ${projected_amount_si}, Interest earned: ${interest_earned_si}")
print(f"CI Account projected amount: ${projected_amount_ci}, Interest earned: ${interest_earned_ci}")

print("MODULE 2: TIME FOR A CI ACCOUNT TO REACH A TARGET AMOUNT")

# Input parameters
principal = int(input("Enter the principal amount in $: "))
interest_rate_percentage = float(input("Enter the interest rate (enter 7% as 7): "))
time_unit = input("Enter the interest rate time unit (year, quarter, month, week, day): ")
compounding_period_unit = input("Enter the compounding period time unit (year, quarter, month, week, day, custom): ")
target_amount = float(input("Enter the target amount: "))

# Summarise input data
summary = f"CI Account: P = {principal}, r = {interest_rate_percentage}% per {time_unit}, Compounding Frequency: {compounding_period_unit}\nTarget amount: {target_amount}"
print(summary)

# Calculate compound interest and projection
interest_rate_decimal = interest_rate_percentage / 100

def define_time_period(time_unit, compounding_period_unit):
    if time_unit == "year":
        return time_dictionary["years_dict"][compounding_period_unit]
    elif time_unit == "quarter":
        return time_dictionary["years_dict"][compounding_period_unit] / 4
    elif time_unit == "month":
        return time_dictionary["years_dict"][compounding_period_unit] / 12
    elif time_unit == "week":
        return time_dictionary["years_dict"][compounding_period_unit] / 52
    elif time_unit == "day":
        return time_dictionary["years_dict"][compounding_period_unit] / 365

time_period = define_time_period(time_unit, compounding_period_unit)

projection = []
amount = principal
periods = 0
while amount < target_amount:
    amount *= (1 + interest_rate_decimal / time_period)
    projection.append(round(amount, 2))
    periods += 1

# Output projection and time taken
print("Forward projection:", projection)
if compounding_period_unit == "year":
    time_unit_plural = "years"
elif compounding_period_unit == "quarter":
    time_unit_plural = "quarters"
elif compounding_period_unit == "month":
    time_unit_plural = "months"
elif compounding_period_unit == "week":
    time_unit_plural = "weeks"
elif compounding_period_unit == "day":
    time_unit_plural = "days"
print(f"Time taken: {periods} {time_unit_plural}")

# PART 3, comparing 2 ci accounts
print("MODULE 3: COMPARING TWO CI ACCOUNTS")
def input_ci_account_params(account_number):
    print(f"Input parameters for Compound Interest Account {account_number}:")
    principal = int(input("Enter the principal amount in $: "))
    interest_rate_percentage = float(input("Enter the interest rate (enter 7% as 7): "))
    time_unit = input("Enter the interest rate time unit (year, quarter, month, week, day): ")
    compounding_period_unit = input(
        "Enter the compounding period time unit (year, quarter, month, week, day, custom): ")
    projection_time = int(input("Enter the projection time in years: "))

    return {
        "principal": principal,
        "interest_rate_percentage": interest_rate_percentage,
        "time_unit": time_unit,
        "compounding_period_unit": compounding_period_unit,
        "projection_time": projection_time
    }

# Prompt the user to input parameters for both Compound Interest Accounts
ci_account1_params = input_ci_account_params(1)
ci_account2_params = input_ci_account_params(2)

print("\nCompound Interest Account 1 parameters:", ci_account1_params)
print("Compound Interest Account 2 parameters:", ci_account2_params)

# function to calculate the compound interest of the second account
def calculate_compound_interest(principal, interest_rate_percentage, time_unit, compounding_period_unit, projection_time):
    def define_time_period(time_unit, compounding_period_unit):
        if time_unit == "year":
            return time_dictionary["years_dict"][compounding_period_unit]
        elif time_unit == "quarter":
            return time_dictionary["years_dict"][compounding_period_unit] / 4
        elif time_unit == "month":
            return time_dictionary["years_dict"][compounding_period_unit] / 12
        elif time_unit == "week":
            return time_dictionary["years_dict"][compounding_period_unit] / 52
        elif time_unit == "day":
            return time_dictionary["years_dict"][compounding_period_unit] / 365

    interest_rate_decimal = interest_rate_percentage / 100
    time_period = define_time_period(time_unit, compounding_period_unit)

    projection = []
    amount = principal
    periods = 0
    while periods < projection_time:
        amount *= (1 + interest_rate_decimal / time_period) ** (time_period)
        projection.append(round(amount, 2))
        periods += 1

    return projection
