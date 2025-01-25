import cv2
import numpy as np
import materialColor
import figureLineBaseTwoImgPts

def figureVanishingPt(imgPts, objRatioPts):
    ptsCnt, dim = imgPts.shape
    ratioCnt = len(objRatioPts)
    if ptsCnt != ratioCnt:
        print('count not match')
        return None
    if ptsCnt<3:
        print('count not enough')
        return None
    objPos = np.array(objRatioPts, dtype=np.float64).reshape(-1)
    b = np.tile([0., -1.], ptsCnt).reshape(-1, 1)
    vanishingPt = np.zeros([dim], dtype=np.float64)
    for d in range(dim):
        A = np.zeros([2*ptsCnt, 3+ptsCnt], dtype=np.float64)
        for i in range(ptsCnt):
            A[2*i, 0] = objPos[i]
            A[2*i, 1] = 1.
            A[2*i, 3+i] = -imgPts[i, d]
            A[2*i+1, 2] = objPos[i]
            A[2*i+1, 3+i] = -1.
        x = np.linalg.inv(A.T.dot(A)).dot(A.T).dot(b)
        vanishingPt[d] = x[0]/x[2]
    return vanishingPt


def figureVanishingLine(v1,v2):
    return figureLineBaseTwoImgPts.figureLineBaseTwoImgPts(v1, v2)




if  __name__=='__main__':
    src = cv2.imread("data/src.png")
    line1 = np.array([[424, 197], [508, 277], [563, 330]],dtype=np.float32)
    line2 = np.array([[1140, 924], [1144, 804], [
                     1153, 557]], dtype=np.float32)

    vanishingPt1 = figureVanishingPt(line1, [0, 1., 2.])
    vanishingPt2 = figureVanishingPt(line2, [0, 1., 3.])
    if vanishingPt1.any() == None or vanishingPt2.any() == None:
        print('error')
        exit(-1)
    figureVanishingLine(vanishingPt1, vanishingPt2)


    cv2.line(src, line1[0].astype(int), line1[1].astype(
        int), materialColor.CYAN_AMBIENT[::-1], 3)
    cv2.line(src, line1[1].astype(int), line1[2].astype(
        int), materialColor.GOLD_AMBIENT[::-1], 3)
    cv2.line(src, line2[0].astype(int), line2[1].astype(
        int), materialColor.Magenta[::-1], 3)
    cv2.line(src, line2[1].astype(int), line2[2].astype(
        int), materialColor.Yellow[::-1], 3)
    cv2.circle(src, vanishingPt1.astype(int), 5, materialColor.Magenta[::-1])
    cv2.circle(src, vanishingPt2.astype(int), 5, materialColor.Magenta[::-1])
    cv2.line(src, line1[2].astype(int), vanishingPt1.astype(
        int), materialColor.Blue[::-1], 1, cv2.LINE_8)
    cv2.line(src, line2[2].astype(int), vanishingPt2.astype(
        int), materialColor.Blue[::-1], 1, cv2.LINE_8)
    cv2.imshow("src", src)
    cv2.waitKey(0)
    cv2.destroyAllWindows()