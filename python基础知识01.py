#数据类型
"""
f=30.5
ff=str(f)
print(ff)
a=10
=float(a)
print(f)
还有int()、bool()、tuple这些数据类型
元组（tuple） 类型
"""

#条件语句
"""
a=10
b=20
if a <b:
    print("真的")
if a > b:
    print("假的")
"""

#输入函数
"""
print("开始")
name=input("请输入您的姓名")
age=input("请输入您的年龄")
print(name,age)
print(type(name),type(age))
print("结束")
"""

"""
#eval可以将字符串当成表达式进行执行,eval() 只接受字符串、字节或代码对象。
print("1+1")
print(eval("1+1"))
print(type(eval("10,3")))
"""

'''
#多重if语句
a=int(input("请输入你的语文成绩："))
if a >= 90:
    print("优秀")
elif a >= 70:
    print("良好")
elif a >= 60:
    print("及格")
else:
    print("不及格")
'''

"""
字符串有哪些分类?
    1. 普通字符串 => "张三",单引号或者双引号
    2. 纯数字字符串 => "12334567"
    3. 模板字符串 => 我们可以使用三引号(三个单引号或者三个多引号)
    4. JSON字符串 => 轻量级的数据交互单位
    5. 查询字符串 => 键值对的方式
"""

"""
str1 =     "Hello World"
# 下标(索引)  01234567890
# 可以根据字符串的下标来获取字符串里面的字符
# print(str1[0])
# print(str1[1])
# print(str1[2])
# print(str1[3])
# print(str1[4])
# print(str1[5])
# print(str1[6])
# print(str1[7])
# print(str1[8])
# print(str1[9])
# print(str1[10])
#  上面是一串有规律的重复的代码
for item in str1:
    print(item)
"""

