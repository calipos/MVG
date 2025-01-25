
import numpy as np

def crossPt(k1,p1,k2,p2):
    k1=k1.squeeze()
    p1=p1.squeeze()
    k2=k2.squeeze()
    p2 = p2.squeeze()
    A = np.array([k1[0], -k1[1], k2[0], -k2[1]]).reshape(2,2)
    b = np.array([k1[0]*p1[0]-k1[1]*p1[1], k2[0]
                 * p2[0] - k2[1]*p2[1]]).reshape(2, 1)
    return np.linalg.inv(A)@b

def crossRatio1(p1,p2,p3,p4):
    return np.linalg.norm(p1-p2)*np.linalg.norm(p3-p4)/np.linalg.norm(p1-p3)/np.linalg.norm(p2-p4)


def crossRatio2(p1, p2, p3, p4):
    return np.linalg.norm(p1-p2)*np.linalg.norm(p3-p4)/np.linalg.norm(p2-p3)/np.linalg.norm(p1-p4)


def crossRatio3(p1, p2, p3, p4):
    return np.linalg.norm(p1-p2)*np.linalg.norm(p2-p4)/np.linalg.norm(p1-p3)/np.linalg.norm(p3-p4)

k = np.random.rand(4, 2)
ancrho = np.random.rand(1, 2)
# k0(x-ancrho0) = k1(y-ancrho1)
k2 = np.random.rand(1, 2)
p2 = np.random.rand(1, 2)
k3 = np.random.rand(1, 2)
p3 = np.random.rand(1, 2)
k4 = np.random.rand(1, 2)
p4 = np.random.rand(1, 2)
c1 = crossPt(k[0], ancrho, k2, p2)
c2 = crossPt(k[1], ancrho, k2, p2)
c3 = crossPt(k[2], ancrho, k2, p2)
c4 = crossPt(k[3], ancrho, k2, p2)
d1 = crossPt(k[0], ancrho, k3, p3)
d2 = crossPt(k[1], ancrho, k3, p3)
d3 = crossPt(k[2], ancrho, k3, p3)
d4 = crossPt(k[3], ancrho, k3, p3)
e1 = crossPt(k[0], ancrho, k4, p4)
e2 = crossPt(k[1], ancrho, k4, p4)
e3 = crossPt(k[2], ancrho, k4, p4)
e4 = crossPt(k[3], ancrho, k4, p4)
print(crossRatio1(c1, c2, c3, c4))
print(crossRatio1(d1, d2, d3, d4))
print(crossRatio1(e1, e2, e3, e4))
print(crossRatio2(c1, c2, c3, c4))
print(crossRatio2(d1, d2, d3, d4))
print(crossRatio2(e1, e2, e3, e4))
print(crossRatio3(c1, c2, c3, c4))
print(crossRatio3(d1, d2, d3, d4))
print(crossRatio3(e1, e2, e3, e4))
print()