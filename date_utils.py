from datetime import datetime, timedelta

def current_datetime():
    """Return the current date and time as string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def days_between(date1_str, date2_str):
    """Return the number of days between two dates in YYYY-MM-DD format."""
    d1 = datetime.strptime(date1_str, "%Y-%m-%d")
    d2 = datetime.strptime(date2_str, "%Y-%m-%d")
    return abs((d2 - d1).days)

def add_days(date_str, days):
    """Add days to a date (format: YYYY-MM-DD)."""
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    new_date = date_obj + timedelta(days=days)
    return new_date.strftime("%Y-%m-%d")
