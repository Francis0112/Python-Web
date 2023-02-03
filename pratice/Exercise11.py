

# day 6
# Datatime Exercise 


# print(time.ctime())

# now = time.localtime()
# print(now)
# print(now[1])
# x = time.strftime("%B %d, %Y %H:%M:%S", now)
# print(x)
# universal = time.gmtime()
# print(universal)

# # (year, month, day, hour, minutes, secs, day of the week, day of the year, dst)
# time_tuple = (2023, 2, 3, 2, 6, 0, 0, 0, 0)
# asc = time.asctime(time_tuple)
# print(asc)

# # all time in seconds since epoch
# mktime= time.mktime(time_tuple)
# print(mktime)

# from datetime import datetime, timezone

# now = datetime.now()
# print(now)
# year = now.year
# month = now.month
# day = now.day
# hour = now.hour
# minutes = now.minute
# seconds = now.second
# micro = now.microsecond

# print(f"{year}\n{month}\n{day}\n{hour}\n{minutes}\n{seconds}\n{micro}")
# # get UTC timezone
# now = datetime.now(timezone.utc)
# print(now)

# import time

# # get mili second
# t = time.time()
# mili = int(t * 1000)
# print(mili)


from datetime import datetime, timedelta
import time


def today():
    # Exercise 1: Print current date and time in Python
    return datetime.now().strftime("%A, %B %d, %Y")
# print(today())


def string_datetime():
    # Exercise 2: Convert string into a datetime object
    date_string = "Feb 25 2020 4:20PM"
    x = datetime.strptime(date_string, "%b %d %Y %I:%M%p")
    return x
# print(string_datetime())


def subtract_date():
    # Exercise 3: Subtract a week (7 days)  from a given date in Python
    given_date = datetime(2020, 2, 25)
    x = timedelta(days=7)
    res = given_date-x
    return res
# print(subtract_date())


def format_date():
    # Exercise 4: Print a date in a the following format
    # Day_name  Day_number  Month_name  Year
    now = datetime.now()
    return now.strftime("%A %d %B %Y")
# print(format_date())


def finding_day():
    # Exercise 5: Find the day of the week of a given date
    given_date = datetime(2020, 7, 26)
    return given_date.strftime("%A")
# print(finding_day())


def adding_date():
    #  Add a week (7 days) and 12 hours to a given date
    given_date = datetime(2020, 3, 22, 10, 0, 0)
    x = timedelta(days=7, hours=12)
    res = given_date+x
    return res
# print(adding_date())


def mili():
    # Exercise 7: Print current time in milliseconds
    n = time.time()
    t = int(n*1000)
    return t
# print(mili())


def date_string():
    # Exercise 8: Convert the following datetime into a string
    given_date = datetime(2020, 2, 25)
    str_date = given_date.strftime("%Y, %m %d")
    return str_date
# print(date_string())


def calc_date():
    # Exercise 9: Calculate the date 4 months from the current datea
    given_date = datetime(2020, 2+4, 25).date()
    return given_date
# print(calc_date())


def days():
    # Exercise 10: Calculate number of days between two given dates
    #given
    # 2020-02-25
    date_1 = datetime(2020, 2, 25)

    # 2020-09-17
    date_2 = datetime(2020, 9, 17)
    res = date_2 - date_1
    return res
# print(days())

