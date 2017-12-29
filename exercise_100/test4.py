# 输入某年某月某日，判断这一天是这一年的第几天？

year = int(input("年："))
month = int(input("月："))
day = int(input("日："))
months1 = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]  # 闰年366
months2 = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]  # 平年365

if ((year % 4 == 0)and(year % 100 != 0)) or (year % 100 == 0)and(year % 400 == 0):
    date_num = months1[month-1] + day
else:
    date_num = months2[month-1] + day
print("是该年的第%d天" % date_num)