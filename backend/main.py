import datetime

def get_day_order(start_date, cycle_length=5):
    """
    Calculates the day order based on business days (Mon-Fri).
    """
    today = datetime.date.today()
    
    if today < start_date:
        return None, "The semester hasn't started yet."

    # Calculate total days between dates
    delta_days = (today - start_date).days + 1
    
    # Efficiently count working days without a loop
    # This accounts for full weeks + remaining days
    working_days = sum(1 for i in range(delta_days) 
                      if (start_date + datetime.timedelta(days=i)).weekday() < 5)

    if working_days == 0:
        return None, "No working days have passed."

    # The math: (n-1) % cycle + 1 ensures a 1-based index (1 to 5)
    day_order = (working_days - 1) % cycle_length + 1
    return day_order, working_days

def display_day_order():
    # Configuration
    START_DATE = datetime.date(2026, 1, 26)
    today = datetime.date.today()
    
    day_order, result = get_day_order(START_DATE)

    print(f"{' SEMESTER STATUS ':=^40}")
    print(f"Today's Date:   {today.strftime('%A, %Y-%m-%d')}")
    print(f"Start Date:     {START_DATE.strftime('%Y-%m-%d')}")
    
    if isinstance(day_order, int):
        print(f"Working Days:   {result}")
        print("-" * 40)
        print(f"CURRENT ORDER:  DAY {day_order}")
    else:
        print(f"Notice:         {result}")
    print(f"{'':=^40}")

if __name__ == "__main__":
    display_day_order()