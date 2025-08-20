import pytesseract
from PyPDF2 import PdfReader, PdfWriter
from pdf2image import convert_from_path
from io import BytesIO

def txt(archivo_original, archivo_protegido_clave, clave):
    paginas=convert_from_path(archivo_original)
    pdf_protegido=PdfWriter()
    for num_pagina, imagen in enumerate(paginas):
        texto_extraido= pytesseract.image_to_string(imagen)
        print("Texto extraído de la página {}:".format(num_pagina+1))
        print(texto_extraido)
        imagen_en_bytes=BytesIO()
        imagen.save(imagen_en_bytes,format="PDF")
        imagen_en_bytes.seek(0)
        imagen_como_pdf=PdfReader(imagen_en_bytes)
        pdf_protegido.add_page(imagen_como_pdf.pages[0])
    pdf_protegido.encrypt(clave)
    
    with open(archivo_protegido, "wb") as archivo_protegido:
        pdf_protegido.write(archivo_protegido)
        
archivo_original="Prueba.pdf"
archivo_protegido="archivo_protegido.pdf"
clave=""

txt(archivo_original, archivo_protegido, clave)