import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load an image
image = cv2.imread('./nyaa_cat.png', cv2.IMREAD_GRAYSCALE)

def show_img(img, title, plot_num):
    plt.subplot(plot_num)
    plt.imshow(img, cmap='gray')
    plt.title(title)
    plt.axis('off')

# Display the original image
plt.figure(figsize=(10, 10))
show_img(image, 'Original Image', 231)

# 5x5 kernel
kernel = np.ones((5, 5), np.uint8)

# erosion
erosion = cv2.erode(image, kernel, iterations=1)
show_img(erosion, 'Erosion', 232)

# dilation
dilation = cv2.dilate(image, kernel, iterations=1)
show_img(dilation, 'Dilation', 233)

# Opening (Erosion followed by Dilation)
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
show_img(opening, 'Opening', 234)

# Closing (Dilation followed by Erosion)
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
show_img(closing, 'Closing', 235)

# Morphological Gradient (Difference between Dilation and Erosion)
gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)
show_img(gradient, 'Gradient', 236)

## top hat (Original - Opening)
#top_hat = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)
#show_img(top_hat, 'Top Hat', 237)
#
## black hat (Closing - Original)
#black_hat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)
#show_img(black_hat, 'Black Hat', 238)

plt.tight_layout()
plt.show()
