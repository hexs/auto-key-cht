from datetime import datetime, timedelta
from Work_load_Input import i_meeting, i_coding_auto_inspection

BLACK = '\033[90m'
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
PINK = '\033[95m'
CYAN = '\033[96m'
ENDC = '\033[0m'
BOLD = '\033[1m'
ITALICIZED = '\033[3m'
UNDERLINE = '\033[4m'

year = 2024
holiday_note = {
    1: [1, 2, 3, 7, 13, 14, 20, 21, 27, 28],
    2: [3, 4, 10, 11, 17, 18, 24, 25],
    3: [2, 3, 10, 16, 17, 23, 24, 30, 31],
    4: [6, 7, 12, 13, 14, 15, 16, 17, 21, 27, 28],
    5: [1, 4, 5, 11, 12, 18, 19, 22, 26],
    6: [1, 2, 3, 9, 15, 16, 22, 23, 29, 30]

}
holiday = []
for month, days in holiday_note.items():
    for day in days:
        holiday.append(datetime(year, month, day))

for day in holiday:
    if day.weekday() == 6:
        print(RED, day.date(), day.strftime('%A'), ENDC)
    elif day.weekday() == 5:
        print(PINK, day.date(), day.strftime('%A'), ENDC)
    else:
        print(day.date(), day.strftime('%A'))

start_date = datetime(2024, 5, 1)
stop_date = datetime(2024, 5, 23)
date_focus = start_date
n_day = 0
while True:
    if date_focus >= stop_date:
        break
    month = date_focus.month
    day = date_focus.day
    if date_focus in holiday:
        date_focus += timedelta(days=1)
        continue

    JobDate = date_focus.strftime('%d-%b-%y')
    i_meeting(JobDate)
    i_coding_auto_inspection(JobDate)

    date_focus += timedelta(days=1)
    n_day += 1
print(n_day, 'day')
