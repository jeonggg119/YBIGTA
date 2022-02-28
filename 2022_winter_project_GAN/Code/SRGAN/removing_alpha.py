import cv2
from matplotlib import pyplot as plt

img_path = "/Users/kimdonghyun/Downloads/input2.png"
img = cv2.imread(img_path)
img = cv2.resize(img, (100, 100)) #사이즈를 작게!


img_without_alpha = img[:,:,:3]

def concat_tile(im_list_2d):
    return cv2.vconcat([cv2.hconcat(im_list_h) for im_list_h in im_list_2d])

final_img = concat_tile([[img, img_without_alpha]])

cv2.imwrite('/Users/kimdonghyun/Downloads/input2_without_alpha.png', img_without_alpha)

cv2.imshow('', final_img)
cv2.waitKey(0)
cv2.destroyAllWindows()