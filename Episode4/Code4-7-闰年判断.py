year = int(input("请输入一个大于1582的年份："))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
if (not year % 4 and year % 100 ) or (not year % 400 ):
    print("%s是闰年" %year)
else:
    print("%s不是闰年" %year)