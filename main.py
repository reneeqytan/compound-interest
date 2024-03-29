from tabulate import tabulate

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

def module_1():
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

    print("Compound Interest Account")
    principal_ci = int(input("Enter the principal amount in $: "))
    interest_rate_percentage_ci = float(input("Enter the interest rate (enter 7% as 7): "))
    time_unit_ci = input("Enter the interest rate time unit (year, quarter, month, week, day): ")
    compounding_period_unit = input("Enter the compounding period time unit (year, quarter, month, week, day, custom): ")
    projection_time_unit = input("Enter the projection time unit (year, quarter, month, week, day): ")
    projection_time = int(input("Future projection timeframe for both accounts. Enter the amount of time to project into the future: "))

    # convert interest rate to a decimal for easier calculations
    interest_rate_decimal_ci = interest_rate_percentage_ci / 100

    # Define time period based on the selected time unit and projection time, once again as derivatives of a year
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

    # define compounding period based on the selected compounding period unit as derivatives of a year
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

    # define projection period based on the selected projection time unit, defining it in years
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

    # calculate compound interest using the compound interests formula: A = P(1 + r/n)^(nt)
    time_period_ci = define_time_period(time_unit_ci, projection_time)
    compounding_period = define_compounding_period(compounding_period_unit)
    projection_period = define_projection_period(projection_time, projection_time_unit)

    total_amount_ci = round(principal_ci * (1 + interest_rate_decimal_ci / compounding_period) ** (compounding_period * time_period_ci), 2)

    # summary for CI Account for ease of use
    summary_ci = f"CI Account: P = {principal_ci}, r = {interest_rate_percentage_ci}% per year, Compounding Frequency: {compounding_period}"

    # calculating projected amount and interest earned for simple Interest account
    projected_amount_si = total_amount_si
    interest_earned_si = projected_amount_si - principal_si

    # calculating projected amount and interest earned for CI account
    projected_amount_ci = total_amount_ci
    interest_earned_ci = projected_amount_ci - principal_ci

    # output the summary lines
    print("\nSummary:")
    print(summary_si)
    print(summary_ci)

    # output the projected amounts and interest earned
    print("\nProjected Amounts and Interest Earned:")
    print(f"SI Account projected amount: ${projected_amount_si}, Interest earned: ${interest_earned_si}")
    print(f"CI Account projected amount: ${projected_amount_ci}, Interest earned: ${interest_earned_ci}")

def module_2():
    print("MODULE 2: TIME FOR A CI ACCOUNT TO REACH A TARGET AMOUNT")

    # input parameters of the interest calculation
    principal = int(input("Enter the principal amount in $: "))
    interest_rate_percentage = float(input("Enter the interest rate (enter 7% as 7): "))
    time_unit = input("Enter the interest rate time unit (year, quarter, month, week, day): ")
    compounding_period_unit = input("Enter the compounding period time unit (year, quarter, month, week, day, custom): ")
    target_amount = float(input("Enter the target amount: "))

    # summarise input data for easy comparison for user
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
    print("\nForward projection:", projection)
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

def module_3():
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

    ci_account1_projection = calculate_compound_interest(**ci_account1_params)
    ci_account2_projection = calculate_compound_interest(**ci_account2_params)

    # Output the projections
    print("\nProjection for Compound Interest Account 1:")
    print(ci_account1_projection)
    print("\nProjection for Compound Interest Account 2:")
    print(ci_account2_projection)

    # Display the comparison
    print("\nComparison of Compound Interest Account Projections:")
    for period in range(min(len(ci_account1_projection), len(ci_account2_projection))):
        print(f"Period {period+1}: Account 1 - ${ci_account1_projection[period]}, Account 2 - ${ci_account2_projection[period]}")

    # check which account reaches the target amount first, if specified. does this by iterating through in a loop until the target amount is reached by either one
    target_amount = float(input("Enter the target amount to compare (or enter 0 if not needed): "))
    if target_amount != 0:
        for period in range(min(len(ci_account1_projection), len(ci_account2_projection))):
            if ci_account1_projection[period] >= target_amount or ci_account2_projection[period] >= target_amount:
                print(f"\nAccount 1 reaches the target amount of ${target_amount} at period {period+1}")
                print(f"Account 2 reaches the target amount of ${target_amount} at period {period+1}")
                break

