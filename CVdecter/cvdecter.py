# -*- coding: utf-8 -*-
import numpy as np
import cv2
import time
from matplotlib import pyplot as plt
class raspdec:
    def dect(self):

        lower_red = np.array([0, 0, 0])
        upper_red = np.array([0, 255, 255])
        cap = cv2.VideoCapture(0)
        while 1:
            ret, frame = cap.read()
            mask = cv2.inRange(frame, lower_red, upper_red)
            res = cv2.bitwise_and(frame, frame, mask=mask)
            ret,binary = cv2.threshold(res, 127, 255, cv2.THRESH_BINARY)
            count=0
            upper=[]
            width=len(binary[0])
            hight=len(binary)
            for x in range(hight):
                for k in range(width):
                    if any(binary[x][k]):
                        count=1
                if count!=0:
                    upper=[x,k]
                    break
            squre=[]
            count=0
            for x in range(width):
                for k in range(hight):
                    if any(binary[k][x]):
                        count+=1
                if count!=0:
                    squre.append(count)
                count=0
            sum_left=0
            sum_right=0
            for x in range(int(len(squre)/2)):
                sum_left+=squre[x]
            for y in range(int(len(squre)/2)):
                sum_right+=squre[int(len(squre)/2)+y]
            if sum_left>sum_right:
                print("right")
                # return 1
            else:
                print("left")
                # return 0
            time.sleep(1)
if __name__=="__main__":
    a=raspdec()
    print(a.dect())

