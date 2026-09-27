class Student():
    def __init__(self,name,score):
        self.name = name
        self.score = score 
def main():
    student = []
    for i in range(3):
        name = input('Name:')
        score = input('Score:')
        student.append(Student(name,score))
    with open('student.txt','w') as f:
        for stu in student:
            f.write(f'{stu.name} {stu.score}\n')
            
main()