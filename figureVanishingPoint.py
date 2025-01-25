import cv2
import numpy as np










if  __name__=='__main__':
    src=cv2.imread("data/src.png")
    cv2.imshow("src", src)
    line1=np.array([])
    cv2.waitKey(0)
    cv2.destroyAllWindows()