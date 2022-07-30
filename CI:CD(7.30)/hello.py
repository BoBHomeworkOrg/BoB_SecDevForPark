class Hello:
    def say(hello):
        print("hello world")

    def add(self, x, y):
        print("x+y = ", (x+y))
        return (x+y)


if __name__ == "__main__":
    h = Hello()
    h.say()
    h.add(2, 3)
