class Student():
    def __init__(self,name,score:list):
        self.name = name 
        self.score: list = score
    def add_score(self,score):
        self.score.append(score)
    def average_score(self):
        if len(self.score) == 0:
            return 0
        return sum(self.score)/len(self.score)
    def max_score(self):
        if len(self.score)==0:
            return 0
        return max(self.score)
def test():
    student1 = Student('李四',[80,90,85])
    print(f'{student1.name}的平均分是{student1.average_score():.2f}')
    print(f'{student1.name}的最高分是{student1.max_score()}')
    student1.add_score(95)
    print(f'{student1.name}的平均分是{student1.average_score():.2f}')
    print(f'{student1.name}的最高分是{student1.max_score()}')
    print(f'{student1.name}的成绩是{student1.score}')
test()