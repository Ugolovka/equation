import matplotlib.pyplot as plt
import numpy as np
import math

class Equation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

            
    def roots(self):
        discriminant = self.b ** 2 - 4 * self.a * self.c
        if discriminant > 0:
            x1 = (-self.b + math.sqrt(discriminant)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(discriminant)) / (2 * self.a)
            return (x1, x2)
        elif discriminant == 0:
            x1 = -self.b / (2 * self.a)
            return(x1)
        else:
            return None
        
    def draw(self):
        x = np.arange(-10, 10.01, 0.01)
        plt.plot(x, x**2)
        plt.title("Парабола")
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()


equation=Equation(25,36,9)
print(equation.roots())
equation.draw()