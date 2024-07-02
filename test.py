def greet(name):
    print("Hello, " + name + "!")


def add(a, b):
    return a + b


class Person:
    def __init__(self, name, age):
        self.name = name
        self .age = age

    def say_hello(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old")


def main():
    john = Person("John", 30)
    john.say_hello()
    print(add(10, 5))
    greet("World")


if __name__ == "__main__":
    main()

