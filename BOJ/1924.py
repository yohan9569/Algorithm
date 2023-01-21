# 수학 / 브론즈 1 / 2007년


from datetime import date

days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
x, y = map(int, input().split())

print(days[date(2007, x, y).weekday()])
