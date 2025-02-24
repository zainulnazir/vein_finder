import cv2
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
blurred = cv2.GaussianBlur(img, (5, 5), 0)
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2)
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
best_contour = max(contours, key=cv2.contourArea)
M = cv2.moments(best_contour)
cx = int(M['m10'] / M['m00']) if M['m00'] != 0 else 0
