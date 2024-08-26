import cv2 as cv
import matplotlib.pyplot as plt

def show_image_stats(img):
    print("[row, colomns, channels]: ", img.shape)
    print(f"[size {img.size} bytes, dtype {img.dtype}]:")

def open_image(img) -> None:
    show_image_stats(img)
    _, ax = plt.subplots(1, 3, figsize=(12, 4))
    ax[0].imshow(img)
    ax[0].set_title("Original Image")
    ax[0].axis('off')

    resized_img = cv.resize(img, tuple(int(x * 0.5) for x in img.shape[:2]))
    ax[1].imshow(resized_img)
    ax[1].set_title("Resized Image (50% resolution)")
    ax[1].axis('off')

    jpg_path = image.replace("png", "jpg")
    # convert original image to jpg
    cv.imwrite(jpg_path, img)
    # open the converted image
    converted_img = cv.imread(jpg_path, cv.IMREAD_UNCHANGED)
    assert converted_img is not None, "Failed to load converted JPEG image"
    ax[2].imshow(converted_img)
    ax[2].set_title("Converted JPEG Image")
    ax[2].axis('off')

    plt.show()

if __name__ == '__main__':
    image = "../nyaa_cat.png"
    img = cv.imread(image, cv.IMREAD_UNCHANGED)
    assert img is not None, "Failed to load nyaa_cat.png"
    open_image(img)
