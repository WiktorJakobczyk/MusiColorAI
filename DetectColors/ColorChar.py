import matplotlib.pyplot as plt
import pandas as pd
from config import *

class ColorChar:
    df = None
    slices = []
    live=[]

    def __init__(self, url,colors):
        self.slices.clear()
        self.live.clear()

        self.df = pd.read_csv(url)
        self.live = self.df.__getattr__(colors)
        self.kolory = self.df.__getattr__(colors)

        print(f'Leeen {len(self.df)}')
        print(self.live)


        for i in range(len(self.df)):
             self.slices.append(1)


        print(self.slices)
    def createChart(self, ID):

        plt.pie(self.slices,
                labels=self.live,
                colors=self.kolory
                )

        plt.title("Paleta")
        #plt.show()
        plt.savefig(PATH_MUSIC+ID+'/plot.png')
        plt.close()

