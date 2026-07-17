"""
1、字典是作为存储学生的容器，姓名作为键名，成绩作为值
例如：{"zhangshan":80,"lili":90,...}
2、搭建一个学生系统，然后根据学生选择不同的内容，来执行不同的操作
while True:
    #打印选项
    print("==========欢迎来到学生系统==========")
    print("1.添加学生")
    print("2.删除学生")
    print(".......")
    ......
    c=int(input("").strip()) # .strip()是去掉空格的
    if c == __ :
        然后判断学生是否在字典里面
            if 学生存在字典：
                添加失败，不允许添加相同姓名的学生
                ......

"""
data={}
while True:
    print("=====================欢迎来到学生管理系统====================")
    print("1.添加学生")
    print("2.删除学生")
    print("3.修改学生")
    print("4.查询学生")
    print("5.显示所以学生")
    print("6.退出系统")
    c = int(input("请输入对应的操作：").strip())
    if c == 1:
        print("====================添加学生信息====================")
        name = input("请输入学生姓名：")
        if name in data:
            print("添加失败，禁止重复添加")
        else:
            print("无该学生，请输入学生成绩")
            score = float(input(f"{name}的成绩："))
            try:
                if score>100 or score<0:
                    print("添加失败，输入的成绩不规范")
                else:
                    data[name]=score
                    print(f"添加成功！当前学生{name},成绩{score}")
            except:
                print("添加失败，输入的成绩有误！")
    elif c==2:
        print("====================删除学生信息====================")
        name = input("请输入学生姓名：")
        if name in data:
            del data[name]
        else:
            print("无法查询到该学生")
    elif c==3:
        print("====================修改学生信息====================")
        name=input("请输入学生姓名：")
        if name in data:
            print(f"输入{name}的成绩：")
            data[name]=score
        else:
            print("找不到该学生，请检查输入")
    elif c==4:
        print("====================查询学生信息====================")
        name=input("请输入学生姓名：")
        if name in data:
            print(f"{name}的成绩:{data[name]}")
        else:
            print("找不到该学生，请检查输入")
    elif c==5:
        print("====================显示所以学生信息====================")
        for stu,score in data.items():
            print(f"学生姓名：{stu} 学生成绩：{score}")
    elif c==6:
        print("====================表示退出系统====================")
        break
    else:
        print("输入信息错误")
print("程序结束")