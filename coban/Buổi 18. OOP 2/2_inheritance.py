
class A:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Object with name: {self.name}'


class B(A):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def __repr__(self):
        parent_class_str = super().__repr__()
        return f'{parent_class_str}, age: {self.age}'


a = A('bang')
print(a)

b = B('hello', 22)
print(b)