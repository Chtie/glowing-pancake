class Human():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self.name+'\n'+str(self.age))

    @staticmethod
    def do_homework():
        print('English homework')

