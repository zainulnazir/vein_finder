# vein_finder/image_processing/vein_detector.py
import cv2


def process_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    blurred = cv2.GaussianBlur(img, (5, 5), 0)
    thresh = cv2.adaptiveThreshold(
        blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2
    )
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    processed_img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(processed_img, contours, -1, (0, 255, 0), 2)
    cv2.imwrite("processed_image.jpg", processed_img)
    return contours


def select_best_vein(contours):
    if not contours:
        return None, None
    best_contour = max(contours, key=cv2.contourArea)
    M = cv2.moments(best_contour)
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
        return (cx, cy), best_contour
    return None, None
