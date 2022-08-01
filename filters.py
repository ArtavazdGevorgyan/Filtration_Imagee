import cv2
import numpy as np


#########################
# Filter No.1  MONOCHROME
#########################
def blw(img: np.ndarray):
    b, g, r = cv2.split(img)
    gray = 0.30 * r + 0.59 * g + 0.11 * b
    return gray


#########################
# Filter No.2   RETRO
#########################
def retro(img: np.ndarray):
    b, g, r = cv2.split(img)
    rr = 0.393 * r + 0.769 * g + 0.189 * b
    rg = 0.349 * r + 0.686 * g + 0.168 * b
    rb = 0.272 * r + 0.534 * g + 0.131 * b
    rr[rr > 255] = 255
    rg[rg > 255] = 255
    rb[rb > 255] = 255
    return cv2.merge((rb, rg, rr))


#########################
# Filter No.3  CONTRAST
#########################
def contrast(img: np.ndarray, value: int = 30):
    final_img = img.copy()
    final_img[final_img < value] = 0
    final_img[(final_img >= value) & (final_img <= 128)] -= value
    final_img[final_img > 255 - value] = 255
    final_img[(final_img < 255 - value) & (final_img > 128)] += value

    return final_img


#########################
# Filter No.4  SATURATION
#########################
def saturation(img: np.ndarray, sat: int = 2):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    s *= sat
    s[s > 255] = 255
    return cv2.cvtColor(cv2.merge((h, s, v)), cv2.COLOR_HSV2BGR)


#########################
# Filter No.5  Gaussian blur
#########################
def blurr(img: np.ndarray):
    return cv2.GaussianBlur(img, (3, 3), 0)