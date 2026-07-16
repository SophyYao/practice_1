# while循环
"""
while训话的语法
index=1 #初始化
while bool类型:   #循环条件
    #编写循环体，当循环体条件为True的时候，那么就执行循环体内部的代码
    #迭代条件
    index += 1
"""
# index = 1
# while index <=3:
#     print(f"小明跑了第{index}圈")
#     index += 1
# print("循环结束")

"""
死循环就是循环的条件永远的True,那么就永远的执行循环体
while True:
    print("小明跑圈子")
"""

# sum = 0
# index = 1
# while index <= 50:
#     sum += index
#     index += 1
# print("循环结束，sum=",sum)

# sum = 0
# index = 5
# while index <= 50:
#     if index % 2 == 0:
#         sum += index
#     index += 1
# print("循环结束。sum=",sum)

"""
隐式类型转换:系统自动将数据类型转换为目标类型。
"""
# a = 5      # int
# b = 2.0    # float
#
# c = a + b  # Python 自动把 5 变成 5.0，再相加
# print(c)   # 7.0（float）

"""
流程控制语句之 pass
pass 是 Python 中的占位符语句，表示"什么都不做"。语法上需要一条语句，但逻辑上暂时不需要做任何事。
"""
# user=input("请输入你的账号名：")
# if user == "admin":
#     # TODO: 后续补充管理员逻辑
#     pass          # 先占位，避免语法错误
# else:
#     print("普通用户")

"""
流程控制语句之 break
break 用于立即终止整个循环，跳出循环体，继续执行循环后面的代码。
"""
# nums = [3, 7, 1, -5, 8, -2] # 在列表中查找第一个负数
# for n in nums:
#     if n < 0:
#         print(f"找到负数：{n}")
#         break          # 找到一个就停止，不会继续检查 -2
#
# print("循环结束")

# index = 1
# while index <= 5:
#     if index == 3:
#         break
#     print(f"小明跑了第{index}圈")
#     index += 1

"""
流程控制语句之 continue
continue 用于跳过当前循环的剩余代码，直接进入下一次迭代。
"""
# for i in range(1, 6):
#     if i % 2 == 0:
#         continue      # 遇到偶数，跳过本次循环的剩余部分
#     print(i)          # 只执行奇数的情况

"""
for 循环语法
for 临时变量 in (字符串,列表,range函数...是一个序列数据):
    # 代码
"""
# for item in "人工智能":
#     print(item)

"""
range函数也是一个序列数据,特点->包头不包尾
    range(n)    => 可以得到一个0~n之间的数字
    range(n,m)  => 可以得到一个n~m之间的数字
    range(n,m,step) => 可以得到一个n,m之间的数字,步子是step
我们一般可以使用for循环来结合range函数获取里面的每一项
"""
# res1 = range (10)
# for i in res1:
#     print(i)

# res2 = range(1,10)
# for i in res2:
#     print(i)

# res3 = range(10,20,3)
# for i in res3:
#     print(i)

"""
字符串切片
用于截取序列中某一段片段，特点->包头不包尾（左闭右开）
切片的语法 => 字符串的变量名 [start:end:step]
    start => 开始的下标
    end => 结束的下标
    step => 步子
    数字是负数时，一般从最后数，从1开始数
"""
# str1 = "Hello World"
# print(str1[2:5])  # 输出结果：llo  从下标为2开始截取,截取到下标为5结束,没有步长,默认步长为1
# print(str1[1:6:2])  # 输出结果：el   从下标为1开始截取,截取到下标为6结束,步长为2
# print(str1[:5])  # 输出结果：Hello    从下标为0开始截取,截取到下标为5结束
# print(str1[2:])  # 输出结果： llo World   从下标为2开始截取,到末尾结束
# print(str1[:])  #输出结果：Hello World   从开始头结束全部截取
# print(str1[::2])  #输出结果： HloWrd    从开头到结束全部截取,步长为2
# print(str1[:-2])  #输出结果：Hello Wor  从下标为0开始截取,到下标由后面往前面数,数2位
# print(str1[-4:-1])   #输出结果： orl      从下标由后面往前面数4位开始截取,到下标由后面往前面数-1结束
# print(str1[::-1])    # 输出结果：翻转字符串    从开始到结束,步长是从后面往前面数(翻转字符串)
# print(str1[::-2])    # 输出结果：drWolH     ,步长是从后面往前面数(数2位)

"""
字符串的属性和方法
    +               拼接字符串
    *               将字符串复制几遍
    upper           将字符串大写
    lower           将字符串小写
    index           找下标
    split           切割字符串,切割得到的结果是一个列表
    strip           去除字符串两边的空格
    count           统计字符串里面的字符
    len             统计字符串长度
    startswith     判断字符串是否以某某开头
"""
# str1 = "   Hello World   "
# #       01234567890123456     这个str1里面的位数
# print(str1 + "1")  # + 号的用法
# print(str1 * 5)  # * 号的用法
# print(str1.upper()) # upper => 将字符串大写
# print(str1.lower())  # lower => 将字符串小写
# print(str1.split('l'))  # split => 切割
# print(str1.index('l'))  # 找下标
# print(str1.count(' '))  # 统计字符串的字符
# print(len(str1))  # 统计字符串的长度
# print(str1.startswith('Hell'))  # 判断是否以某某开头
# print(str1.startswith('   H'))
# print(str1.startswith('   Hell'))

