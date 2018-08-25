class Animal():
    def __init__(self):
        pass


class Dog(Animal):
    def run(self):
        Cat.run(self)  # 鸭子模型
        print('dog is runing')

    def eat(self):
        print('eating met')


class Cat():
    zhuazi = 0

    def __init__(self):
        Cat.zhuazi += 1

    def run(self):
        print('cat say')


dog = Dog()

dog.run()
Cat.run(dog)  # 鸭子模型
print(isinstance(dog, Animal))

print(type(123))
print(type(123) == int)
print(type(dog) == Animal)
print(isinstance(dog, Animal))
print(dir(dog)[len(dir(dog))-1])

print(dir(dog).__len__())
print(hasattr(dog, 'run'))


# 使用lambad 空函数, 如果没有run2
getattr(dog, 'run2', lambda: None)()

cat = Cat()
cat2 = Cat()
cat.bb = lambda x: x*100


print(Cat.zhuazi)
print(Cat.zhuazi)


# 多重继承

class Robot():
    def run(slef):
        print('robot runing...')

    def code(self):
        print('coding python')


class RobotDog(Dog, Robot):
    pass

# 同时拥有两个类的方法
rd = RobotDog()

rd.run() # 使用先继承的对象的run
rd.eat()
rd.code()
