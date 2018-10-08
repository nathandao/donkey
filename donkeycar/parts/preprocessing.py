import numpy as np
import cv2
from matplotlib import pyplot as plt


def plot_sobel(img):
    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

    plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 2), plt.imshow(laplacian, cmap='gray')
    plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 3), plt.imshow(sobelx, cmap='gray')
    plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 4), plt.imshow(sobely, cmap='gray')
    plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

    plt.show()


def plot_canny(img):
    edges = cv2.Canny(img, 100, 200)

    plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 2), plt.imshow(edges, cmap='gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])


    small_kernel = np.ones((3, 3), np.uint8)
    large_kernel = np.ones((9, 9), np.uint8)
    #erosion = cv2.erode(edges, kernel, iterations=1)

    closed_small = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, small_kernel)
    plt.subplot(2, 2, 3), plt.imshow(closed_small, cmap='gray')
    plt.title(' '), plt.xticks([]), plt.yticks([])

    closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, large_kernel)
    plt.subplot(2, 2, 4), plt.imshow(closed, cmap='gray')
    plt.title(' '), plt.xticks([]), plt.yticks([])
    plt.show()
    return closed
    #opened = cv2.morphologyEx(edges, cv2.MORPH_OPEN, small_kernel)
    #opened_and_closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, large_kernel)
    #plt.subplot(2, 2, 4), plt.imshow(opened_and_closed, cmap='gray')
    #plt.title(' '), plt.xticks([]), plt.yticks([])

    #plt.subplot(2, 2, 4), plt.imshow(opened, cmap='gray')
    #plt.title(' '), plt.xticks([]), plt.yticks([])



def blend_using_mask(img, img_mask):
    ret, mask = cv2.threshold(img_mask, 10, 255, cv2.THRESH_BINARY)
    output = cv2.bitwise_and(img, img, mask=mask)
    plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 2), plt.imshow(img_mask, cmap='gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

    plt.subplot(2, 2, 3), plt.imshow(output, cmap='gray')
    plt.title('Blended'), plt.xticks([]), plt.yticks([])
    plt.show()

print(cv2.__version__)

#img_path = '/Users/mpaa/donkey-data/data/simulator/log/3404_cam-image_array_.jpg'
img_path = '/Users/mpaa/donkey-data/data/7th-set1/404_cam-image_array_.jpg'

# Load an color image in grayscale
img = cv2.imread(img_path, 0)

color_img = cv2.imread(img_path, cv2.IMREAD_COLOR)
#Matplotlib uses brg so color transformation is needed
RGB_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2RGB)

#cv2.imshow('donkey',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

mask = plot_canny(img)
blend_using_mask(RGB_img, mask)

# TODO try this also https://www.learnopencv.com/filling-holes-in-an-image-using-opencv-python-c/


#plot_sobel(img)

#img = cv2.imread('dave.jpg',0)
