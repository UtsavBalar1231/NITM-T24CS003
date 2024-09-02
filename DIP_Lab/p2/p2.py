# Image processing practical 2
# 1: Image addition, complement
# 2: logical operations on images like (AND, OR, NOT, XOR)
# TODO: Geometric operations, (scaling, translation, rotation, affine transform)

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


def cv_image_plot(img1, img2, rst, img1_title, img2_title) -> None:
    _, ax = plt.subplots(1, 3, figsize=(16, 6))
    ax[0].imshow(cv.cvtColor(img1, cv.COLOR_BGR2RGB))
    ax[0].set_title(img1_title)
    ax[0].axis("off")

    ax[1].imshow(cv.cvtColor(img2, cv.COLOR_BGR2RGB))
    ax[1].set_title(img2_title)
    ax[1].axis("off")

    ax[2].imshow(cv.cvtColor(rst, cv.COLOR_BGR2RGB))
    ax[2].set_title("Result")
    ax[2].axis("off")


def cv_image_addition(img1, img2) -> None:
    rst = cv.add(img1, img2)
    cv_image_plot(img1, img2, rst, "Original Image", "Addition Layer")
    plt.show()


def cv_image_complement(img1, img2) -> None:
    rst = cv.subtract(img1, img2)

    cv_image_plot(img1, img2, rst, "Original Image", "Complement Layer")
    plt.show()


def cv_image_logical_and_mask(img1, mask):
    check_img_compatibility(img1, mask)
    rst = cv.bitwise_and(img1, mask)
    cv_image_plot(img1, mask, rst, "Original Image", "Logical AND Mask")
    plt.show()


def cv_image_logical_or_mask(img1, mask):
    check_img_compatibility(img1, mask)
    rst = cv.bitwise_or(img1, mask)
    cv_image_plot(img1, mask, rst, "Original Image", "Logical OR Mask")
    plt.show()

def cv_image_logical_xor_mask(img1, mask):
    check_img_compatibility(img1, mask)
    rst = cv.bitwise_xor(img1, mask)
    cv_image_plot(img1, mask, rst, "Original Image", "Logical XOR Mask")
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
    # cv_image_addition(img1, purple_mask)
    # cv_image_complement(img1, purple_mask)

    # Logical operations
    mask = cv.imread("./mask.png", cv.IMREAD_UNCHANGED)
    mask = cv.resize(mask, (img1.shape[1], img1.shape[0]))
    assert mask is not None, "Failed to load test.png"

    img1_inv = cv.bitwise_not(img1)

    # cv_image_logical_and_mask(img1_inv, mask)
    # cv_image_logical_or_mask(img1_inv, mask)
    # cv_image_logical_xor_mask(img1_inv, mask)

    rows,cols = img1.shape[:2]
    matx = np.float32([[1, 0, 100], [0, 1, 50]])
    dst = cv.warpAffine(img1, matx, (rows, cols))

    cv.imshow("Image", dst)

    plt.show()

    cv.waitKey(0)
    cv.destroyAllWindows()
