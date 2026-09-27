import os
print("当前目录：", os.getcwd())
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
def main():
        students = []
        try:
            with open('students.txt','r') as f :
                for line in f :
                    line = line.strip()
                    if line :
                        parts = line.split()
                        if len(parts)== 2 :
                            name = parts[0]
                            score = int(parts[1])
                            students.append(Student(name, score))
        except FileNotFoundError:
            print('找不到')
            return
        print('所有学生信息')
        for stu in students:
            print(f'Name：{stu.name},Score：：{stu.score}')
        if students:
            top_stu = max(students, key = lambda s : s.score)
            print(f'最高分学生：Name{top_stu.name},Score：{top_stu.score}')
        else:
            print('学生不存在')
main()