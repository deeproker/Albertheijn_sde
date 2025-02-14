from datetime import date

def validate_date_range(start_date: date, end_date: date):
    if start_date > end_date:
        raise ValueError("Start date must be before end date.")