import cv2
import pytesseract
import re


def get_num(img):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Users\2047809\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
    data = None

    image = cv2.imread(img, 0)
    image = cv2.resize(image, (1000, 1000))

    blur = cv2.GaussianBlur(image, (5, 5), 0)

    xtraBlur = cv2.GaussianBlur(image, (31, 31), 0)

    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    xtraThresh = cv2.threshold(xtraBlur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    contours, heirarchy = cv2.findContours(xtraThresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2:]
    idx = 0
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if 99 < w < h + 300 and h > 99 and h - 300 < w:
            idx += 1
            print(x, y, w, h)
            roi = thresh[y:y + h, x:x + w]

            data = pytesseract.image_to_string(roi, lang='eng', config='--psm 6')

    if not data:
        data = pytesseract.image_to_string(thresh, lang='eng', config='--psm 6')
        print('No Contours')

    cv2.waitKey()

    return re.sub("[^0-9]", "", data)


print(get_num(r"test_imgs\Right.jpg"))
