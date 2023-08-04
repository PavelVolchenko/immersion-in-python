# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
import sys


def check_date(date: list[str]) -> bool:
    MONTH = [31, (28, 29), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day, month, year = list(map(int, date))
    if 0 < year < 9999:
        if month == 2:
            return bool(0 < day <= (MONTH[month-1][1] if is_leapyear(year) else MONTH[month-1][0]))
        else:
            return 0 < day <= MONTH[month-1]


def is_leapyear(year: int) -> bool:
    return bool(not year % 4 and year % 100 or not year % 400)


# def check_date(date):
#     MONTH = [31, (28, 29), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     day, month, year = list(map(int, date.split('.')))
#     if 0 < year < 9999:
#         if month == 2:
#             if is_leapyear(year) and 0 < day <= (MONTH[month-1][1]):
#                 print('Date is OK')
#                 return True
#             elif 0 < day <= (MONTH[month-1][0]):
#                 print('Date is OK')
#                 return True
#             else:
#                 print('WRONG DATE!')
#                 return False
#         else:
#             if 0 < day <= (MONTH[month-1]):
#                 print('Date is OK')
#                 return True
#             else:
#                 print('WRONG DATE!')
#                 return False
#
#
# def is_leapyear(year):
#     if not year % 4 and year % 100 or not year % 400:
#         print('This is a leap year!', end=' ')
#         return True
#     return False


# check_date('29.2.2017')
# check_date('5.5.2000')
# check_date('31.4.2017')
# check_date('29.2.2016')

if __name__ == '__main__':
    date = sys.argv[-1].split('.')
    print(check_date(date))
