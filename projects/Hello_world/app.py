import time

if __name__ == "__main__":
    #print函数讲解
    print("Hello python world!")
    a = "Hello "
    b = 1
    print(a,b)
    print("www","github","com",sep=".")
    print("---RUNOOB EXAMPLE ： Loading 效果---")
    print("Loading",end = "")
    for i in range(20):
        print(".",end = '',flush = True)
        time.sleep(0.5)
    #python的六个基本数据类型讲解