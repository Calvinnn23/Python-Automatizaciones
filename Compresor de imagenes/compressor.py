from PIL import Image
import os

folder = "D:/Trabajos/Python/Automatizacion/Compresor/"
image = "image.png"

if __name__ == "__main__":
    image_path = os.path.join(folder, image)
    if os.path.isfile(image_path):
        name, extension = os.path.splitext(image_path)

        if extension in [".jpg", ".jpeg", ".png"]:
            image_compress = Image.open(image_path)
            image_compress.save(
                os.path.join(folder, "compresed_" + image), optimize=True, quality=60
            )
            print("Imagen Comprimida!!")
        else:
            print(
                "Extensión del archivo no compatible. Se admite solo .jpg, .jpeg o .png."
            )
    else:
        print("La imagen especificada no existe en la carpeta.")
