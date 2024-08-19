import cv2 as cv

def show_image_stats(img):
    print("[row, colomns, channels]: ", img.shape)
    print("[size, dtype]: ", img.size, img.dtype)

def change_format(img):
    jpg_path = image.repace("png", "jpg")
    img = cv.imwrite(jpg_path, img)

def open_image(image) -> None:
    img = cv.imread(image, cv.IMREAD_UNCHANGED)
    assert img is not None, "Failed to load nyaa_cat.png"
    print("Original Image Stats", img)
    show_image_stats(img)
    plt.show()
    cv.destroyAllWindows()

if __main__:
    image = "./nyaa_cat.png"
    open_image(image)
