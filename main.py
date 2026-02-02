import datetime


def calculate_day_order ():
    """Calculates the current day order based on working days from a start 
    date .... - consider mondays to fridays as working days .. day order from cycle 1 to 5  """
    # we can change this to  our semester's actual start date 
    semester_start_date = datetime.date(2026,1,26)
    day_order_cycle = 5

    today = datetime.date.today()

    if today <  semester_start_date:
        print("The semester has not yet updated")
        return 
    working_days_count = 0 
    current_date = semester_start_date

    #loop through each form the start date untill today 
    while current_date <= today:
        # weekday() return 0 for monday and 6 for sunday.
        # we only count days where the value is less than 5 ...( which will be monday , tuesday , wednesday , thursday , friday )
        if current_date.weekday() < 5 :
            working_days_count = working_days_count + 1 
        #move to the next day 
        current_date += datetime.timedelta(days = 1 )
    if working_days_count > 0 :
        """ will calculate the day order ... the logic count form (count - 1 ) % cycle  + 1 to ensure the result is between 1 and 5 
             like say  date 1 : ( 1 - 1 ) % 5 + 1 = 1 --> day 1 
             dor date 5  : ( 5 - 1 ) % 5 + 1 = 5 --> day 5 
            and for date 6 : ( 6 - 1 ) % 5 + 1 = 1 --> day 1
            """
        current_day_order = (working_days_count - 1 ) % day_order_cycle + 1 
        print(f" todays ' date : {today.strftime ('%A , %Y-%m-%d')}")
        print(f"semester start date : {semester_start_date.strftime('%Y-%m-%d')}")
        print(f"total working days passed : {working_days_count}")
        print("-"* 70)
        print(f"current day order : Day { current_day_order}")
        print("-"*70)
    else:
        print("no working days have passed since  the semester passed since the semester start date ")

calculate_day_order()
