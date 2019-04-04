from t2 import Human


class Student(Human):
    # 构造函数
    def __init__(self, school, name, age):
        self.school = school
        super(Student, self).__init__(name, age)
        super(Student, self).do_homework()

    # 实例方法
    def print_file(self, string):
        pass

    # 类方法
    @classmethod
    def plus_sum(cls):
        pass

    # 静态方法
    @staticmethod
    def add(x, y):
        pass


student = Student('清华大学', '鸡小萌', 16)
