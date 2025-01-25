import cv2
import numpy as np
import materialColor
import figureVanishingPoint


def figureLineBaseTwoImgPts(x1, x2):
    X1 = np.array([x1[0], x1[1], 1], dtype=np.float64)
    X2 = np.array([x2[0], x2[1], 1], dtype=np.float64) 
    line = np.cross(X1, X2)
    return line/line[2]
