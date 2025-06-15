class Calculator:
    @staticmethod
    def square(n):
        print(f"the square is { n * n}")
    def cube(self,n):
        print(f"the cube is { n * n * n}")
    @staticmethod
    def greet():
        print("Hello there!")

c = Calculator()
c.greet()
c.square(4)
c.cube(4)