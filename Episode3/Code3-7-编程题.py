apple = 14
student = 4

print("每位同学可以分到%d个苹果" %(apple // student))
print("一共分出%d个苹果" %(apple // student * student))
print("把%d个苹果放回冰箱" %(apple - (apple // student * student)))