"""
 in和 not in 的用法
"""
# s = "hello"
# print("h" in s)     # True
# print("x" not in s) # True
# lst = [1, 2, 3]
# print(2 in lst)     # True

"""
列表用 [] 来进行表示
创建列表 => 
    1. 创建一个空的列表
        变量名 = []     # 里面没有任何的元素
    2. 创建一个有元素的列表
        变量名 = [1,2,3,4,5,6]  # 里面有数据
        这里面的数据可以是不同的数据类型

列表也是一串有序列的数据,下标(索引)也是从0开始的
有下标
    利用下标来获取元素  列表名[n]
    利用下标来修改元素  列表名[n] = xxx
    利用下标来删除元素  del 列表名[n]

列表的属性和方法
    +               拼接列表
    *               复制n列表
    in 和 not in    判断在列表当中是否存在
    count           统计列表某一个元素出现的次数
    index           从列表当中查找元素对应的下标
    append          往列表当中添加元素,添加在末尾
    insert(下标,元素) 将元素添加到列表当中指定的下标
    extend          往列表的末尾添加列表
    remove          删除列表当中的元素
    reverse         翻转列表
    clear           清除列表当中元素
    max,min,len     求列表当中的最大值,最小值,长度
    sorted()        对列表进行排序
        sorted(列表)                对列表进行从小到大的排序
        sorted(列表,reverse=True)   对列表进行从大到小的排序

列表的切片和字符串的切片的语法一样

列表推导式其实就是for循环的简化方式
语法 => 
    [ 返回数据 for item in 序列数据 if 数据加工]
    得到的结果是一个列表

"""
# str_list = ["张三","李四","王五","赵六",True,10]
# print(str_list)

# str_empty = []
# print(str_empty)

# num_list = [1,3,5,7,9]
# print(num_list[0])
# print(num_list[4])

# num_list[1] = "曾兵" #利用下标进行修改
# print(num_list)

# del num_list # 删除整个列表

# l1 = [1,2,3]
# l2 = [4,5,6]
# print(l1 + l2,l1,l2)

# l1 = [1,2,3]
# print(l1 * 3,l1)  #输出：[1, 2, 3, 1, 2, 3, 1, 2, 3] [1, 2, 3]

# print(31 in [1,2,3,3,4,5,6]) # False
# print(31 in [1,2,3,4,31,2])  # True
# print(33 not in [1,2,3,4,21]) # True

# l1 = [1,2,3,4,5,6,7,3]
# print(l1.count(3),l1)  # 输出：2 [1, 2, 3, 4, 5, 6, 7, 3]

# l1 = [1,3,5,7,9]
# print(l1.index(7),l1)  #3 [1, 3, 5, 7, 9]

# l1 = [1,2,3]
# l1.append("张三")
# print(l1)  # [1, 2, 3, '张三']

# l1 = [1, 2, 3]
# 1. insert(位置, 值) —— 在指定位置插入
# l1.insert(0, 6)         # 在索引 0 处插入 6
# print(l1)               # [6, 1, 2, 3]

# 2. extend —— 追加多个元素
# l1.extend([7, 8, 9, 6])
# print(l1)               # [6, 1, 2, 3, 7, 8, 9, 6]

# 3. remove —— 删除第一个匹配的值（注意是整数 6，不是字符串 "6"）
# l1.remove(6)            # 删除第一个 6
# print(l1)               # [1, 2, 3, 7, 8, 9, 6]

# 4. reverse —— 原地反转
# l1.reverse()
# print(l1)               # [6, 9, 8, 7, 3, 2, 1]

# 5. len —— 获取长度
# l2 = len(l1)
# print(l2, l1)           # 7 [6, 9, 8, 7, 3, 2, 1]

# 6. max / min
# n = max(l1)
# print(n)                # 9

# m = min(l1)
# print(m)                # 1

# 7. sorted —— 返回新列表，原列表不变
# res1 = sorted(l1)
# print(l1, res1)         # [6, 9, 8, 7, 3, 2, 1] [1, 2, 3, 6, 7, 8, 9]

# 8. sorted 降序
# res2 = sorted(res1, reverse=True)
# print(res2)             # [9, 8, 7, 6, 3, 2, 1]

# 9. clear —— 清空列表
# l1.clear()
# print(l1)               # []

# 将list1里面的整数丢到list2里面去
list1 = [1, 3, 5, 7, 9, 2, 4, 6, 8]
list2 = []
# 遍历这个list1,将里面的元素一个一个的取出来,判断是不是偶数,如果是偶数,丢到list2
for item in list1:
    if item % 2 == 0:
        # print(item)
        # 如果是偶数,那么就将这个数据丢大list2里面去
        list2.append(item)
print(list2)
print("-----------使用列表推导式来实现------------")
list1 = [1, 3, 5, 7, 9, 2, 4, 6, 8]
list2 = [item for item in list1 if item % 2 == 0]
print(list2)

