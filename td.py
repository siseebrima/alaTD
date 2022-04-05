def timeCalc():
    '''
        calculates the an employees' work stat at the end of the month.

        prints the status of the employee

    '''
    # prompt the user to provide the figures
    total_screenshots = int(input('Enter your total number of screenshots: '))
    low_activity = int(input('Enter the amount of low-activity screenshots: '))
    total_days = int(input('Total days worked: '))

    target = total_days * 8

    low = low_activity / 20
    work = total_screenshots / 20

    low_remainder = low_activity % 20
    work_remainder = total_screenshots % 20

    minutes = (work_remainder - low_remainder) * 3

    worked_time = work - low

    if minutes < 0:
        minutes += 60
        worked_time -= 1
    

    if worked_time >= target:
        print('Congratulations! You\'ve attained 100% work time this month.')
        print('your counted work time is ' + str(worked_time) + ' hours ' + str(minutes) + ' minutes')

    else:
        print('target for the month is ' + str(target))
        print('But your counted work time is ' + str(worked_time) + ' hours ' + str(minutes) + ' minutes')
        print('Your work time percentage is ' + str((worked_time / float(target)) * 100) + '%')
    

timeCalc()