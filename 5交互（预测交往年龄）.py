import random
name=input("请输入你的姓名：")
user_age=int(input("请输入你的年龄："))
gender=input("请输入你的性别（男/女）：")
def 获取随机数字():
    results=[]
    for _ in range(100):
     results.append(random.randint(1,20))
    results.sort()
    trimmed_results=results[1:-1]
    稳定随机年龄=round(sum(trimmed_results)/len(trimmed_results))
    return 稳定随机年龄
random_years=获取随机数字()
future_age=user_age+random_years
if gender=="男":
    称呼="先生"
elif gender=="女":
    称呼="小姐"
else:
    称呼="同志"
if gender=="男":
    对象="女朋友"
elif gender=="女":
    对象="男朋友"
else:
    对象="另一半"
if future_age>=30:
   print(f"很遗憾{name}{称呼}，你将在{future_age}岁找到你的{对象}")
else:
    print(f"恭喜你{name}{称呼}，你将在{future_age}岁找到你的{对象}")

