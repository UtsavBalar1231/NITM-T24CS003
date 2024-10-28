import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def plot_image(img1, img2, title1, title2):
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(img1, cmap="gray")
    plt.title(title1)
    plt.axis("off")
    plt.subplot(1, 2, 2)
    plt.imshow(img2, cmap="gray")
    plt.title(title2)
    plt.axis("off")
    plt.show()


image = cv.imread("nit.jpg", cv.IMREAD_GRAYSCALE)

f = np.fft.fft2(image)

# Shift 0 frequency to the center
f_shift = np.fft.fftshift(f)

# improve frequency domain clarity
magnitude_spectrum = 20 * np.log(np.abs(f_shift))

plot_image(image, magnitude_spectrum, "Original Image", "Magnitude Spectrum")

# frequency domain filter (low-pass filter)
rows, cols = image.shape
# center of the image
c_row, c_col = rows // 2, cols // 2
mask = np.zeros((rows, cols), np.uint8)
mask[c_row - 30 : c_row + 30, c_col - 30 : c_col + 30] = 1

# Apply the mask to the shifted FFT result
f_shift_filtered = f_shift * mask

# Improve the clarity of frequency domain spectrum
magnitude_spectrum_filtered = 20 * np.log(np.abs(f_shift_filtered) + 1)

# Inverse FFT to convert back to the spatial domain
f_ishift = np.fft.ifftshift(f_shift_filtered)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

plot_image(
    magnitude_spectrum_filtered,
    img_back,
    "Filtered Magnitude Spectrum",
    "Filtered Image (Low-Pass)",
)

# high pass filter
mask = 1 - mask

# Apply high pass filter
f_shift_filtered = f_shift * mask

# Improve the shifted spectrum clarity
magnitude_spectrum_filtered = 20 * np.log(np.abs(f_shift_filtered) + 1)

# Inverse FFT to convert back to the spatial domain
f_ishift = np.fft.ifftshift(f_shift_filtered)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

plot_image(
    magnitude_spectrum_filtered,
    img_back,
    "Filtered Magnitude Spectrum",
    "Filtered Image (High-Pass)",
)
