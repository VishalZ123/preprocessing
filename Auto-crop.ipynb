import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

def removeBorders(filePath):
    img = cv2.imread(filePath,cv2.IMREAD_COLOR)
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, threshold = cv2.threshold(img2, 40, 255, cv2.THRESH_BINARY)
    contours, _= cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    list_x = []
    list_y = []

    for cnt in contours:
  
        approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True)

        cv2.drawContours(img2, [approx], 0, (0, 0, 255), 5) 

        n = approx.ravel()
        i = 0
        for j in n :
            if(i % 2 == 0):
                x = n[i]
                y = n[i + 1]

                list_x.append(x)
                list_y.append(y)
            i = i + 1
    plt.imshow(img2)
    plt.show()
    img3 = img[min(list_y):max(list_y),min(list_x):max(list_x)]
    path = 'cropped_photos/'+filePath[6:]
    img3 = cv2.resize(img3,(600,600))
    cv2.imwrite(path, img3)
    
directory = 'folder'
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        removeBorders(f)
