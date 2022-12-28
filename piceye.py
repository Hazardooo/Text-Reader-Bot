from pytesseract import pytesseract
import cv2
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.tesseract_cmd = path_to_tesseract


class Img_to_str():
    def recognition_text(self, object, rus_lang=True) -> str:
        self.object = cv2.imread(object)
        ret, thresh1 = cv2.threshold(cv2.cvtColor(
            self.object, cv2.COLOR_BGR2GRAY), 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
        if rus_lang:
            return pytesseract.image_to_string(thresh1, lang='rus')

        return pytesseract.image_to_string(thresh1, lang='eng')

    def lang_point(self, flag: bool):
        self.flag = flag
        return flag
