# -*- coding: utf-8 -*-
from CVdecter import *
import numpy as np
import cv2
import time
from matplotlib import pyplot as plt
if __name__=="__main__":
    img = cv2.imread('data/img/dec1.png', 0)
    ret, thresh = cv2.threshold(img, 127, 255, 0)
    print(img.s)