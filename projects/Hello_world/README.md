# hello_world
学习一门新的编程语言都是从“hello word”开始!
Learning a new programming language always starts with "hello word"!

print("Hello python world!")

##Python print() 函数
- 语法 \
    print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
- 参数 \
    objects -- 复数，表示可以一次输出多个对象。输出多个对象时，需要用 , 分隔。
    sep -- 用来间隔多个对象，默认值是一个空格。
    end -- 用来设定以什么结尾。默认值是换行符 \n，我们可以换成其他字符串。
    file -- 要写入的文件对象。
    flush -- 输出是否被缓存通常决定于 file，但如果 flush 关键字参数为 True，流会被强制刷新。

##python的六个基本数据类型
- String（字符串）\
    字符串是 Python 中最常用的数据类型。我们可以使用引号( ' 或 " )来创建字符串。
    
- Number（数字）\
    Python 数字数据类型用于存储数值。
    数据类型是不允许改变的,这就意味着如果改变数字数据类型的值，将重新分配内存空间。
    - 整型(int) - 通常被称为是整型或整数，是正或负整数，不带小数点。Python3 整型是没有限制大小的，可以当作 Long 类型使用，所以 Python3 没有 Python2 的 Long 类型。布尔(bool)是整型的子类型
    - 浮点型(float) - 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 102 = 250）
    - 复数( (complex)) - 复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。
- List（列表）
    序列是 Python 中最基本的数据结构。
    序列中的每个值都有对应的位置值，称之为索引，第一个索引是 0，第二个索引是 1，依此类推。
    Python 有 6 个序列的内置类型，但最常见的是列表和元组。
- Tuple（元组）
    Python 的元组与列表类似，不同之处在于元组的元素不能修改。
- Set（集合）
    集合（set）是一个无序的不重复元素序列。
    可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
- Dictionary（字典）
    字典是另一种可变容器模型，且可存储任意类型对象。
    字典的每个键值 key=>value 对用冒号 : 分割，每个对之间用逗号(,)分割，整个字典包括在花括号 {} 中 ,格式如下所示：
    d = {key1 : value1, key2 : value2, key3 : value3 }

###基本类型中可变与不可变：
- 不可变数据（3 个）：\
    Number（数字）、String（字符串）、Tuple（元组）；
- 可变数据（3 个）：\
    List（列表）、Dictionary（字典）、Set（集合）。