def module_4():# PART 4, MODELING REGULAR DEPOSITSS
    # mr kigodi aint no way u getting a car for 20,000... not in this economy.
    print("As a precursor to this, please fill out Module 1's info for Module 4's calculations. Thank you.")
    module_1() # necessary to fill out info
    # similar process here as before, function that asks for user input to define parameters in prep for calculations
    print("MODULE 4: MODELING REGULAR DEPOSITS")
    def input_regular_deposit_params():
        print("MODULE 4: Compound Interest account with regular deposits")
        principal = float(input("Enter the principal amount in $: "))
        interest_rate_percentage = float(input("Enter the interest rate (enter 7% as 7): "))
        time_unit = input("Enter the interest rate time unit (year, quarter, month, week, day): ")
        compounding_period_unit = input(
            "Enter the compounding period time unit (year, quarter, month, week, day, custom): ")
        regular_deposit_amount = float(input("Enter the regular deposit amount per compounding period: "))
        target_amount = float(input(
            "Enter the dollar amount to project to (if you enter 0, you will be asked for the amount of time to project for): "))
        # handles the decision to either use a target amount or a projection time
        if target_amount == 0:
            projection_time = int(input("In that case, enter the amount of time to project for: "))
            projection_time_unit = input("Enter the projection time unit (year, quarter, month, week, day, custom): ")
        else:
            projection_time = None
            projection_time_unit = None
        # returns the relevant parameters for the calculations
        return {
            "principal": principal,
            "interest_rate_percentage": interest_rate_percentage,
            "time_unit": time_unit,
            "compounding_period_unit": compounding_period_unit,
            "regular_deposit_amount": regular_deposit_amount,
            "target_amount": target_amount,
            "projection_time": projection_time,
            "projection_time_unit": projection_time_unit
        }


    # prompts user to input parameters for the compound interest account with regular deposits
    regular_deposit_params = input_regular_deposit_params()
    print("\nRegular Deposit Account parameters:", regular_deposit_params)


    # Calculate compound interest with regular deposits
    def calculate_compound_interest_with_regular_deposits(compounding_frequency, principal, interest_rate_percentage, time_unit,
                                                          compounding_period_unit,
                                                          regular_deposit_amount, projection_time, projection_time_unit,
                                                          target_amount):
        # converts interest rate to a decimal
        interest_rate_decimal = interest_rate_percentage / 100

        # defines compounding period based on the selected compounding period unit
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

        compounding_period = define_compounding_period(compounding_period_unit)
        regular_deposit_params["compounding_frequency"] = input(
            "Enter the compounding frequency (quarterly, monthly, weekly, daily, hourly, 10-minutely): ")

        # calculate compound interest with regular deposits
        def define_time_period(time_unit, compounding_period_unit): # converts time periods based on the derivative of a year
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

        # initialise lists to store projections
        opening_amounts = []
        interest_earneds = []
        regular_deposits = []
        closing_amounts = []

        # initialises opening amount with principal
        opening_amount = principal

        # Calculate compound interest and projections for each compounding period
        for period in range(projection_time):
            # Calculate interest earned for the current period
            interest_earned = opening_amount * (interest_rate_decimal / compounding_period)
            # Add regular deposit to the opening amount
            opening_amount += regular_deposit_amount
            # Calculate closing amount for the current period
            closing_amount = opening_amount + interest_earned
            # Store calculated values
            opening_amounts.append(round(opening_amount, 2))
            interest_earneds.append(round(interest_earned, 2))
            regular_deposits.append(regular_deposit_amount)
            closing_amounts.append(round(closing_amount, 2))
            # Update opening amount for the next period
            opening_amount = closing_amount

        return opening_amounts, interest_earneds, regular_deposits, closing_amounts


    # calls the function to calculate compound interest with regular deposits

    opening_amounts, interest_earneds, regular_deposits, closing_amounts = calculate_compound_interest_with_regular_deposits(**regular_deposit_params, compounding_frequency=None)
              # Add compounding_frequency here



    data = []
    # iterates over the length of opening amounts, constructs list containing the opening amount, interest earned etc. then appends to data list above
    for period in range(len(opening_amounts)):
        data.append(
            [opening_amounts[period], interest_earneds[period], regular_deposits[period], closing_amounts[period]])

    # display results using tabulate library, doesn't it look pretty uwu
    print("Projections:")
    print(tabulate(data, headers=["Opening Amount", "Interest Earned", "Regular Deposit", "Closing Amount"], tablefmt="fancy_grid"))

    def is_target_amount_reached(closing_amounts, target_amount):
        # check if any closing amount is greater than or equal to the target amount
        for closing_amount in closing_amounts:
            if closing_amount >= target_amount:
                return True
        return False

    target_amount = regular_deposit_params["target_amount"]

    # uses above logic (target amount reached function) to return result for whether the target was reached
    if is_target_amount_reached(closing_amounts, target_amount):
        print("Target amount is reached!")
    else:
        print("Target amount is not reached.")

    # checks if the target amount is reached
    target_amount = regular_deposit_params["target_amount"]
    if target_amount != 0:
        # determines if the target amount is reached with the current regular deposit amount
        if is_target_amount_reached(closing_amounts, target_amount):
            print("Target amount reached.")
        else:
            # adjusts the regular deposit amount iteratively until the target amount is reached
            min_regular_deposit = 0
            max_regular_deposit = target_amount  # sets so maximum regular deposit cannot exceed  target amount
            while True:
                # calculates the midpoint of the minimum and maximum regular deposit amounts
                regular_deposit_amount = (min_regular_deposit + max_regular_deposit) / 2
                # calculates compound interest with the updated regular deposit amount
                opening_amounts, interest_earneds, regular_deposits, closing_amounts = calculate_compound_interest_with_regular_deposits(
                    **regular_deposit_params, regular_deposit_amount=regular_deposit_amount)
                # checks if the target amount is reached with the updated regular deposit amount
                if is_target_amount_reached(closing_amounts, target_amount):
                    print("Target amount reached with regular deposit amount:", regular_deposit_amount)
                    break
                else:
                    # adjusts the range for the regular deposit amount based on whether the closing amount is greater or less than the target amount
                    if closing_amounts[-1] < target_amount:
                        # if closing amount is less than target amount, increase the minimum regular deposit amount
                        min_regular_deposit = regular_deposit_amount
                    else:
                        # if closing amount is greater than target amount, decrease the maximum regular deposit amount
                        max_regular_deposit = regular_deposit_amount

    # Prepare data for tabulation
    data = []
    for period in range(len(opening_amounts)):
        data.append([opening_amounts[period], interest_earneds[period], regular_deposits[period], closing_amounts[period]])

def module_5():
    print("Refer to presenter and presentation for explanation")

### PART 6

def print_menu(): # wraps each function in a ... function haha
    print("This program has five modules. Choose a module by typing its number")
    print("(1) Compare simple and compound interest savings accounts")
    print("(2) Calculate the time for a CI savings account to reach a target amount")
    print("(3) Compare two Compound Interest savings accounts")
    print("(4) Model a CI savings account with regular deposits")
    print("(5) Model increases in compounding frequency")
    print("(6) Quit")

def main(): # main is the menu, user has a loop to choose what they want to do
    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            module_1()
        elif choice == "2":
            module_2()
        elif choice == "3":
            module_3()
        elif choice == "4":
            module_4()
        elif choice == "5":
            module_5()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

main()