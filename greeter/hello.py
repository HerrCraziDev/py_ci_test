class Hello:
    def __init__(self, greet: str = "World"):
        self.name = greet

    def greet(self):
        return f"Hello {self.name}!"

    def set_name(self, name: str):
        self.name = name


if __name__ == "__main__":
    greeter = Hello()
    print(greeter.greet())
