import matplotlib.pyplot as plt
import pandas as pd


class TestChar:
    df = None
    slices = []
    live=[]

    def __init__(self, url,colors):
        self.df = pd.read_csv(url)
        self.live = self.df.__getattr__(colors)
        self.kolory = self.df.__getattr__(colors)

        print(f'Leeen {len(self.df)}')
        for i in range(len(self.df)):
             self.slices.append(1)


    def createChart(self):
        plt.pie(self.slices,
                labels=self.live,
                colors=self.kolory
                )

        plt.title("Paleta")
        plt.show()

