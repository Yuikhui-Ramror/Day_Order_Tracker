import datetime


def is_working_day(d, holidays):
    # Sunday = always off
    if d.weekday() == 6:
        return False

    # Saturday rules
    if d.weekday() == 5:
        week_of_month = (d.day - 1) // 7 + 1
        if week_of_month not in (1, 3):
            return False

    # Custom holidays
    if d.strftime("%Y-%m-%d") in holidays:
        return False

    return True


def get_day_order(today, semester_start, cycle_length, holidays):
    """
    Returns:
        (day_order, is_working_day)
    """

    if today < semester_start:
        return None, False

    working_days = 0
    current = semester_start

    while current <= today:
        if is_working_day(current, holidays):
            working_days += 1
        current += datetime.timedelta(days=1)

    # If today itself is not working → no day order
    if not is_working_day(today, holidays):
        return None, False

    day_order = (working_days - 1) % cycle_length + 1
    return day_order, True