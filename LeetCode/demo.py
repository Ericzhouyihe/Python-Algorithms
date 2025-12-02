class Student:
    school = '深兰教育'

    def __init__(self, name):
        self.name = name

    def study1(self, course):
        print(f'{self.name}在学习{course}课!')

    @classmethod
    def study2(cls, course):
        print(f'{cls.school}正在学习{course}课!')
        print(f'{Student.school}正在学习{course}课!')

    @staticmethod
    def study3(course):
        print(f'{Student.school}的学生在学习{course}课!')

    @property  # 只读属性装饰器
    def study4(self):
        return f'{self.name}在学习Python课'


stu1 = Student('张三')
stu2 = Student('李四')

stu1.study1('Python')
stu2.study1('机器学习')

Student.study1(stu1, "Python")
Student.study1(stu2, "机器学习")

Student.study2('Python')
stu1.study2('Python')
stu2.study2('Python')

Student.study3('Python')
stu1.study3('Python')
stu2.study3('Python')

print(stu1.study4)
print(stu2.study4)