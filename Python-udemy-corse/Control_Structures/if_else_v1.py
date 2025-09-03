def grades(grade):
    if grade > 10:
        return('Invalid Grade!')
    elif grade >= 9.1 and grade <= 10:
        return('A')
    elif grade >= 8.1 and grade <= 9:
        return('A-')
    elif grade >= 7.1 and grade <= 8:
        return('B')
    elif grade >= 6.1 and grade <= 7:
        return('B-')
    elif grade >= 5.1 and grade <= 6:
        return('C')
    elif grade >= 4.1 and grade <= 5:
        return('C-')
    elif grade >= 3.1 and grade <= 4:
        return('D')
    elif grade >= 2.1 and grade <= 3:
        return('D-')
    elif grade >= 1.1 and grade <= 2:
        return('E')
    elif grade >= 0 and grade <= 1.0:
        return('E-')
    else:
        return('Invalid Grade!')
    

if __name__ == '__main__':

    input_grade = input('What was your grade: ')
    current_grade = grades(float(input_grade))

    if(current_grade == 'Invalid Grade!'):
        print('type a valid grade. 0 to 10')
    else: 
        print(f'The concept of your grade is {current_grade}')