import time

if __name__ == "__main__":
    #print函数讲解
    print("Hello python world!")

    a = "Hello "
    b = 1
    print(a,b)

    print("www","github","com",sep=".")

    print("--- EXAMPLE ： Loading 效果---")
    print("Loading",end = "",flush = False)
    for i in range(20):
        print(".",end = '',flush = False)
        time.sleep(0.5)

    file = open("hello_world.txt","w")
    print("--- EXAMPLE ： Loading 效果---")
    print("Loading",end = "",file=file,flush = False)
    for i in range(50):
        print(".",end = '',file=file,flush = False)
        time.sleep(0.5)
    file.close()

    #python的六个基本数据类型讲解