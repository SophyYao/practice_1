# 猜数字小游戏
# import random
#
# secret = random.randint(1, 10)
# guess = int(input("猜一个 1-10 的数字："))
#
# if guess == secret:
#     print("🎉 猜对了！")
# elif guess < secret:
#     print("小了，答案是", secret)
# else:
#     print("大了，答案是", secret)


# 九九乘法口诀表
# \t 是制表符（Tab），作用是让输出内容对齐，类似键盘上的 Tab 键。
# for j in range(1,10):
#     for i in range(1,j+1):
#         print(f"{j}*{i}={j*i}",end="\t")
#     print()


# 输入一个字符串,输出所有偶数的索引位置的字符串
# s = input("请输入一个字符串：")
# print(s[::2])

# 编写一个程序,查找输入的字符串当中是否包含"python"字符串
# s=input("请输入一个字符串:")
# if "python" in s:
#     print("有python")
# else:
#     print("没用python")

# s="abcdab"
# # print("------------计算字符串的长度------------")
# # print(len(s))
# # print("------------翻转字符串------------")
# # m=s[::-1]
# # print(m)
# # n=list(s)
# # n.reverse()  #这个也是翻转  .reverse() 是列表专属方法
# # str1=""     # 再将列表转换成字符串
# # for i in n:
# #     str1 += i
# # print(str1)
# # print("------------统计各个字符串出现的次数------------")
# # diff=""
# # for char in s:
# #     print(char)
# #     is_new=True
# #     for exist in diff:
# #         if exist == char:
# #             is_new = False
# #             break
# #     if is_new == True:
# #         diff += char
# # print(diff)

#编写一个程序,定义一个列表,将列表里面所有的元素去重
# s="abcdab"
# char_count = {}
# for char in s:
#     if char in char_count:
#         char_count[char] += 1
#     else:
#         char_count[char] = 1
# print(char_count)

# set 会自动去重，但会打乱原有顺序
# my_list = [1, 2, 2, 3, 4, 4, 4, 5, 1]
# unique_list = list(set(my_list))
# print(unique_list)

# 利用字典的key来去重
# s1 = [1,2,3,4,5,6,7]
# s2 = [3,4,5,6,7,8,9]
# ss = s1 + s2
# print(ss)
# dict = {}
# for s in ss:
#     dict[s] = "无所谓"
# print(list(dict))

