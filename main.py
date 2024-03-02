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

