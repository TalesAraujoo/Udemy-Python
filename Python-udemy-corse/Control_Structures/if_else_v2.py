def grades(grade_value):
    
    if grade_value.isnumeric():
        grade = float(grade_value)
    else: 
        return('Invalid Grade!')
    

    if grade > 10:
        return('Invalid Grade!')
    elif grade >= 9.1:
        return('A')
    elif grade >= 8.1:
        return('A-')
    elif grade >= 7.1:
        return('B')
    elif grade >= 6.1:
        return('B-')
    elif grade >= 5.1:
        return('C')
    elif grade >= 4.1:
        return('C-')
    elif grade >= 3.1:
        return('D')
    elif grade >= 2.1:
        return('D-')
    elif grade >= 1.1:
        return('E')
    elif grade >= 0:
        return('E-')
    else:
        return('Invalid Grade!')
    

if __name__ == '__main__':

    input_grade = input('What was your grade: ')

    current_grade = grades(input_grade)

    if(current_grade == 'Invalid Grade!'):
        print('type a valid grade. 0 to 10')
    else: 
        print(f'The concept of your grade is {current_grade}')