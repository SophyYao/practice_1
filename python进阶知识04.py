"""
列表 (list) 与 集合 (set) 的区别

1. 定义方式
   列表用方括号：my_list = [1, 2, 3]
   集合用花括号：my_set = {1, 2, 3}

2. 元素是否可重复
   列表可以重复：[1, 1, 2, 2] 没问题
   集合自动去重：{1, 1, 2} 会变成 {1, 2}

3. 是否有顺序
   列表有顺序，可以通过下标取元素：my_list[0] 拿到第一个
   集合没有顺序，不能用下标：my_set[0] 会报错

4. 查找速度
   列表查找慢，要一个个扫
   集合查找快，像查字典

5. 元素类型限制
   列表什么都能放：数字、字符串、列表、字典都可以
   集合里的元素必须是不可变的：可以放数字、字符串、元组，不能放列表、字典、另一个集合

6. 互相转换
   列表转集合：set(my_list)  会自动去重，但顺序不保证
   集合转列表：list(my_set)  顺序随机，要固定顺序用 sorted(my_set)

7. 什么时候用哪个
   需要顺序、允许重复、要按位置取元素 → 用列表
   需要去重、快速判断在不在、不关心顺序 → 用集合
"""
# s={1,3,5,7,9}
# print(s)

# l = [1,2,3,4,5,6,7,8,9,1,2,3]
# 转换成集合
# s1 = set(l) # 集合的里面的元素是没有重复的
# print(s1)

"""
集合 (set) 特点与语法
特点：
无序：没有下标，不能 my_set[0]
去重：{1, 1, 2} → {1, 2}
查找快：if x in my_set 很快
元素必须不可变：不能放列表、字典
语法：
创建：s = {1, 2, 3} 或 s = set()
增：s.add(4)
删：s.remove(4)  或 s.discard(4)  # discard 不存在不报错
查：if 4 in s:
长度：len(s)
转列表：list(s)
"""
# s = {1,2,3,4,5}
# s.add(6)
# print(s)

# s.remove(6)
# print(s)

# for index,item in enumerate(s):  #enumerate 不是转换类型，而是给可迭代对象加上序号。
#     print(index,item)

# s.clear()  #清楚集合的元素
# print(s)

# del s   #删除整个集合
# print(s)

"""
集合推导式：
{表达式 for 变量 in 可迭代对象 if 条件}
"""
# s1 = {i for i in range(10) if i % 2 == 0}
# print(s1)

# 字典推导式 key:value
# d1 = {i:i ** 2 for i in range(1,6)}
# print(d1)

"""
list() 变列表，set() 去重变集合
tuple() 变元组，dict() 要键值对
"""
# -------- 列表转字典 --------
# 要求：列表里的元素是 (key, value) 元组对
# a = [('name', '曾兵'), ('age', 25)]
# b = dict(a)
# print(b)          # → {'name': '曾兵', 'age': 25}
# print(b['name'])  # → 曾兵  （用key取值，比 a[0][1] 直观）

# -------- 元组转列表 --------
# a = (10, 20, 30)
# b = list(a)
# print(b)          # → [10, 20, 30]

# -------- 列表转集合 --------
# a = [1, 2, 3, 1, 2, 4, 6]
# b = set(a)
# print(b)          # → {1, 2, 3, 4, 6}  自动去重

# -------- 列表转元组 --------
# a = [1, 2, 3]
# b = tuple(a)
# print(b)          # → (1, 2, 3)

# 集合转列表
# s = {1, 2, 3}
# l = list(s)           # → [1, 2, 3]  顺序随机

# 字典转列表（只拿key）
# d = {'a': 1, 'b': 2}
# k = list(d)           # → ['a', 'b']
# v = list(d.values())  # → [1, 2]
# items = list(d.items())  # → [('a', 1), ('b', 2)]

# 字符串转列表
# s = "hello"
# l = list(s)           # → ['h', 'e', 'l', 'l', 'o']

# 字符串转集合（去重字符）
# s = "hello"
# st = set(s)           # → {'h', 'e', 'l', 'o'}

"""
函数
语法
def 函数名(函数的参数):
    函数体
    return 返回值
 def => 定义函数的关键字
 函数名 => 函数的名字,建议遵守函数的命名规则
 函数的参数 => 当我们调用这个函数的时候,传递的数据
 函数体 => 当函数被调用(执行),就会运行这个函数体
 return 返回值 => 当我们调用(执行)这个函数的时候,函数返回的结果
 函数的参数列表 => 我们在定义函数时，想要传递的数据
"""
# def login(username,password):
#     if username == 'admin' and password == '123456':
#         return "登录成功"
#     else:
#         return "登录失败"
# zhangsan = login("zhangsan","123456")
# print(zhangsan)
# admin = login("admin","123456")
# print(admin)


"""
调用函数的时候,函数名() => 这个()它的作用就是调用的意思

函数就是一个工具，定义一次，就可以调用多次 函数可以分装细节
"""
# def fn():
#     print("这是一个函数体")
#     return "123123"
# print(fn)   # 输出的其实函数地址(房间的门牌号)
# print(fn()) # 让函数 fn 这个函数运行起来
# print("*"*50)

# def fun1(a,b):      # 这里的a和b有一个专门的名字 => 形参
#     print("11111")
#     return "2222"
# aa = fun1(1,2)      # 这里面的1和2有一个专门的名字 -> 实参
# print(aa)

"""
解包就是将一组数据拆分,然后分给其他人
"""
# # 1. 最简单的解包
# x,y = 10,20
# y,x = x,y
# print(f"{x}~~~{y}")

# # 2. 字符串的解包
# a,b,c = "ABC"
# print(f"{a},{b},{c}")

