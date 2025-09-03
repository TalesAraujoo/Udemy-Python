def get_weekday(day):
    match day:
        case 2 | 3 | 4 | 5 | 6:
            return 'day of the week'
        case 1 | 7:
            return 'day of the weekend'
        case _:
            return 'Invalid day'
        
if __name__ == '__main__':
    for day in range(0, 8):
        print(f'{day}: {get_weekday(day)}')