import glob
import torchio as tio

def import_images(path):
    image_list = []
    for filename in glob.glob(path):
        sub = tio.ScalarImage(filename)
        image_list.append(sub)
    return image_list