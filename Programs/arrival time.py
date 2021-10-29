Hotp = int(input())
Motp = int(input())
Hp = int(input())
Mp = int(input())

day = 24

days = 0
Hours = Hotp + Hp
Minutes = Motp + Mp
days = Hp // day
HoursI = 0
if Hours > 24:
    HoursI = (Hours % 24)
else:
    HoursI = Hours
if Minutes >= 60:
    Minutes = Minutes % 60
    HoursI += 1

if len(str(HoursI)) == 1 and len(str(Minutes)) == 1: # Если числа однозначные, добавляем незначащий ноль
    print("0" + str(HoursI), "hours", ":", "0" + str(Minutes), "minutes")
    print(days, "days")
else:
    print(HoursI, "hours", ":", Minutes, "minutes")
    print(days, "days")
