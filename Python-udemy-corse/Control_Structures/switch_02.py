def get_weekdays(day):
    days = {
        1: 'Sunday',
        2: 'Monday',
        3: 'Tuesday',
        4: 'Wednesday',
        5: 'Thursday',
        6: 'Friday',
        7: 'Saturday'
    }
    return days.get(day, 'Invalid Day')

def get_weekdays_weekend(day):
    weekday_weekend = {
        1: 'day of the weekend',
        2: 'day of the week',
        3: 'day of the week',
        4: 'day of the week',
        5: 'day of the week',
        6: 'day of the week',
        7: 'day of the weekend'
    }
    return weekday_weekend.get(day, 'Invalid')

if __name__ == '__main__':

    for day in range(0 , 8):
        print(f'{day}: {get_weekdays(day)}')
        print(f'{get_weekdays_weekend(day)}')