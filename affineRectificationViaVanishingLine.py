import cv2
import numpy as np
import materialColor
import figureLineBaseTwoImgPts
import figureVanishingPoint
 

def undistortProjectivityBaseVanishingLine(vanishingLine):
    A = np.eye(3, dtype=np.float64)
    A[2, :] = vanishingLine
    return A

if __name__ == '__main__':
    src = cv2.imread("data/src2.png")
    line1 = np.array([[108, 1451], [359,1313], [534,1217]], dtype=np.float32)
    line2 = np.array([[77, 1281], [359.5, 1312.5], [675, 1349], [1028, 1388], [
                     1426,1433],[1877.5,1484]], dtype=np.float32)

    vanishingPt1 = figureVanishingPoint.figureVanishingPt(line1, [0, 1., 2.])
    vanishingPt2 = figureVanishingPoint.figureVanishingPt(line2, [0, 1., 2.,3.,4,5])
    if vanishingPt1.any() == None or vanishingPt2.any() == None:
        print('error')
        exit(-1)
    vanishingLine = figureVanishingPoint.figureVanishingLine(
        vanishingPt1, vanishingPt2)
    H=undistortProjectivityBaseVanishingLine(vanishingLine)
    cv2.line(src, line1[0].astype(int), line1[1].astype(
        int), materialColor.Magenta[::-1], 3)
    cv2.line(src, line1[1].astype(int), line1[2].astype(
        int), materialColor.Yellow[::-1], 3)
    cv2.line(src, line2[0].astype(int), line2[1].astype(
        int), materialColor.Magenta[::-1], 3)
    cv2.line(src, line2[1].astype(int), line2[2].astype(
        int), materialColor.Yellow[::-1], 3)
    cv2.line(src, line2[2].astype(int), line2[3].astype(
        int), materialColor.Blue[::-1], 3)
    cv2.line(src, line2[3].astype(int), line2[4].astype(
        int), materialColor.Red[::-1], 3)
    cv2.line(src, line2[4].astype(int), line2[5].astype(
        int), materialColor.Cyan[::-1], 3)
    cv2.circle(src, vanishingPt1.astype(int), 5, materialColor.Magenta[::-1])
    cv2.circle(src, vanishingPt2.astype(int), 5, materialColor.Magenta[::-1])
    cv2.line(src, line1[2].astype(int), vanishingPt1.astype(
        int), materialColor.Blue[::-1], 1, cv2.LINE_8)
    cv2.line(src, line2[2].astype(int), vanishingPt2.astype(
        int), materialColor.Blue[::-1], 1, cv2.LINE_8)

    H[0, 2] = -920
    H[1, 2] = -1644
    dst = cv2.warpPerspective(src, H, src.shape[:2][::-1])
    cv2.imwrite('dst.jpg', dst)
    cv2.imwrite('src.jpg', src)
    # cv2.imshow("dst", dst)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
