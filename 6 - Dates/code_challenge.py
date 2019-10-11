from datetime import datetime, timedelta

# print today's date
today = datetime.now()
print('Today is ' + str(today) )

# print yesterday's date
one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday was ' + str(yesterday))

# ask a user to enter a date
# print the date one week from the date entered
user_date = input('Enter a date in mm/dd/yyyy format: ')
user_formatted_date = datetime.strptime(user_date, '%m/%d/%Y')
one_week = timedelta(weeks=1)
one_week_from_user_date = user_formatted_date + one_week
print('One week after ' + str(user_date) + ' is ' + str(one_week_from_user_date) )