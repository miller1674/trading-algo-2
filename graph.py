

import matplotlib.pyplot as plt

import numpy as np

class Graph:
    def __init__(self):
        print("graph is ready")
    
    def draw_graph(self, y):
    
        x = np.linspace(0, 2, 100)
        p=range(1,len(y)+1)
        plt.plot(p, y)

        plt.xlabel('Weeks')
        plt.ylabel('Percent Gain')

        plt.title("Trading Algo")

        plt.legend()

        plt.show()