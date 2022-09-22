# from dataclasses import dataclass
# @dataclass
# class person:
#     name: str
#     age: int
#
#     p1 = ("Adeola", 17)
#     print(p1)

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return self.name and self.age
p1 = person("Adeola", 16)
print(p1)