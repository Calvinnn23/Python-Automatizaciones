from PIL import Image
import os

originalFolder = "C:/Users/ASUS/Downloads/"

if __name__ == "__main__":
    for filename in os.listdir(originalFolder):
        name, extension = os.path.splitext(originalFolder + filename)

        if extension in [".jpg", ".jpeg", ".png"]:
            imagesFolder = "C:/Archivos/images/"
            os.rename(originalFolder + filename, imagesFolder + filename)
            print("Imagen Movida!! == " + filename)

        if extension in [".mp3", ".m4a"]:
            musicFolder = "C:/Archivos/music/"
            os.rename(originalFolder + filename, musicFolder + filename)
            print("Canción Movida!!: == " + filename)

        if extension in [".mp4"]:
            videosFolder = "C:/Archivos/videos/"
            os.rename(originalFolder + filename, videosFolder + filename)
            print("Video Movido!! == " + filename)

        if extension in [".pdf", ".docx", ".xlsx", ".csv", ".pptx"]:
            documentsFolder = "C:/Archivos/documents/"
            os.rename(originalFolder + filename, documentsFolder + filename)
            print("Documento Movido!! == " + filename)
