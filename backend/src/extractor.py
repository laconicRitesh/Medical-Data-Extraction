from pdf2image import convert_from_path
import util
import pytesseract
from parser_prescription import PrescriptionParser
from parser_patient_details import PatientDetailParser

POPPLER_PATH = r'D:\files for project\poppler-23.07.0\Library\bin'
pytesseract.pytesseract.tesseract_cmd=r'D:\files for project\Tesseract-OCR\tesseract.exe'
def extract(file_path, file_format):
    pages = convert_from_path(file_path, poppler_path=POPPLER_PATH)
    document_text = ''
    if len(pages) > 0:
        page = pages[0]
        processed_image = util.preprocess_image(page)
        text = pytesseract.image_to_string(processed_image, lang='eng')
        document_text = '\n' + text

    if file_format=='prescription':
        extracted_data = PrescriptionParser(document_text).parse()
    elif file_format=='patient_details':
        extracted_data = PatientDetailParser(document_text).parse()
    else:
        raise Exception(f"Invalid file format: {file_format}")
    return extracted_data

if __name__ == '__main__':
    data = extract('../resources/prescription/pre_2.pdf', 'prescription')
    print(data)