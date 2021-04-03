import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
def readFile():
   data = pd.read_csv('president_heights.csv')
   print(data.head(5))
   height = np.array(data['height(cm)'])
   print("Mean of Heigth = ",height.mean())
   print("Standard Deviation = {}".format(height.std()))
   print("Minimun Height = {}".format(height.min()))
   print("Maximun Height = {}".format(height.max()))
   #print(height.describe())

   drawGraph(height)

def drawGraph(height):

   sns.set()
   plt.hist(height)
   plt.title("Height Distribution of Percentile of height")
   plt.xlabel("Height(cm)")
   plt.ylabel("Number")
   plt.show()

