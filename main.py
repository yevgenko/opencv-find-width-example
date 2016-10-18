import numpy as np
import cv2

PHOTO_FILE = 'photo1.png'
# PHOTO_FILE = 'photo2.png'
KNOWN_DISTANCE = 23 - 3  # cm, where 3 is the length of brick from photo1 and 23 is distance from camera to surface
KNOWN_WIDTH_PX = 171  # cm
KNOWN_WIDTH_CM = 3  # cm
FOCAL_LENGTH = (KNOWN_WIDTH_PX * KNOWN_DISTANCE) / KNOWN_WIDTH_CM  # (rect[1][0] * KNOWN_DISTANCE) / KNOWN_WIDTH


def find_rect(image):
    # convert the image to grayscale, blur it, and detect edges
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(gray, 35, 125)

    # find the contours in the edged image and keep the largest one;
    # we'll assume that this is our piece of paper in the image
    # (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    img2, cnts, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    c = max(cnts, key=cv2.contourArea)

    # compute the bounding box of the of the paper region and return it
    return cv2.minAreaRect(c)


def width(knownDistance, focalLength, perWidth):
    # compute and return the distance from the maker to the camera
    return (knownDistance * perWidth) / focalLength

image = cv2.imread(PHOTO_FILE)
rect = find_rect(image)

print 'Pixels:'
print 'w: ', rect[1][0], 'h: ', rect[1][1]

print 'CMs:'
print 'w: ', width(KNOWN_DISTANCE, FOCAL_LENGTH, rect[1][0]), 'h: ', width(KNOWN_DISTANCE, FOCAL_LENGTH, rect[1][1])

# draw a bounding box around the image and display it
box = np.int0(cv2.boxPoints(rect))
cv2.drawContours(image, [box], -1, (0, 255, 0), 2)

cv2.imshow("image", image)
cv2.waitKey(0)
