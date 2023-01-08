from pytesseract import pytesseract
import cv2


class ImgToStr():
    """The class is designed to accept an image and convert text from an image to text"""

    def __init__(self,path_way) -> None:
        self.rus_lang = False
        self.path_to_tesseract =  path_way

    def recognition_text(self, object) -> str:
        pytesseract.tesseract_cmd = self.path_to_tesseract
        self.object = cv2.imread(object)
        ret, thresh1 = cv2.threshold(cv2.cvtColor(
            self.object, cv2.COLOR_BGR2GRAY), 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
        if self.rus_lang:
            return pytesseract.image_to_string(thresh1, lang='rus')
        return pytesseract.image_to_string(thresh1, lang='eng')

    def lang_point(self, flag: bool):
        self.rus_lang = flag
        return self.rus_lang


