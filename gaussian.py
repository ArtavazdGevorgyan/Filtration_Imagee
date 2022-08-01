import cv2
import numpy as np


#######################
#   WORKING CODE
#######################
def gauss_1(img: np.ndarray):
    ker = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16
    b, g, r = cv2.split(img)
    cols = img.shape[0] - 2
    rows = img.shape[1] - 2
    tb = np.empty((cols, rows), dtype="int32")
    tg = np.empty((cols, rows), dtype="int32")
    tr = np.empty((cols, rows), dtype="int32")

    for i in range(0, cols):
        for j in range(0, rows):
            tb[i, j] = (np.sum(b[i: i + 3, j: j + 3] * ker))
            tg[i, j] = (np.sum(g[i: i + 3, j: j + 3] * ker))
            tr[i, j] = (np.sum(r[i: i + 3, j: j + 3] * ker))

    return cv2.merge((tb, tg, tr))


#######################
#   NOT WORKING CODE
#######################
def gauss_2(img: np.ndarray):
    ker = np.array([[[1, 2, 1], [2, 4, 2], [1, 2, 1]],
                    [[1, 2, 1], [2, 4, 2], [1, 2, 1]],
                    [[1, 2, 1], [2, 4, 2], [1, 2, 1]]]) / 16
    cols = img.shape[0] - 2
    rows = img.shape[1] - 2
    finalimg = np.empty((cols, rows, 3), dtype="int32")
    for i in range(0, cols):
        for j in range(0, rows):
            tmp = img[i: i + 3, j: j + 3, :] * ker
            finalimg[i, j, :] = np.sum(tmp, axis=(1, 2))
    return finalimg
