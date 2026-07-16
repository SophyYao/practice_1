"""
元组
 元组是一组不可以改变的列表
  元组用 （） 来表示
  创建元组
      t0 = tuple（“Hello World”）	# 相当于将字符串转换成元组
      t1 = （10,20,30）			# 创建了一个10,20,30元素的元组
      t2 = （10，）					# 创建一个元素的元组，一个元素需要在这个元素后面添加 ，
  元组也是一串序列数据，所以可以使用for循环来进行遍历
"""
# t0 = tuple("Hello World")
# print(t0)
# print(t0[1])
# t0[1] = "w"  #会报错 元组（tuple）是不可变的——创建后不能修改元素。

# t1 = (10,20,30)
# print(t1)

# t2 = (10,)
# print(t2)

"""
元组的下标，下标（索引）都是从0开始的
元组不能改变，不能被删除，只能获取
元组的推导式和列表的推导式用法一样
"""
# t1 = (x for x in range(1,10) if x % 2 == 0)  #生成器表达式，不是元组
# print(t1)
# print(tuple(t1))  # tuple转换成元组

"""
字典也是一种数据类型,但是字典里面存储的是 key_value 值的形式
一般别人会把数据转换JSON字符串,传递给我们,但是我们没有办法直接使用,所以我们一般将JSON字符串转换成一种数据结构,让我们利用python来进行操作,
这种数据结构就叫做字典
字典用 {} 来进行表示
	() -> 元组
	[] -> 列表
	{} -> 字典
字典的key_value形式
	{"key":value,"key2":value}
	注意: key是一个字符串双引号的形式，也就是关键词需要打引号，不同关键词之间，要打逗号。
"""
# infor = {
#     "username":"张三",
#     "age":18,
#     "gender":"男"
# }

"""
基础操作：增删改查
在获取字典里面的元素的时候,我们都是通过key来获取value
字典里面的元素的内容也是可以被改变的,也可以通过key来修改字典里面的value
删除字典里面的元素,也可以通过key来进行删除 => del 字典名[key]
删除整个字典 => del 字典名

"""
# info = {
#     "username":"张三",
#     "age":18,
#     "gender":"男"
# }

# print("info的姓名：",info["username"])  #获取字典里面的内容,通过key来获取value 语法 => info[变量名或者变量值]
# print("info的年龄：",info["age"])

# info["name"]="李四" #添加元组key_value
# info["sex"]="女"
# print(info)

# 修改元组
# info["name"]="王五"
# info["sex"]="妖"
# info["username"]="田七"
# aa="phone"
# info[aa] = "12345678899"
# print(info)

# 删除字典里面的元素
# del info["phone"]
# print(info)

# 删除整个字典
# del info
# print(info)

# 使用get方法
# my_dict = {"key1":"value1","key2":"value2"}
# print(my_dict.get("key1"))
# print(my_dict.get("key2"))

"""
字典转换成json字符串（json是纯文本字符串，用于网络传输、文件存储、跨语言交换）语法：
# 导入一个工具包
import json
# 字典转换成JSON数据 => json.dumps
data_json = json.dumps(data_dict)
# 注意:中文会出现ascii编码  JSON标准严格要求键和字符串值必须用双引号 "，单引号 `' 不行。
与字典的区别之一：Python 字典：单双引号随意
              JSON 文本：必须双引号（这是 JSON 规范定的，不是 Python 定的）
"""
# import json
# data_dict = {
#     "username":"张三",
#     "age":18,
#     "gender":"男"
# }
# data_json = json.dumps(data_dict,ensure_ascii=False)
# print(data_json)

"""
字典的遍历一般有三种方式
1. 直接遍历字典
2. 通过items来获取key 和value
.keys()	    所有键     dict_keys(['a', 'b'])
.values()	所有值     dict_values([1, 2])
.items()	所有键值对  dict_items([('a', 1), ...]) 
3. 通过enumerate来获取index,key,value

"""
# data_dict = {
#     "name":"张三",
#     "age":18
# }
# for key in data_dict:
#     print(key,data_dict[key])    # print(key,data_dict.get(key))
# print("-------------------")
# for key ,value in data_dict.items():
#     print(f"{key}~{value}")
# print("+++++++++++++++++++")
# for index,(key,value) in enumerate(data_dict.items(),start=2): # 下标从2开始
#     print(index,key,value)

"""
字典.keys() => 获取字典里面的所有的key
字典.values() => 获取字典里面的所有value
"""
# data_dict = {"name":"lili","age":18}
# keys = data_dict.keys()
# for key in keys:
#     print(key)
# print()
# values = data_dict.values()
# for value in values:
#     print(value)

"""
写入到json数据
	里面存储是json格式的文件
	将数据写入到json文件当中 => 步骤
		导包 => import json
		with open("json数据的文件名",'参数',encoding="utf-8") as f:
		json.dumps(字典,参数,ensure_ascii=False)
		解释
			with => 固定写法
			open => 打开JSON数据,打开JSON的文件
			参数 => 
				w => write => 写入文件
				r => read => 读取文件
				b => binary => 二进制
				wb / rb => 二进制写入/读取（图片、视频等）
			encoding="utf-8" => 全球通用编码格式
			as 取个小名
			ensure_ascii=False => 防止ascii的转换
			json.dumps() 对象 → 字符串	需要拿到字符串变量
			json.dump()	对象 → 写入文件	直接保存到文件时
			写入文件必须用 json.dump()（没有 s），并传入文件对象 f。

"""
import json
# data_dict = {
#     "username":"张三",
#     "age":18,
#     "gender":"男"
# }
# 写入文件
# with open("dict.json","w",encoding="utf-8") as f:
#     json.dump(data_dict,f,ensure_ascii=False)
# print("写入完毕")
#读取json数据
# with open ("dict.json","r",encoding="utf-8") as f:
#     test = json.load(f)
# print(test)