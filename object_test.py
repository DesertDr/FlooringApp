# object_test

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"  

    @property
    def person_name(self) -> str:
        print(f'"{self.name}" called')
        return self.name

    @person_name.setter
    def person_name(self, value: str):
        print(f'"{self.name}" set to "{value}"')
        self.name = value

    @person_name.deleter
    def person_name(self):
        print(f'"{self.name}" deleted')
        del self.name

if __name__ == "__main__":
    # p1 = Person("John", 36)
    p1 = Person("John", 12)

    print(p1.name)
    print(p1.age)

    p1.person_name = "Jane"
    print(p1.name)

    del p1