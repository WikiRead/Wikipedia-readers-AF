import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.image as mpimg 
import json
import seaborn as sns
import matplotlib.colors as cols

def alpha_cmap(cmap):
    my_cmap = cmap(np.arange(cmap.N))
    # Set a square root alpha.
    x = np.linspace(0, 1, cmap.N)
    my_cmap[:,-1] = x ** (0.5)
    my_cmap = cols.ListedColormap(my_cmap)

    return my_cmap


df = pd.read_csv("data/data.csv")
df = df.values 
for i in range(len(df)):
    X = df[i,1]
    X = json.loads(X) 
    Y = df[i,2]
    Y = json.loads(Y)   
    map_img = mpimg.imread("data/images/image" + str(i) + ".png") 
    if len(X) > 2:
        hmax = sns.kdeplot(X, Y,color='r', shade=True, cmap=alpha_cmap(plt.cm.viridis), shade_lowest=False)
        hmax.collections[0].set_alpha(0)
    plt.imshow(map_img, zorder=0)
    ##plt.show()
    plt.savefig("heatmaps/map" + str(i) + ".png")
    plt.clf() 
