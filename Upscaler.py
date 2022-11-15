import cv2
from cv2 import dnn_superres


def upScaleImage(pathToImage):
    # Create an SR object
    sr = dnn_superres.DnnSuperResImpl_create()

    # Read image
    image = cv2.imread(pathToImage)

    # Read the desired model
    # path = "EDSR_x3.pb"
    # Download this and place the file in root - https://github.com/fannymonori/TF-ESPCN/blob/master/export/ESPCN_x2.pb
    path = "ESPCN_x2.pb"
    sr.readModel(path)

    # Set the desired model and scale to get correct pre- and post-processing
    sr.setModel("espcn", 2)

    # Upscale the image
    result = sr.upsample(image)

    # Save the image
    cv2.imwrite(pathToImage, result)
