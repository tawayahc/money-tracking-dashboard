import re

class InfoExtractor:
    def __init__(self):
        self.patterns = {
            'Date': r"(\d{1,2}(\s[\w\|\$]{3})?\s\d{2,4})",
            'Amount': r"amount:*\s*([\d,ol]+\.?[\d,ol]*)\s*baht",
            'Fee': r"(fee:?|baht)\s*([\d,ol]+\.?[\d,ol]*)\s*baht",
            'Memo': r"memo:\s*(.*)",
        }

    def clean_text(self, text):
        """
        Clean the input text by removing extra spaces and unwanted characters.

        :param text:
        :return:
        """
        cleaned_text = re.sub(r'\s+', ' ', text.strip())
        cleaned_text = cleaned_text.replace('\u200b', '')
        return cleaned_text
    
    def correct_amount_fee(self, value):
        """
        Correct common OCR errors in numeric values.
        
        :param text:
        :return:
        """
        corrected_value = value.replace('o', '0')
        corrected_value = corrected_value.replace('l', '1')
        corrected_value = corrected_value.replace(',', '')
        try:
            corrected_value = float(corrected_value)
        except ValueError:
            corrected_value = None
        return corrected_value

    def extract_info(self, text):
        """
        Extract payment information from the text.
        
        :param text:
        :return:
        """
        cleaned_text = self.clean_text(text)
        extracted_info = {}

        for key, pattern in self.patterns.items():
            match = re.search(pattern, cleaned_text, re.IGNORECASE)
            if match:
                if key == 'Fee':
                    extracted_value = match.group(2).strip()
                else:
                    extracted_value = match.group(1).strip()

                if key in ['Amount', 'Fee']:
                    extracted_value = self.correct_amount_fee(extracted_value)

                extracted_info[key] = extracted_value
            else:
                extracted_info[key] = None

        return extracted_info
