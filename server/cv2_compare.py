from skimage import measure
import matplotlib.pyplot as plt
import numpy as np
import cv2
from time import sleep
def compare_images(imageA, imageB):
        
    # compute the tructural similarity
    s = measure.compare_ssim(imageA, imageB,  multichannel=True)
    print("Similarity: %.2f" % s)
    print(s)
    return s


#path = '/home/parking_lot/test/'
#jpg = '.jpg'
#origImg = ['a1','b1','c1','d1','e1','f1','g1','h1','bb1']
#contImg = ['a2','b2','c2','d2','e2','f2','g2','h2','bb2']
def compare(origImg, contImg) : 
    sim_list = []
    for i in range(len(origImg)) :
        original = origImg[i]
        contrast = contImg[i]
        # convert the images to grayscale
        
        # original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY) if len(original.shape) == 3 else original
        # contrast = cv2.cvtColor(contrast, cv2.COLOR_BGR2GRAY) if len(contrast.shape) == 3 else contrast

        sim = compare_images(original, contrast)
        if(sim <= 0.7):
            sim_list.append(True)
        else:
            sim_list.append(False)
        # print(sim_list)
        sleep(0.5)

    return sim_list
        


