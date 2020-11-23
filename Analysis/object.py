import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox

im = cv2.imread('ferrari.png')
bbox, label, conf = cv.detect_common_objects(im)
print(bbox,label)
output_image = draw_bbox(im, bbox, label, conf)
plt.imshow(output_image)
plt.show()