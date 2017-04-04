# -*- coding: utf-8 -*-
import numpy as np
import cv2
class raspdec:
    def sum_mat(self,mat):
        res = 0;
        for i in mat:
            for a in i:
                for x in a:
                    res += x
        return res
    def dect(self):
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        rgb = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        center_height = len(frame) / 2
        center_width = len(frame[0]) / 2
        lower_red = np.array([0, 0, 0])
        upper_red = np.array([0, 0, 255])
        mask = cv2.inRange(frame, lower_red, upper_red)
        res = cv2.bitwise_and(frame, frame, mask=mask)
        center_height = int(len(frame) / 2)
        center_width = int(len(frame[0]) / 2)
        frame_upper_left = res[:center_width, :center_height]
        frame_upper_right = res[center_width:, :center_height]
        frame_low_left = res[center_width:, :center_height]
        frame_low_right = res[center_width:, center_height:]
        left = self.sum_mat(frame_upper_left) + self.sum_mat(frame_low_left)
        right = self.sum_mat(frame_upper_right) + self.sum_mat(frame_low_right)
        if left > right:
            print("left")
            return 0
        else:
            print("right")
            return 1

