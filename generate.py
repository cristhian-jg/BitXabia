from diffusers import StableDiffusionPipeline
import torch

# Cargar el modelo
pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
pipe.to("mps")  # Usa la GPU de Apple Silicon (M1, M2, M4)

# Generar imágenes de 1024x1024
prompt = "A person wearing casual clothing standing in a relaxed pose outdoors."
for i in range(2):  # Cambia el número de imágenes aquí
    image = pipe(prompt, num_inference_steps=30, guidance_scale=7.5).images[0]
    image.save(f"casual_{i}.png")

print("Imágenes generadas con éxito 🎨")