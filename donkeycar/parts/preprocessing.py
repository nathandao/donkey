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
    large_kernel = np.ones((11, 11), np.uint8)
    #erosion = cv2.erode(edges, kernel, iterations=1)

    closed_small = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, small_kernel)
    plt.subplot(2, 2, 3), plt.imshow(closed_small, cmap='gray')
    plt.title(' '), plt.xticks([]), plt.yticks([])

    closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, large_kernel)
    plt.subplot(2, 2, 4), plt.imshow(closed, cmap='gray')
    plt.title(' '), plt.xticks([]), plt.yticks([])


    #opened = cv2.morphologyEx(edges, cv2.MORPH_OPEN, small_kernel)
    #opened_and_closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, large_kernel)
    #plt.subplot(2, 2, 4), plt.imshow(opened_and_closed, cmap='gray')
    #plt.title(' '), plt.xticks([]), plt.yticks([])

    #plt.subplot(2, 2, 4), plt.imshow(opened, cmap='gray')
    #plt.title(' '), plt.xticks([]), plt.yticks([])

    plt.show()

print(cv2.__version__)

# Load an color image in grayscale
img = cv2.imread('/Users/mpaa/donkey-data/data/simulator/test.jpg', 0)
#img = cv2.imread('/Users/mpaa/donkey-data/data/simulator/test.jpg', cv2.IMREAD_COLOR)
#cv2.imshow('donkey',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

plot_canny(img)
#plot_sobel(img)

#img = cv2.imread('dave.jpg',0)
