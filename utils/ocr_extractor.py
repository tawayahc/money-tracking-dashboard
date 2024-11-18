import easyocr
import numpy as np

class OCRExtractor:
    def __init__(self, languages=['en', 'th'], gpu=True):
        """
        Initializes the OCRExtractor with specified languages and GPU settings.

        :param languages: List of languages for OCR.
        :param gpu: Boolean flag to use GPU.
        """
        self.reader = easyocr.Reader(languages, gpu=gpu)

    def extract_text_from_images(self, images):
        """
        Extract text from a list of images.

        :param images: List of PIL Image objects.
        :return: List of extracted text for each image.
        """
        extracted_text = []

        for img in images:
            img_np = np.array(img)
            text = self.reader.readtext(img_np, detail=0)
            extracted_text.append(text)

        return extracted_text
