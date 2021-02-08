'''
属性：类属性和实例属性
'''

# 类属性 就是类对象所拥有的属性
class Student:
    name = '李明'     # 属于类属性

    def __init__(self,age):
        self.age = age  # 实例属性
        pass
    pass


lm = Student(18)
print(lm.name, lm.age)
print('---------通过类对象 访问name ---------')
print(Student.name)
# print(Student.age)
'''
小结
类属性是可以 被类对象和实例属性共同访问使用的
实例对象只能有实例对象所访问
'''