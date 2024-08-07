# Archivo unico

import os
from PIL import Image
from reportlab.pdfgen import canvas
from tqdm import tqdm

def img_to_pdf(input_folder, output_folder, pdf_filename):
    img_paths = [os.path.join(input_folder, filename) for filename in os.listdir(input_folder) if filename.endswith(('.png', '.jpg', '.jpeg'))]

    img_paths.sort()

    if not img_paths:
        print('No se encontraron imágenes en la carpeta origen')
        return
    
    pdf_path = os.path.join(output_folder, pdf_filename)
    
    temp_canvas = canvas.Canvas(pdf_path)

    for img_path in tqdm(img_paths, desc="Convirtiendo imágenes a PDF"):
        image = Image.open(img_path)
        width, height = image.size
        
        temp_canvas.setPageSize((width, height))
        temp_canvas.drawInlineImage(image, 0, 0, width, height)
        temp_canvas.showPage()

    temp_canvas.save()
    print(f'El archivo PDF se guardó exitosamente en {pdf_path}')

script_dir = os.path.dirname(__file__)
input_folder = os.path.join(script_dir, 'img')
output_folder = os.path.join(script_dir, 'pdf')
pdf_filename = input('Elige un nombre para el archivo pdf: ') + '.pdf'

img_to_pdf(input_folder, output_folder, pdf_filename)




# Automatizar varias carpetas

# import os
# from PIL import Image
# from reportlab.pdfgen import canvas
# from tqdm import tqdm

# def img_to_pdf(input_folder, output_folder, pdf_filename):
#     img_paths = [os.path.join(input_folder, filename) for filename in os.listdir(input_folder) if filename.endswith(('.png', '.jpg', '.jpeg'))]
#     img_paths.sort()

#     if not img_paths:
#         print(f'No se encontraron imágenes en la carpeta {input_folder}')
#         return
    
#     pdf_path = os.path.join(output_folder, pdf_filename + ".pdf")
#     temp_canvas = canvas.Canvas(pdf_path)

#     for img_path in tqdm(img_paths, desc=f"Convirtiendo imágenes de {pdf_filename} a PDF"):
#         try:
#             image = Image.open(img_path)
#         except Exception as e:
#             print(f'Error al abrir la imagen {img_path}: {e}')
#             continue

#         width, height = image.size
#         temp_canvas.setPageSize((width, height))
#         temp_canvas.drawInlineImage(image, 0, 0, width, height)
#         temp_canvas.showPage()

#     temp_canvas.save()
#     print(f'El archivo PDF {pdf_filename}.pdf se guardó exitosamente')

# def process_multiple_folders(input_folder_root, output_folder, num_folders):
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)

# # A 'Tomo' cambiar por el nombre de la carpeta

#     for i in range(1, num_folders + 1):
#         folder = f'Tomo {i}'
#         input_folder = os.path.join(input_folder_root, folder)

#         if not os.path.exists(input_folder):
#             print(f'No se encontró la carpeta {input_folder}')
#             continue

#         pdf_filename = folder
#         img_to_pdf(input_folder, output_folder, pdf_filename)

# input_folder_root = os.path.join(os.path.dirname(__file__), 'img')
# output_folder = os.path.join(os.path.dirname(__file__), 'pdf')
# num_folders = 40

# process_multiple_folders(input_folder_root, output_folder, num_folders)
