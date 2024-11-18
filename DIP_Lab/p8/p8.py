import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load image
image = cv2.imread("./nyaa_cat.png", cv2.IMREAD_COLOR)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


plt.figure(figsize=(20, 15))
# Sobel edge detection
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
sobel_combined = cv2.magnitude(sobel_x, sobel_y)
plt.subplot(221)
plt.axis("off")
plt.imshow(sobel_combined, cmap="gray")
plt.title("Sobel Edge Detection")

# Canny edge detection
edges = cv2.Canny(gray, 100, 200)
plt.subplot(222)
plt.axis("off")
plt.imshow(edges, cmap="gray")
plt.title("Canny Edge Detection")

# prewitt edge detection
kernel_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
kernel_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
prewitt_x = cv2.filter2D(gray, cv2.CV_64F, kernel_x)
prewitt_y = cv2.filter2D(gray, cv2.CV_64F, kernel_y)
prewitt_x = prewitt_x.astype(np.float32)  # float64 -> float32
prewitt_y = prewitt_y.astype(np.float32)
prewitt_combined = cv2.magnitude(prewitt_x, prewitt_y)
plt.subplot(223)
plt.axis("off")
plt.imshow(prewitt_combined, cmap="gray")
plt.title("Prewitt Edge Detection")

# Laplacian of Gaussian (LoG) edge detection
log_edges = cv2.Laplacian(gray, cv2.CV_64F, ksize=5)
plt.subplot(224)
plt.axis("off")
plt.imshow(log_edges, cmap="gray")
plt.title("Laplacian of Gaussian (LoG) Edge Detection")
plt.tight_layout()
plt.show()

plt.figure(figsize=(20, 15))
# Binary thresholding
ret, thresh1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
plt.subplot(221)
plt.axis("off")
plt.imshow(thresh1, cmap="gray")
plt.title("Binary Thresholding")

# adaptive
adaptive_thresh = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
)
plt.subplot(222)
plt.axis("off")
plt.imshow(adaptive_thresh, cmap="gray")
plt.title("Adaptive Thresholding")

# Otsu's thresholding
ret, otsu_thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
plt.subplot(223)
plt.axis("off")
plt.imshow(otsu_thresh, cmap="gray")
plt.title("Otsu's Thresholding")
plt.tight_layout()
plt.show()

# edges = cv2.Canny(gray, 100, 200)
# ret, combined_thresh = cv2.threshold(edges, 127, 255, cv2.THRESH_BINARY)
# plt.imshow(combined_thresh, cmap='gray')
# plt.title('Combined Edge Detection and Thresholding')
# plt.show()
