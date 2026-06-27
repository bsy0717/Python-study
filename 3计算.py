import math
print(math.sin(1))
def f(x):
    return 2*x+1
result1=f(5)
print(result1)
def y(x):
    分式=(5*x)/(6*x+1-3/x)
    return (math.exp(x)
            +x**5
            +math.log2(16)
            -分式)
result2=y(10)
print(result2)
def 计算长方形的数据(长,宽):
    面积=长*宽
    周长=(长+宽)*2
    return 面积,周长
result面积,result周长=计算长方形的数据(5,7)
print("长方形的面积是：",result面积)
print("长方形的周长是：",result周长)
def 计算长方体的V(x,y,z):
    V=x*y*z
    return V
resultV=计算长方体的V(10,3,5)
print("长方体的体积是：",resultV)
    



