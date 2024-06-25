from datetime import datetime, timedelta
from Work_load import WorkLoad
from constant import *

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

work_load = WorkLoad(year, holiday, "C026730")
start_date = datetime(year, 5, 22)
stop_date = datetime(year, 6, 25)
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

    work_load.read_work_load(JobDate)
    work_load.show_work_load_time_use(JobDate)
    work_load.show_work_load_table(JobDate)
    print()

    if False:  # key work load
        work_load.i_meeting(JobDate)
        work_load.i_coding_auto_inspection(JobDate)

        work_load.read_work_load(JobDate)
        work_load.show_work_load_time_use(JobDate)
        work_load.show_work_load_table(JobDate)
        print()

    date_focus += timedelta(days=1)
    n_day += 1
print(n_day, 'day')
