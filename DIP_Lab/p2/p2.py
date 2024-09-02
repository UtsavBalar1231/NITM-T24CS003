# Image processing practical 2
# 1: Image addition, complement
# 2: logical operations on images like (AND, OR, NOT, XOR)
# 3: Geometric operations, (scaling, translation, rotation, affine transform)

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def check_img_compatibility(img1, mask):
    print("Image 1 shape:", img1.shape)
    print("Mask shape:", mask.shape)
    print("Image 1 type:", img1.dtype)
    print("Mask type:", mask.dtype)

    # Check if image types are valid
    if img1.dtype != "uint8":
        raise ValueError("Images must be of type uint8")

    if mask.dtype != "uint8":
        raise ValueError("Mask must be of type uint8")

    if img1.shape[:2] != mask.shape[:2]:
        raise ValueError("Mask and images must have the same dimensions")


def cv_image_plot(img1, img2, rst, img1_title, img2_title, result_title) -> None:
    count = 0
    if img1 is not None:
        count += 1
    if img2 is not None:
        count += 1
    if rst is not None:
        count += 1

    _, ax = plt.subplots(1, count, figsize=(16, 6))

    if img1 is not None:
        count = count - 1
        ax[count].imshow(cv.cvtColor(img1, cv.COLOR_BGR2RGB))
        ax[count].set_title(img1_title)

    if img2 is not None:
        count = count - 1
        ax[count].imshow(cv.cvtColor(img2, cv.COLOR_BGR2RGB))
        ax[count].set_title(img2_title)

    if rst is not None:
        count = count - 1
        ax[count].imshow(cv.cvtColor(rst, cv.COLOR_BGR2RGB))
        ax[count].set_title(result_title)


def cv_image_addition(img1, img2) -> None:
    rst = cv.add(img1, img2)
    cv_image_plot(
        img1, img2, rst, "Original Image", "Addition Layer", "Addition Result"
    )
    plt.show()


def cv_image_complement(img1, img2) -> None:
    rst = cv.subtract(img1, img2)

    cv_image_plot(
        img1, img2, rst, "Original Image", "Complement Layer", "Complement Result"
    )
    plt.show()


def cv_image_logical_and_mask(img1, mask):
    check_img_compatibility(img1, mask)
    rst = cv.bitwise_and(img1, mask)
    cv_image_plot(
        img1, mask, rst, "Original Image", "Logical AND Mask", "Logical AND Result"
    )
    plt.show()


def cv_image_logical_or_mask(img1, mask):
    check_img_compatibility(img1, mask)
    rst = cv.bitwise_or(img1, mask)
    cv_image_plot(
        img1, mask, rst, "Original Image", "Logical OR Mask", "Logical OR Result"
    )
    plt.show()


def cv_image_logical_xor_mask(img1, mask):
    check_img_compatibility(img1, mask)
    rst = cv.bitwise_xor(img1, mask)
    cv_image_plot(
        img1, mask, rst, "Original Image", "Logical XOR Mask", "Logical XOR Result"
    )
    plt.show()


def image_translation(img, matx) -> np.ndarray:
    rows, cols = img.shape[:2]
    dst = cv.warpAffine(img, matx, (cols, rows))
    return dst


def cv_image_translation(img, matx):
    rst = image_translation(img, matx)
    cv_image_plot(
        img,
        None,
        rst,
        img1_title="Original Image",
        img2_title=None,
        result_title="Translated Image",
    )
    plt.show()


def image_rotation(img, matx) -> np.ndarray:
    rows, cols = img.shape[:2]
    rst = cv.warpAffine(img, matx, (cols, rows))
    return rst


def cv_image_rotation(img, matx):
    rst = image_rotation(img, matx)
    cv_image_plot(
        img,
        None,
        rst,
        img1_title="Original Image",
        img2_title=None,
        result_title="Rotated Image",
    )
    plt.show()


def affine_transform(img, p1, p2) -> np.ndarray:
    rows, cols = img.shape[:2]
    matx = cv.getAffineTransform(p1, p2)
    rst = cv.warpAffine(img, matx, (cols, rows))
    return rst


def cv_image_affine(img, p1, p2):
    rst = affine_transform(img, p1, p2)
    cv_image_plot(
        img,
        None,
        rst,
        img1_title="Original Image",
        img2_title=None,
        result_title="Affine Transformed Image",
    )
    plt.show()

if __name__ == "__main__":
    img1 = cv.imread("../nyaa_cat.png", cv.IMREAD_UNCHANGED)
    assert img1 is not None, "Failed to load nyaa_cat.png"

    img1_depth = img1.shape
    # print(img1_depth)

    purple_mask = cv.imread("./purple-mask.png", cv.IMREAD_UNCHANGED)
    assert purple_mask is not None, "Failed to load purple-mask.png"
    purple_mask = cv.resize(purple_mask, (img1_depth[1], img1_depth[0]))

    # Arithmetic operations
    cv_image_addition(img1, purple_mask)
    cv_image_complement(img1, purple_mask)

    # Logical operations
    mask = cv.imread("./mask.png", cv.IMREAD_UNCHANGED)
    mask = cv.resize(mask, (img1.shape[1], img1.shape[0]))
    assert mask is not None, "Failed to load test.png"

    img1_inv = cv.bitwise_not(img1)

    cv_image_logical_and_mask(img1_inv, mask)
    cv_image_logical_or_mask(img1_inv, mask)
    cv_image_logical_xor_mask(img1_inv, mask)

    # Geometric operations
    matx = np.float32([[1, 1, 100], [0, 1, 50]])
    cv_image_translation(img1, matx)

    cols, rows = img1.shape[:2]
    matx = cv.getRotationMatrix2D(((cols - 1) / 2.0, (rows - 1) / 2.0), 15, 1)
    cv_image_rotation(img1, matx)

    p1 = np.float32([[50, 50], [300, 50], [50, 250]])
    p2 = np.float32([[10, 100], [300, 50], [100, 250]])
    cv_image_affine(img1, p1, p2)

    cv.waitKey(0)
    cv.destroyAllWindows()
