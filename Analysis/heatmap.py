import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.image as mpimg 
import json
import seaborn as sns
import matplotlib.colors as cols
import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox


def alpha_cmap(cmap):
    my_cmap = cmap(np.arange(cmap.N))
    # Set a square root alpha.
    x = np.linspace(0, 1, cmap.N)
    my_cmap[:,-1] = x ** (0.5)
    my_cmap = cols.ListedColormap(my_cmap)

    return my_cmap

def FindPoint(x1, y1, x2,  
              y2, x, y) : 
    if (x > x1 and x < x2 and 
        y > y1 and y < y2) : 
        return True
    else : 
        return False


def get_image_data(df):
    #df = pd.read_csv("data/data.csv")
    df = df.values 
    freq_list = []
    sessions = {}
    for i in range(len(df)):
        X = df[i,1]
        X = json.loads(X) 
        Y = df[i,2]
        Y = json.loads(Y)   
        im = cv2.imread('data/images/image'+str(i)+'.png')

        dim = (1920, 1080)
        resized = cv2.resize(im, dim, interpolation = cv2.INTER_AREA)
        bbox, label, conf = cv.detect_common_objects(resized)
        freq = 0
        for j in range(len(label)):
            if label[j] != 'laptop' and label[j] != 'tv':
                x1, y1, x2, y2 = bbox[j]
                for k in range(len(X)):
                    if FindPoint(x1,y1,x2,y2,X[k],Y[k]):
                        freq += 1
        if len(X)!= 0:
            freq_list.append(freq/len(X))
        else:
            freq_list.append(0)
        output_image = draw_bbox(resized, bbox, label, conf)
        if len(X) > 2:
            try:
                hmax = sns.kdeplot(X, Y,color='r', shade=True, cmap=alpha_cmap(plt.cm.viridis), shade_lowest=False)
                #hmax.collections[0].set_alpha(0)
                xmin = min([x for x in X if x > 0])
                xmax = max([x for x in X if x < 1980])
                ymin = min([x for x in Y if x > 0])
                ymax = max([x for x in Y if x < 1080])
                print(xmin,xmax,ymin,ymax)
                if df[i,4] not in sessions:
                    sessions[df[i,4]] = [(abs((ymax-ymin)*(xmax-xmin)),(im.shape[0]*im.shape[1]))]
                else:
                    sessions[df[i,4]].append((abs((ymax-ymin)*(xmax-xmin)),(im.shape[0]*im.shape[1])))
            except:
                print("exception occured")

        plt.imshow(output_image, zorder=0)
        plt.savefig("heatmaps/map" + str(i) + ".png")
        plt.clf() 

    return freq_list,sessions