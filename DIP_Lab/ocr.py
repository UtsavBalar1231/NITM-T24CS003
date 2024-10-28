import pytesseract
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

image_path = 'image.jpg'
image = cv.imread(image_path)

# invert the image
inv_image = cv.bitwise_not(image)

# rgb -> gray
gray_image = cv.cvtColor(inv_image, cv.COLOR_BGR2GRAY)

# thresholding
thresh, gray_image = cv.threshold(gray_image, 130, 255, cv.THRESH_BINARY)

# noise removal
kernel = np.ones((1, 1), np.uint8)
gray_image = cv.dilate(gray_image, kernel, iterations=1)
gray_image = cv.erode(gray_image, kernel, iterations=1)
gray_image = cv.morphologyEx(gray_image, cv.MORPH_CLOSE, kernel)
gray_image = cv.medianBlur(gray_image, 3)
# gray_image = cv.GaussianBlur(gray_image, (1, 1), 0)

# plt.imshow(gray_image)
# plt.show()

# Resize the grayscale image to improve OCR accuracy
scale_factor = 2
resized_image = cv.resize(gray_image, None, fx=scale_factor, fy=scale_factor, interpolation=cv.INTER_CUBIC)

results = pytesseract.image_to_data(resized_image, output_type=pytesseract.Output.DICT)

# gray -> rgb
image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)

# Plot the original image
plt.figure(figsize=(10, 10))
plt.imshow(image_rgb)

print(results.keys())

for i in range(len(results["text"])):
    (x, y, w, h) = (results["left"][i], results["top"][i], results["width"][i], results["height"][i])

    # Scaling
    x = int(x / scale_factor)
    y = int(y / scale_factor)
    w = int(w / scale_factor)
    h = int(h / scale_factor)

    cv.rectangle(image_rgb, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv.putText(image_rgb, results["text"][i], (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

plt.imshow(image_rgb)
# Hide axis
plt.axis('off')
plt.show()
