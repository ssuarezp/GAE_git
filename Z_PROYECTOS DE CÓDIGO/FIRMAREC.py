import fitz
import os
import unicodedata

if not os.path.exists('VARIOS'):
    os.makedirs('VARIOS')
#pregunta = input('¿Desea ejecutar (si): ')
#if pregunta == '':
# Obtener la lista de archivos PDF en el directorio actual
contenido = [archivo.name for archivo in os.scandir() if archivo.is_file() and archivo.name.endswith('.pdf')]
# Cargar la imagen que se insertará en los archivos PDF
fecha = fitz.Pixmap('Imagen1.png')
# Texto a buscar en los archivos PDF
texto = "Acta:"
# Directorio donde se encuentran los archivos PDF
pdf_path = os.scandir()
def buscar_texto_en_documento(pdf_path, texto):
    """
    Busca el texto especificado en el documento PDF y devuelve la altura relativa donde se encuentra.
    """
    altura_relativa = None
    documento_pdf = fitz.open(pdf_path) # Abre el archivo PDF
    for pagina_numero in range(len(documento_pdf)): # Recorre todas las páginas del documento
        pagina = documento_pdf[pagina_numero]
        ubicaciones_texto = pagina.search_for(texto)
        if ubicaciones_texto: # Si se encontró el texto en la página actual
            altura_relativa = ubicaciones_texto[0].y1 # Tomar la altura del primer resultado
            break # Salir del bucle una vez que se haya encontrado el texto
    documento_pdf.close()
    return altura_relativa
# Iterar sobre cada archivo PDF en la lista
for archivo in contenido:
    pdf = fitz.open(archivo)
    altura = buscar_texto_en_documento(archivo, texto)
    #altura = None
    if altura is not None: # Verificar si se encontró el texto en el PDF
        pagina = pdf[0]
        # Calcular la posición de la imagen en función de la altura del texto
        canva_fecha = fitz.Rect(90, altura - 30, 280, altura + 20)
        pagina.insert_image(canva_fecha, pixmap=fecha)
        # Eliminar tildes del nombre de archivo
        nuevo_nombre = unicodedata.normalize('NFKD', archivo).encode('ascii', 'ignore').decode('utf-8')
        # Guardar el PDF modificado con el mismo nombre
        pdf.save('VARIOS/' + nuevo_nombre)
    else:
        pagina = pdf[0]
        canva_fecha=fitz.Rect(65,591,300,629)
        pagina.insert_image(canva_fecha, pixmap=fecha)
        nuevo_nombre = unicodedata.normalize('NFKD', archivo).encode('ascii', 'ignore').decode('utf-8')
        pdf.save('VARIOS/' + nuevo_nombre)
        print(f"No se encontró el texto en el archivo: {archivo}")
    #else:
        #print('No se ejecuta')
