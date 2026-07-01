#========<线上自动售货机>========
All_goods={"饮料":["可乐","雪碧","芬达","冰红茶","元气森林"],
           "零食":["辣条","薯片","果冻","面包","蛋糕"],
           "水果":["苹果","梨子","桃子","西瓜","香蕉"],
           "蔬菜":["白菜","番茄","黄瓜","胡萝卜","土豆"],
           "肉类":["鸡肉","牛肉","猪肉","羊肉","鱼肉"]}

kinds=list(All_goods.keys())

Prices={"可乐":3,"雪碧":3,"芬达":3,"冰红茶":3,"元气森林":5,"辣条":5,"薯片":7,"果冻":2,"面包":4,"蛋糕":10,"苹果":1,"梨子":1,"桃子":1,"西瓜":10,"香蕉":1,"白菜":3,
        "番茄":5,"黄瓜":6,"胡萝卜":7,"土豆":6,"鸡肉":10,"牛肉":40,"猪肉":18,"羊肉":35,"鱼肉":20}

card={"余额":500}                                                           
#>>>>>>>>>>>>===============================================================================================================================================
print("//////欢迎光临线上自动售货机//////")
print("="*60)
print(f"您当前购物卡余额为:{card['余额']}元")
print("="*60)

while True:
    print("\n>>>>>>输入你想购买的物品种类序号:")
    for index,K in enumerate(kinds):                                           
      print(f"{index+1}.{K}")                                               

    try:
       user_choice=int(input("\n>>>>>>请输入想要的商品种类序号(或者点击0退卡退出):"))                  
    except ValueError:
       print(">>>>>>输入格式错误，请重新输入！<<<<<<")
       continue

    if user_choice==0:
       print(f">>>>>>已为你取出购物卡！卡内剩余金额：{card['余额']}元,欢迎下次光临！")
       break

    if user_choice<1 or user_choice>len(kinds):                         
       print(">>>>>>序号超出范围，请重新输入！<<<<<<")
       continue

    selected_kinds=kinds[user_choice-1]                                
    selected_goods=All_goods[selected_kinds ]                           

    if len(selected_kinds)==0:
       print(f">>>>>>很遗憾,【{selected_kinds}】类的所有商品已经全部卖完了！请选择其他种类")
       continue
    
    print(f"\n>>>>>>您选择了:【{selected_kinds}】，以下是具体商品和价格:")                                

    for index,K in enumerate(selected_goods):                                        
       print(f"{index+1}.{K}----{Prices[K]}元")                                                               

    try:
       kinds_choice=int(input("\n>>>>>>请输入您想购买的商品序号:"))
      
    except ValueError:
       print(">>>>>>输入格式错误，请重新选择:")
       continue

    if kinds_choice<1 or kinds_choice>len(selected_goods):
       print(">>>>>>序号超出范围,请重新输入！<<<<<<")
       
    selected_product=selected_goods[kinds_choice-1]
    price=Prices[selected_product]

    if card['余额']<price:
       print(f">>>>>>余额不足！需要{Prices}<<<<<<")
       continue

    card['余额']-=price
    print(f"\n=====>>>>>>购买成功!您成功购买了：【{selected_product}】，花费{price}元<<<<<<=====")
    print(f"======当前卡内剩余金额：{card['余额']}元")

    All_goods[selected_kinds]=[
       K for K in All_goods[selected_kinds]
       if K!=selected_product
    ]
    
    print(f">>>>>>【{selected_product}】已经从货架上移除。")

    print("="*60)
    continue_buy=input(">>>>>>是否继续购买？(输入y继续,输入任意键退卡)")
    if continue_buy.lower()!='y':
       print(f"======已经为您取出购物卡！卡内剩余金额：{card['余额']}元，欢迎下次光临======")
       break
    