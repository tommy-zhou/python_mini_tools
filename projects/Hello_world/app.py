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
    print("--- EXAMPLE ： Loading 效果---",file=file,flush = False)
    print("Loading",end = "",file=file,flush = False)
    for i in range(50):
        print(".",end = '',file=file,flush = False)
        time.sleep(0.5)
    file.close()

    #python的六个基本数据类型讲解
    #String（字符串）
    str = 'Hello world'

    print (str)          # 输出字符串
    print (str[0:-1])    # 输出第一个到倒数第二个的所有字符
    print (str[0])       # 输出字符串第一个字符
    print (str[2:5])     # 输出从第三个开始到第五个的字符
    print (str[2:])      # 输出从第三个开始的后的所有字符
    print (str * 2)      # 输出字符串两次，也可以写成 print (2 * str)
    print (str + "TEST") # 连接字符串

    #Number（数字）
    a, b, c, d = 20, 5.5, True, 4+3j
    print(type(a), type(b), type(c), type(d))

    #List（列表）
    list = [ 'abcd', 786 , 5.53, 'python', 90.8 ]
    tinylist = [123, 'python']

    print (list)            # 输出完整列表
    print (list[0])         # 输出列表第一个元素
    print (list[1:3])       # 从第二个开始输出到第三个元素
    print (list[2:])        # 输出从第三个元素开始的所有元素
    print (tinylist * 2)    # 输出两次列表
    print (list + tinylist) # 连接列表

    #Tuple（元组）
    tuple = ( 'abcd', 786 , 5.53, 'python', 90.8 )
    tinytuple = (123, 'python')

    print (tuple)             # 输出完整元组
    print (tuple[0])          # 输出元组的第一个元素
    print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
    print (tuple[2:])         # 输出从第三个元素开始的所有元素
    print (tinytuple * 2)     # 输出两次元组
    print (tuple + tinytuple) # 连接元组

    #Set（集合）
    sites = {'Google', 'Google', 'Python', 'Facebook', 'Zhihu', 'Baidu'}
    print(sites)   # 输出集合，重复的元素被自动去掉

    # 成员测试
    if 'Python' in sites :
        print('Python 在集合中')
    else :
        print('Python 不在集合中')

    # set可以进行集合运算
    a = set('abracadabra')
    b = set('alacazam')
    print(a)
    print(a - b)     # a 和 b 的差集
    print(a | b)     # a 和 b 的并集
    print(a & b)     # a 和 b 的交集
    print(a ^ b)     # a 和 b 中不同时存在的元素

    #Dictionary（字典）
    dict = {}
    dict['one'] = "1"
    dict[2]     = "2"
    print(dict['one'])       # 输出键为 'one' 的值
    print(dict[2])           # 输出键为 2 的值

    tinydict = {'name': 'Python','code':1, 'site': 'www.Python.com'}
    print(tinydict)           # 输出完整的字典
    print(tinydict.keys())    # 输出所有键
    print(tinydict.values())  # 输出所有值