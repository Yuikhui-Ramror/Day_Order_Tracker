import datetime
import json


def load_holidays(file_path="holidays.json"):
    """
    Loads holidays from a JSON file and returns a set of date strings.
    """
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
        return set(data.get("holidays", []))
    except FileNotFoundError:
        print("Error: holidays.json file not found.")
        return set()


def get_day_order(start_date, holidays, cycle_length=5):
    """
    Calculates the day order by moving day-by-day from the semester start date,
    skipping weekends and holidays.
    """
    today = datetime.date.today()

    if today < start_date:
        return None, "The semester hasn't started yet."

    working_days = 0
    current_date = start_date

    while current_date <= today:
        is_weekday = current_date.weekday() < 5  # Monday–Friday
        is_holiday = current_date.isoformat() in holidays

        if is_weekday and not is_holiday:
            working_days += 1

        current_date += datetime.timedelta(days=1)

    if working_days == 0:
        return None, "No working days have passed."

    # Cycle day order (Day 1 → Day N → Day 1 ...)
    day_order = (working_days - 1) % cycle_length + 1
    return day_order, working_days


def display_day_order():
    # Configuration
    START_DATE = datetime.date(2026, 1, 26)
    CYCLE_LENGTH = 5

    today = datetime.date.today()
    holidays = load_holidays()

    day_order, result = get_day_order(
        START_DATE,
        holidays,
        CYCLE_LENGTH
    )

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
