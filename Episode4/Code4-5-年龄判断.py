age = input("请输入你的年龄:")
if age.isdigit():
    if 0 <= int(age) <= 120:
        print("输入正确")
    else:
        print("输入错误，请重新输入")
else:
    print("请输入阿拉伯数字")
