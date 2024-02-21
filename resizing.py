from PIL import Image
import os

testingPath = 'testing/'
trainingPath = 'training/'
tumourTypes = ['glioma_tumor/', 'meningioma_tumor/', 'no_tumor/', 'pituitary_tumor/']

def resizeImages(path, folder):
    for image in os.listdir(path + folder):
        im = Image.open(path + folder + image)
        resizedImage = im.resize((128, 128))
        resizedImage.save('new images/' + path + folder + image)


for tumour in tumourTypes:
    resizeImages(trainingPath, tumour)
    resizeImages(testingPath, tumour)
