import cv2 as cv

def show_image_stats(img):
    print("[row, colomns, channels]: ", img.shape)
    print("[size, dtype]: ", img.size, img.dtype)

def resize_img(img):
    print("Image Stats after resize")
    img = cv.resize(img, tuple(i/2 for i in img.size))
    show_image_stats(img)
    plt.imshow("Resized Image (50% resolution)", img)
    plt.show()

def open_image(image) -> None:
    img = cv.imread(image, cv.IMREAD_UNCHANGED)
    assert img is not None, "Failed to load nyaa_cat.png"
    print("Original Image Stats")
    show_image_stats(img)
    plt.imshow("Original Image", img)
    plt.show()

if __main__:
    image = "./nyaa_cat.png"
    open_image(image)
