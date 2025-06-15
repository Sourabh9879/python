class Calculator:
    @staticmethod
    def square(n):
        print(f"the square is { n * n}")
    def cube(self,n):
        print(f"the cube is { n * n * n}")

c = Calculator()
c.square(4)
c.cube(4)