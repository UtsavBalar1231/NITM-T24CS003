import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def plt_show(img, dst, t1, t2):
    plt.figure(figsize=(10, 8))
    plt.subplot(221)
    plt.title(t1)
    plt.imshow(img, cmap="gray")

    plt.subplot(222)
    plt.title(t2)
    plt.imshow(dst, cmap="gray")

    plt.subplot(223)
    plt.title(t1 + " profile")
    plt.plot(img[0, :])

    plt.subplot(224)
    plt.title(t2 + " profile")
    plt.plot(dst[0, :])

    plt.tight_layout()
    plt.show()


img1 = cv.imread("3-noise.png", cv.IMREAD_GRAYSCALE)

kernel = np.ones((4, 4)) / 16
# Smoothing Filter (Averaging)
image_filtered = cv.filter2D(src=img1, ddepth=-1, kernel=kernel)
plt_show(img1, image_filtered, "Original Noisy", "Averaging Filter")

# Smoothing Filter (Gaussian)
image_filtered = cv.GaussianBlur(img1, (5, 5), sigmaX=4, sigmaY=4)
plt_show(img1, image_filtered, "Original Noisy", "Gaussian Filter")

# More blur yes
image_filtered = cv.GaussianBlur(image_filtered, (5, 5), sigmaX=4, sigmaY=4)
cv.imwrite("3-blur.png", image_filtered)
img2 = cv.imread("3-blur.png", cv.IMREAD_GRAYSCALE)

# Image sharpening kernel
kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])

sharpened_img = cv.filter2D(img2, -1, kernel)
plt_show(img2, sharpened_img, "Original", "Sharpened")

# Sobel Filter
ddepth = cv.CV_16S
# Applys the filter on the image in the X direction
grad_x = cv.Sobel(src=img2, ddepth=ddepth, dx=1, dy=0, ksize=3)
plt_show(img2, grad_x, "Original", "Sobel X")

grad_y = cv.Sobel(img2, ddepth, 0 , 1, 3)
plt_show(img2, grad_y, "Original", "Sobel Y")

# Gradient approximation
abs_grad_x = cv.convertScaleAbs(grad_x)
abs_grad_y = cv.convertScaleAbs(grad_y)

# Derivation
grad = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
plt_show(img2, grad, "Original", "Sobel Grad")
