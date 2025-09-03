# we dont have a switch in python, but we can create a 
# function to do the same thing using a dicionary

def get_weekday(day):
    days = {
        1: 'Sunday',
        2: 'Monday',
        3: 'Tuesday',
        4: 'Wednesday',
        5: 'Thursday',
        6: 'Friday',
        7: 'Saturday',
    }
    return days.get(day, 'Invalid Day')

if __name__ == '__main__':

    for dia in range(0,9):
        print(f'{dia}: {get_weekday(dia)}')