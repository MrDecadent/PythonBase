python_score = input("请输入你的python分数：")
c_score = input("请输入你的C语言分数：")

if python_score.isdigit() and c_score.isdigit():
    if int(python_score) >= 60 or int(c_score) >= 60:
        print("你的成绩合格")
    else:
        print("你的成绩不合格")
else:
    print("你输入的成绩格式有错，必须输入数字！")