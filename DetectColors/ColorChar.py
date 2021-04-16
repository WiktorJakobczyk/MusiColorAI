import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import rcParams

from config import *

class ColorChar:
    df = None
    slices = []
    live = []

    def __init__(self, url, colors):
        self.slices.clear()
        self.live.clear()

        self.df = pd.read_csv(url,usecols=colors)
        self.live = self.df[colors[0]]
        self.kolory = self.df[colors[0]]
        print(colors[1])
        self.slices = self.df[colors[1]]
        # for i in range(len(self.df)):
        #     self.slices.append(1)
        # print(len(self.slices2[1]))
        # print(len(self.slices))


    def createChart(self, ID):
        plt.pie(self.slices,
                colors=self.kolory,
                radius=1.5
                )

        plt.savefig(PATH_MUSIC+ID+'/plot.png', transparent=True, bbox_inches=rcParams["savefig.bbox"])
        plt.close()

