import sys

def main(sc):
    while True:
        num = int(input("请输入指令(5退出)："))
        if num == 1:
            calc(sc)
        elif num == 2:
            display(sc)
        elif num == 3:
            search(sc)
        elif num == 4:
            rank(sc)
        elif num == 5:
            sys.exit(0)
        
def calc(sc):
    for student in sc:
        student[5] = sum(student[2:5])  # 总分
        student[6] = round(student[5] / 3, 1)  # 平均
    sc.sort(key=lambda x: x[5], reverse=True)  # 排名
    for i in range(len(sc)):
        sc[i][7] = i + 1
    print("已填入总分，平均和名次。")

def display(sc):
    print("成绩资料如下（按座位号排列）：")
    sc.sort(key=lambda x: x[0])
    for data in sc:
        print(data)

def search(sc):
    while True:
        name = input("请输入查询姓名（N退出）：")
        if name.upper() == "N":
            break
        for student in sc:
            if name == student[1]:
                print(student)
                break
        else:
            print("查无此人。")
        continue

def rank(sc):
    print("名次由低到高：")
    sc.sort(key=lambda x: x[7], reverse=True)
    for data in sc:
        print(data)



sc = [
    [1, "A", 80, 95, 88, 0, 0, 0],
    [2, "B", 98, 97, 96, 0, 0, 0],
    [3, "C", 91, 93, 95, 0, 0, 0],
    [4, "D", 92, 94, 90, 0, 0, 0],
    [5, "E", 92, 97, 80, 0, 0, 0]
]
main(sc)