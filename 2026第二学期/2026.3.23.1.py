class Student():
    def __init__(self,name,sid):
        self.name = name 
        self.id = sid
class Course():  
    def __init__(self, course_name, students=None):
        self.course_name = course_name
        self.students = students if students is not None else []
    def add_student(self,student):
        self.students.append(student)
    def show_students(self):
        print(f'{self.course_name}课程的学生有:')
        for student in self.students:
            print(f'姓名:{student.name} 学号:{student.id}')
def test():
    course = Course('数学',[])
    student1 = Student('李四','2021001')
    student2 = Student('王五','2021002')
    course.add_student(student1)
    course.add_student(student2)
    course.show_students()
    print(course.students)
test()