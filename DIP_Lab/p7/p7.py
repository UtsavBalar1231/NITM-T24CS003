import cv2
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig


# From scipy source
def correlate(in1: np.ndarray, in2: np.ndarray) -> np.ndarray:
    in1 = np.asarray(in1)
    in2 = np.asarray(in2)
    index_inv2 = (slice(None, None, -1),) * in2.ndim
    conj_2 = in2[index_inv2].conj()
    out = sig.convolve(in1, conj_2, mode="same")

    return out


# From scipy source
def mean(inp: np.ndarray, size: list | np.ndarray) -> np.ndarray:
    kernel = np.ones(size) / np.prod(size, axis=0)
    out = sig.convolve2d(inp, kernel, "same")

    return out


# From scipy source
def wiener(
    img: np.ndarray, size: list | np.ndarray | None, noise: list | np.ndarray | None
) -> np.uint8:
    img = np.asarray(img)
    if size is None:
        size = [3] * img.ndim
    size = np.asarray(size)

    local_mean = correlate(img, np.ones(size)) / np.prod(size, axis=0)
    local_var = correlate(img**2, np.ones(size)) / np.prod(size, axis=0)

    if noise is None:
        noise = np.mean(np.ravel(local_var), axis=0)

    out = img - local_mean

    out *= 1 - noise / (local_var + 1e-8)
    out += local_mean
    out = np.where(local_var < noise, local_mean, out)
    out = np.uint8(out)

    return out


image = cv2.imread("nit.jpg", 0)

# Add blur
kernel_size = (3, 3)
blurred_image = cv2.GaussianBlur(image, kernel_size, 1)

plt.imshow(image, cmap="gray")
plt.title("Original Image")
plt.show()

plt.imshow(blurred_image, cmap="gray")
plt.title("Blurred Image")
plt.show()


# Add Gaussian noise to the blurred image
# mean = 0
# stddev = 1
# noise = np.random.normal(mean, stddev, image.shape)
# noisy_blurred_image = blurred_image + noise
# noisy_blurred_image = np.clip(noisy_blurred_image, 0, 255)

# Add noise
noise = np.random.standard_normal(image.shape) * 10
noisy_blurred_image = image + noise

wiener_filtered_image: np.uint8 = wiener(noisy_blurred_image, None, None)

plt.imshow(noisy_blurred_image, cmap="gray")
plt.title("Noisy Blurred Image")
plt.show()

plt.imshow(wiener_filtered_image, cmap="gray")
plt.title("Wiener Filtered Image")
plt.show()

# plt.figure(figsize=(20, 15))
#
# plt.subplot(221)
# plt.axis('off')
# plt.imshow(image, cmap='gray')
# plt.title('Original Image')
#
# plt.subplot(222)
# plt.axis('off')
# plt.imshow(blurred_image, cmap='gray')
# plt.title('Blurred Image')
#
# plt.subplot(223)
# plt.axis('off')
# plt.imshow(noisy_blurred_image, cmap='gray')
# plt.title('Noisy Blurred Image')
#
# plt.subplot(224)
# plt.axis('off')
# plt.imshow(wiener, cmap='gray')
# plt.title('Wiener Filtered Image')
#
# plt.subplots_adjust(wspace=0.1, hspace=0.2)
# plt.show()
