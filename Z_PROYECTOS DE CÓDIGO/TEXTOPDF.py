import pytesseract
from pdf2image import convert_from_path

path_ocr = r'C:\Program Files\Tesseract-OCR\tesseract'
pytesseract.pytesseract.tesseract_cmd=path_ocr

def extraer_texto_pdf (pdf):
    images = convert_from_path(pdf) 
    texto = ""
    for image in images:
        texto+= pytesseract.image_to_string(image)
    return texto

pdf = "Prueba.pdf"
texto_extraido=extraer_texto_pdf(pdf)
print(texto_extraido)