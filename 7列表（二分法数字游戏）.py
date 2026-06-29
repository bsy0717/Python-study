import random
numbers=list(range(0,1000))
target=random.choice(numbers)

print("【=======【列表切割猜数字游戏】=======】")
print("初始范围在0--100")

while True:
    print(f"\n>>>>当前可猜的数字个数:{len(numbers)}个<<<<")

    if len(numbers)>10:
        print(f"===剩余列表片段:{numbers[:3]}...{numbers[-3:]}")
    else:
        print(f"===剩余列表片段：{numbers}")

    输入=input("===请输入数字：")

    try:
        guess=int(输入)
    except ValueError:
        print("===请输入数字！")
        continue

    if guess==target:
        print("恭喜你成功找到目标数字!\n[====<游戏结束！>====]")
        break

    elif guess<target:
        print(f"===正确数字比{guess}大,已切割掉0到{guess}这一段===")
        numbers=[x for x in numbers if x>guess]

    else:
        print(f"===正确数字比{guess}小,已切割掉1000到{guess}这一段===")
        numbers=[x for x in numbers if x<guess]

    if len(numbers)==0:
       print("=======啥子你把所有的可能数字都切掉了，游戏出错了啊======")
       break





