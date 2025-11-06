name = input("请输入你的名字：")
age = input("请输入你的年龄：")
# 类型转换
age = int(age)
year = 2025
birth = year - age
print("用户信息：姓名%s，年龄%s，出生年份：%d" % ( name, age, birth ))