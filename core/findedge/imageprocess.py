import cv2
import numpy as np


def object_dectected(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blurred = cv2.GaussianBlur(gray, (11, 11), 0)

    canny = cv2.Canny(blurred, 10, 100)
    # cv2.imshow("Result:", canny)
    # cv2.waitKey()

    # canny_dilate = cv2.dilate(canny, None, iterations=1)
    # canny_erode = cv2.erode(canny_dilate, None, iterations=1)

    cnts, _ = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    print("I count {} screw in this image".format(len(cnts)))
    print(len(cnts))
    contours = image.copy()
    # cv2.drawContours(contours, cnts, -1, (0, 255, 0), 2)

    # loop over the contours individually
    centroid = image.copy()
    nuts = []
    screws = []
    for c in cnts:
        # Area
        # print(cv2.contourArea(c))
        # perimeter
        print(cv2.arcLength(c, True))
        M = cv2.moments(c)
        # centroid from moments
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
        cv2.circle(centroid, (cx, cy), 5, (0, 0, 255), -1)
        if cv2.arcLength(c, True) < 200:
            nuts.append((cx, cy))
        else:
            screws.append((cx, cy))
    cv2.imshow("result", centroid)
    cv2.waitKey(0)
    return nuts, screws


if __name__=='__main__':
    image = cv2.imread("all.png")
    nut, screw = object_dectected(image)
    print(nut)
    print("tet")
    print(screw)
