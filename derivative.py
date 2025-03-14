import matplotlib.pyplot as plt
import numpy as np
import math

class Derivative:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def draw(self):
        x = np.arange(-10, 10.01, 0.01)
        plt.plot(x, x*2 )  
        plt.legend() 
        plt.show()

derivative=Derivative(6, 6)
derivative.draw()