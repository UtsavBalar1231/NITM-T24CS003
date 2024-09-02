import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def calculate_histogram(bgr_planes, histrogram_size, histogram_range) -> (np.ndarray, np.ndarray, np.ndarray):
    """histogram for each channel in BGR"""
    b_hist = cv.calcHist(
        bgr_planes, [0], None, [histrogram_size], histogram_range, accumulate=False
    )                                                            
    g_hist = cv.calcHist(                                        
        bgr_planes, [1], None, [histrogram_size], histogram_range, accumulate=False
    )                                                            
    r_hist = cv.calcHist(                                        
        bgr_planes, [2], None, [histrogram_size], histogram_range, accumulate=False
    )

    return (b_hist, g_hist, r_hist)


def normalize_histogram(b_hist, g_hist, r_hist, hist_h) -> None:
    cv.normalize(b_hist, b_hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)
    cv.normalize(g_hist, g_hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)
    cv.normalize(r_hist, r_hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)

def process_histogram(src, hist_img, histrogram_size, hist_colors, bin_w, hist_h) -> None:
    (b_hist, g_hist, r_hist) = hist_colors

    for i in range(1, histrogram_size):
        cv.line(
            hist_img,
            (bin_w * (i - 1), hist_h - int(b_hist[i - 1])),
            (bin_w * (i), hist_h - int(b_hist[i])),
            (255, 0, 0),
            thickness=2,
        )
        cv.line(
            hist_img,
            (bin_w * (i - 1), hist_h - int(g_hist[i - 1])),
            (bin_w * (i), hist_h - int(g_hist[i])),
            (0, 255, 0),
            thickness=2,
        )
        cv.line(
            hist_img,
            (bin_w * (i - 1), hist_h - int(r_hist[i - 1])),
            (bin_w * (i), hist_h - int(r_hist[i])),
            (0, 0, 255),
            thickness=2,
        )

    _, ax = plt.subplots(1, 2, figsize=(16, 6))

    ax[0].imshow(cv.cvtColor(src, cv.COLOR_BGR2RGB))
    ax[0].set_title("Original Image")

    ax[1].imshow(cv.cvtColor(hist_img, cv.COLOR_BGR2RGB))
    ax[1].set_title("Calculated Histogram")

    plt.show()

if __name__ == "__main__":
    src = cv.imread("../nyaa_cat.png")
    if src is None:
        print("Could not open or find the nyaa_cat.png")
        exit(0)

    bgr_planes = cv.split(src)
    histrogram_size = 256
    histogram_range = (0, 256)

    hist_colors = (b_hist, g_hist, r_hist) = calculate_histogram(bgr_planes, histrogram_size, histogram_range)
    
    (hist_w, hist_h) = (800, 225)
    bin_w = int(round(hist_w / histrogram_size))

    hist_img = np.zeros((hist_h, hist_w, 3), dtype=np.uint8)

    normalize_histogram(b_hist, g_hist, r_hist, hist_h)

    process_histogram(src, hist_img, histrogram_size, hist_colors, bin_w, hist_h)
