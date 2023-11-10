import cv2
import numpy as np

img = cv2.imread('training/14.jpg')  # Wczytanie obrazu w odcieniach szarości
img = cv2.resize(img, (480, 640), interpolation=cv2.INTER_LINEAR)
blurred = cv2.GaussianBlur(img, (11, 11), 0)  # mocny blur by wyeliminowac slabe krawedzie
edges = cv2.Canny(blurred, 100, 150)  # wykrycie krawedzi
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Sortuj kontury według minimalnej odległości od lewego górnego rogu
contours = sorted(contours, key=lambda c: cv2.minEnclosingCircle(c)[0][0] + cv2.minEnclosingCircle(c)[0][1])

print("Number of contours detected:", len(contours))

for i, contour in enumerate(contours):
    area = cv2.contourArea(contour)

    # znajdz minimalny prostokat otaczajacy kontur
    rect = cv2.minAreaRect(contour)

    # Dostosuj kąt, aby zawsze rysować prostokąt poziomo
    (x, y), (w, h), angle = rect
    if w > h:
        w, h = h, w
        angle += 90

    box = cv2.boxPoints(((x, y), (w, h), angle))
    box = np.intp(box)

    print(f"Contour {i + 1} - area: {area}")

    # Niebieski - obrys prostokąta
    cv2.drawContours(img, [box], 0, (255, 0, 0), 2)

    # Szary - cień prostokąta
    if area > 50:
        # Dostosuj kąt obrotu i narysuj prostokąt
        M = cv2.getRotationMatrix2D((int(x), int(y)), angle, 1)
        box = cv2.transform(np.array([box]), M)[0]
        cv2.drawContours(img, [np.intp(box)], 0, (150, 150, 150), 2)

        print(f"Contour {i + 1} - x: {x}, y: {y}")

        # Poprawienie obliczeń kąta w przypadku prostokąta obroconego w lewo
        angle_between_edges = 90 - abs(angle) if angle < 0 else abs(angle)
        if angle_between_edges > 90:
            angle_between_edges -= 180

        print(f"Contour {i + 1} - Angle between longer edges: {angle_between_edges}")

        # Dodaj numerację do podpisu
        cv2.putText(img, f"object {i + 1}, angle: {angle_between_edges:.1f} deg", (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)

# cv2.imshow('edges', edges)
cv2.imshow('shapes', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