# a,*b,c = [1,2,3,4,5,6,7,8,9]
# print(f"{a}~~~~{b}~~~~{c}")
# a,*b,c = "abcdefg"
# print(f"{a}~~~~{b}~~~~{c}")
# a,*_ = [1,2,3,"曾兵"]
# print(f"{a}~~~~{_}")

#位置传参解包
# def fun(a,b,c):
#     print(a,"-",b,"-",c)
# args = [1,2,3]
# fun(*args)  # *args 收集任意多个位置参数，打包成元组。

# 关键词传参解包
# def func(a,b,c):
#     print(a,b,c)
# keywords = {'a':1,'b':2,'c':3}
# func(**keywords)   #  ** 解包,用于字典

"""
lambda函数 => 他的本质就是一个匿名函数,所谓的匿名函数就是没有名字的函数
    如果说一个函数只有一个返回值,并且只有一句代码,那么就可以使用lambda函数进行简化操作
简化 => 
    1. 将def关键字省略不写,使用lambda进行替换
    2. 函数名也省略不写,使用变量名进行接收
    3. 函数的参数()也省略不写,包括返回值return也省略不写
"""
# 普通的函数
# def fn():
#     return "你好"
# res = fn()
# print(res)

# 使用lambda函数进行简化
# fn = lambda:"我好"
# res = fn()
# print(res)

# 位置传参
# def fn1(a,b):
#     return a + b
# res1 = fn1(1,2)
# print(res1)

# fn1 = lambda a,b : a + b
# res1 = fn1(1,2)
# print(res1)

# # 默认值传参
# fn2 = lambda a,b,c="小文": a+b+c
# res2 = fn2("问问","小小")
# print(res2)

# 带有 * 号的参数的lambda表达式
# fn3=lambda *args:args    # *args 收集任意多个位置参数，打包成元组。
# res3 = fn3(1,2,3,4,5,6)
# print(res3)

# fn4= lambda **kwargws:kwargws
# res4=fn4(name="张三",sge=18,gender="男")
# print(res4)

"""
了解 => python就是弱类型语言
    int a = 10
    float b = 20
a 的参数类型是 int 整数类型
b 的参数类型是 int 整数类型
返回的数据类型是一个 int 类型
"""
# def add(a:int,b:int):
#     return a+b
# res=add(['a','b','c'],['1','2'])
# print(res)

"""
一、什么是递归
    函数自己调用自己，把大问题拆成一模一样的小问题
二、两个必备条件（缺一不可）
    1. 终止条件（刹车）
       告诉递归什么时候停
       没有会无限循环，程序崩溃（RecursionError）
"""
# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)
# print(factorial(5))

"""
函数的嵌套
函数嵌套 = 大函数里包小函数，小函数能访问大函数的东西，外面看不到小函数。
"嵌套函数"通常指函数里面定义函数；函数里面调用函数叫"嵌套调用"，两者不一样。
函数嵌套定义也要先定义后调用，和正常函数规则一样，只是定义的位置在另一个函数里面。
"""

# 函数嵌套定义（函数里面定义函数）
# def outer():
#     print("外层函数开始")
#     def inner():  # 在 outer 里面定义 inner
#         print("内层函数执行")
#     inner()  # 在 outer 里面调用 inner
#     print("外层函数结束")
# outer()

#函数嵌套调用（函数里面调用别的函数）
# def wash_vegetables():
#     print("洗菜")
# def cut_vegetables():
#     print("切菜")
# def cook():
#     wash_vegetables()     # 调用洗菜
#     cut_vegetables()      # 调用切菜
#     print("炒菜完成")
# cook()

# global 关键字的作用就是将局部变量声明全局变量
# a = 66  # 全局变量
# def fun1():
#     print(f"fun1函数~~~{a}")
# def fun2():
#     global a # 告诉python,现在这个a就是一个全局变量的a
#     a = 200 # 改的全局变量
#     print(f"fun2函数~~~{a}")
# fun1()  # 66
# fun2()  # 200
# fun1()  # 200

# def fun2():
#     global c
#     c = 200              # 定义全局变量 c
#     print(f"fun2函数~~~{c}")
# def fun1():
#     print(f"fun1函数~~~{c}")   # 使用全局变量 c
# fun2()   # 先执行！创建 c = 200，打印 "fun2函数~~~200"
# fun1()   # 再执行！c 已经存在，打印 "fun1函数~~~200"

# 1. 排序回顾
l1 = [22,11,33,55,44]
l1.sort() # 升序
print(l1)
l1.sort(reverse=False) # 升序
print(l1)
l1.sort(reverse=True) # 降序
print(l1)


# 2. 字符串列表,元素排序
l2 = ["bc","abc","zyxl","h"]
# 对l2列表的元素进行排序
l2.sort()
print(l2)   # 默认:会按照字母的顺序进行排序
# 假如说:我们想要让他按照的字母的长度进行排序 -> len
# 添加一个属性 key = len 表是按长度进行排序
l2.sort(key=len)
print(l2)
l2.sort(key=len,reverse=True)
print(l2)


# 定义函数
# def get_data(t1):
#     return t1[1]        # 返回的t1这个序列数据下标为1的
#3. 对列表嵌套元组,内容进行排序
# l3 = [(1,3),(2,2),(5,1),(3,9)]
# l3.sort()
# print(l3)   # 按照第一个数字进行排序
# 我的目的是按照第二个数字排序,第二个数字的下标为1
# l3.sort(key=get_data)
# print(l3)
# l3.sort(key=get_data,reverse=True)
# print(l3)

# 1. 排序回顾
# l1 = [22,11,33,55,44]
# l1.sort() # 升序
# print(l1)
# l1.sort(reverse=False) # 升序
# print(l1)
# l1.sort(reverse=True) # 降序
# print(l1)
