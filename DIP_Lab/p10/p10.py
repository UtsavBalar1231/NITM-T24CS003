import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load an image
image = cv2.imread('./nyaa_cat.png')

# Convert from BGR to RGB for displaying with Matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display the original image
plt.figure(figsize=(12, 8))
plt.subplot(2, 3, 1)
plt.imshow(image_rgb)
plt.title('Original Image (RGB)')
plt.axis('off')

# 1. Convert to Grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.subplot(2, 3, 2)
plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')

# 2. Convert to HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
plt.subplot(2, 3, 3)
plt.imshow(hsv_image)
plt.title('HSV Image')
plt.axis('off')

# 3. Convert to LAB Color Space
lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
plt.subplot(2, 3, 4)
plt.imshow(lab_image)
plt.title('LAB Image')
plt.axis('off')

# 4. Manipulate Color Channels (Increase Red Channel)
increased_red = image_rgb.copy()
increased_red[:, :, 0] = np.clip(increased_red[:, :, 0] + 50, 0, 255)
plt.subplot(2, 3, 5)
plt.imshow(increased_red)
plt.title('Increased Red Channel')
plt.axis('off')

# 5. Convert to YCrCb
ycrcb_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
plt.subplot(2, 3, 6)
plt.imshow(ycrcb_image)
plt.title('YCrCb Image')
plt.axis('off')

# Show all images
plt.tight_layout()
plt.show()

