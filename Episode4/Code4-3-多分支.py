# score = int(input("请输入分数:"))

# if score >= 90 :
#     print("A")
# else:
#     if score >= 80 :
#         print("B")
#     else:
#         if score >= 70 :
#             print("C")
#         else:
#             print("D")

# if score >= 90 :
#     print("A")
# elif score >= 80 :
#     print("B")
# elif score >= 70 :
#     print("C")
# else:
#     print("D")

# BMI计算
# BMI = w/(h*h)
w = float(input("请输入你的体重，单位KG:"))
h = float(input("请输入你的身高，单位米:"))
bmi = w / (h * h)
print(bmi)

if bmi < 18.5:
    print("过瘦")
elif bmi < 23.9:
    print("健康")
else:
    print("肥胖")
