import time
import matplotlib.pyplot as plt


class GraphActions:
    @staticmethod
    def create_graph_from_file(x, y, title, xTitle, yTitle):
        timestamp = int(time.time())
        plt.plot(x, y)
        plt.xlabel(xTitle)
        plt.ylabel(yTitle)
        plt.title(title)
        plt.savefig(f'..\Data_files\graph_{timestamp}.png')
