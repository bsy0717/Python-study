import random

def 抽卡(本次抽数=10):
    All_times=0
    This_times=0
    Get_place=[]

    print(f"抽卡开始，目标抽取次数{本次抽数}次")
    print(f"规则:1-60(1%),61-79(递增)80(50%),160(100%)")

    for i in range(1,本次抽数+1):
        All_times+=1
        This_times+=1

        p=0.01
        if This_times<=60:
            P=p
        elif 60<This_times<80:
            Plus_number=(0.50-0.01)/(80-60)
            P=p+(This_times-60)*Plus_number
        elif This_times==80:
            P=0.50

        if All_times%160==0:
            P=1.0

        是否出金=random.random()<P
        if 是否出金:
           Get_place.append(All_times)
           This_times=0

    print(f"出金位置：{Get_place}")
    return Get_place

print("是否花费1600原石进行十连抽？")
输入=input("请输入确认开始抽卡：")
if 输入=="确认":
   抽卡(100)
else:
    print("已取消抽卡")