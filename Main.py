# -*- coding: utf-8 -*-
from CVdecter import *
import numpy as np
import cv2
import time
from matplotlib import pyplot as plt
if __name__=="__main__":
    cap = cv2.VideoCapture(0)
    decimg=cv2.imread("data/img/dec1.png")
    decimgGray=cv2.cvtColor(decimg,cv2.COLOR_BGR2GRAY)
    fast = cv2.ORB_create()
    while (True):
        ret, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        lower_red = np.array([150, 0, 150])
        upper_red = np.array([255, 250, 255])
        mask = cv2.inRange(hsv, lower_red, upper_red)
        res = cv2.bitwise_and(frame, frame, mask=mask)
        edges = cv2.Canny(gray, 100, 200)
        kp = fast.detect(gray, None)
        kp2= fast.detect(edges, None)
        #chess=cv2.findChessboardCorners(edges,20)
        #print(kp)
        img2 = cv2.drawKeypoints(frame, kp,outImage=None, color=(0, 255, 0))
        img3 = cv2.drawKeypoints(frame, kp2, outImage=None, color=(0, 0, 255))
        cv2.imshow('dect',img2)
        cv2.imshow('Window', res)
        cv2.imshow('Window2', img3)
        cv2.imshow('Window4', edges)
        #time.sleep(2)
        #plt.imshow(img2,"gray")
        #plt.show()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    print("Done")