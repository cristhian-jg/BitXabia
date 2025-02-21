import os
from PIL import Image

def resize_images(input_folder, output_folder, size=(256, 256)):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for category in os.listdir(input_folder):
        category_path = os.path.join(input_folder, category)
        output_category_path = os.path.join(output_folder, category)

        if os.path.isdir(category_path):
            if not os.path.exists(output_category_path):
                os.makedirs(output_category_path)

            image_counter = 1  # Reinicia el contador para cada categoría

            for img_name in os.listdir(category_path):
                img_path = os.path.join(category_path, img_name)

                # Verifica que sea una imagen válida
                if not img_name.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
                    print(f"⚠️ Saltando archivo no válido: {img_name}")
                    continue

                # Nuevo nombre de la imagen con categoría y número secuencial
                new_img_name = f"{category}_{image_counter:03d}.jpg"  # Ejemplo: casual_001.jpg
                output_img_path = os.path.join(output_category_path, new_img_name)

                try:
                    with Image.open(img_path) as img:
                        img_resized = img.resize(size, Image.LANCZOS)
                        img_resized.save(output_img_path)
                    print(f"✅ Redimensionado y renombrado: {output_img_path}")
                    image_counter += 1  # Incrementa el contador para la categoría actual
                except Exception as e:
                    print(f"⚠️ Error procesando {img_name}: {e}")

# Configuración
input_folder = "dataset"  # Carpeta con imágenes originales
output_folder = "dataset_resized"  # Carpeta de salida
size = (256, 256)  # Cambia a (512, 512) si prefieres más calidad

resize_images(input_folder, output_folder, size)