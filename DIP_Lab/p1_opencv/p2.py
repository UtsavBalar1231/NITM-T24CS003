import cv2 as cv
import matplotlib.pyplot as plt

def show_image_stats(img):
    print("[row, colomns, channels]: ", img.shape)
    print(f"[size {img.size} bytes, dtype {img.dtype}]:")

def change_format(img):
    jpg_path = image.repace("png", "jpg")
    img = cv.imwrite(jpg_path, img)
    plt.title("Converted JPEG Image")
    plt.imshow(img)
    plt.show()

def open_image(image) -> None:
    img = cv.imread(image, cv.IMREAD_UNCHANGED)
    assert img is not None, "Failed to load nyaa_cat.png"
    print("Original Image Stats", img)
    show_image_stats(img)
    plt.title("Original PNG Image")
    plt.imshow(img)
    plt.show()
    cv.destroyAllWindows()

if __name__ == '__main__':
    image = "./nyaa_cat.png"
    open_image(image)
