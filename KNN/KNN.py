import cv2 as cv
import numpy as np
from collections import Counter
from sklearn.cluster import KMeans
import os
import pandas as pd
import matplotlib.pyplot as plt

idx = 0
R = 0
G = 0
B = 0
RGB = []
N = 1
cols = 3
rows = N

def show_img_compar(img_1, img_2 ):
    f, ax = plt.subplots(1, 2, figsize=(10,10))
    ax[0].imshow(img_1)
    ax[1].imshow(img_2)
    ax[0].axis('off') #hide the axis
    ax[1].axis('off')
    f.tight_layout()
    plt.show()
    
def input_csv(R, G, B, flist):
        data = {
                'R' : [R],
                'G' : [G],
                'B' : [B],
                '#RGB_Code' : [RGB_Code_Generator(R,G,B).upper()],
                'File Name' : [flist]
                }
        df = pd.DataFrame(data)

        if not os.path.exists('test_data.csv'):
            df.to_csv('test_data.csv', mode='w', encoding='utf-8-sig', index=False)
        else:
            df.to_csv('test_data.csv', mode='a', encoding='utf-8-sig', index=False, header=False)

def RGB_Code_Generator(R, G, B):
    R, G, B = int(R), int(G), int(B)
    return '#' + hex(R)[2:].zfill(2) + hex(G)[2:].zfill(2) + hex(B)[2:].zfill(2)

def palette_perc(k_cluster, flist):
    width = 300
    palette = np.zeros((50, width, 3), np.uint8)

    n_pixels = len(k_cluster.labels_)
    counter = Counter(k_cluster.labels_) # count how many pixels per cluster
    perc = {}
    for i in counter:
        perc[i] = np.round(counter[i]/n_pixels, 2)
    perc = dict(sorted(perc.items()))

    for i in range(0, N):
        R = int(k_cluster.cluster_centers_[i][0])      # R
        G = int(k_cluster.cluster_centers_[i][1])      # G
        B = int(k_cluster.cluster_centers_[i][2])      # B
        
        RGB_code = RGB_Code_Generator(R,G,B)
        print(RGB_code.upper())

        input_csv(R, G, B, flist)
        #for logging purposes
        #print(perc)
        print(k_cluster.cluster_centers_)

    step = 0

    for idx, centers in enumerate(k_cluster.cluster_centers_):
        palette[:, step:int(step + perc[idx]*width+1), :] = centers
        step += int(perc[idx]*width+1)

    return palette

def main():
    img = cv.imread("D:\\Coding\\Color\\img\\clustered\\two\\clustered_2.jpg")
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    img_2 = cv.imread("D:\\Coding\\Color\\img\\non-clustered\\two\\image2.jpg")
    img_2 = cv.cvtColor(img_2, cv.COLOR_BGR2RGB)
    
    print("==========   Clustered   ==========")
    clt_1 = KMeans(n_clusters=N)
    clt_1 = clt_1.fit(img.reshape(-1, 3))
    show_img_compar(img, palette_perc(clt_1), "D:\\Coding\\Color\\img\\clustered\\two\\clustered_2.jpg")

    print("==========   Non-Clustered   ==========")
    clt_2 = KMeans(n_clusters=N)
    clt_2 = clt_2.fit(img_2.reshape(-1, 3))
    show_img_compar(img_2, palette_perc(clt_2), "D:\\Coding\\Color\\img\\non-clustered\\two\\clustered_2.jpg")    
'''
    file_list = os.listdir('D:\\Coding\\Color\\img\\clustered\\two\\')
    path = "D:\\Coding\\Color\\img\\clustered\\two\\"
    for flist in file_list:
        full_path = path + flist
        print(full_path)
        img = cv.imread(full_path)
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

        clt_1 = KMeans(n_clusters=5)
        clt_1 = clt_1.fit(img.reshape(-1, 3))
        #palette_perc(clt_1, idx)
        palette_perc(clt_1, flist)
'''
if __name__ == '__main__':
        main()
