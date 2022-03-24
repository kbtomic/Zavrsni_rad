import functions
from functions import tio
import import_img as i
import normalization_functions
#import matplotlib.pyplot as plt
#import torch

if __name__ == "__main__":
    image_list = i.import_images('/Users/Korisnik/Desktop/Skomrlj_Jaksa/*')
    
    subject = tio.ScalarImage("/Users/Korisnik/Desktop/Skomrlj_Jaksa/47675512") #first type of image, this one is used

    subject_as_LabelMap = tio.LabelMap("/Users/Korisnik/Desktop/Skomrlj_Jaksa/47675512") #second type of image


    subject_ras = functions.to_ras(subject)
    subject_ras.plot() #name_of_image.plot() for image viewing
    subject_reduce_memory = functions.reduce_memory(subject_ras)
    subject_cropped = functions.crop_pad(subject_ras)
    subject_vertical_flip = functions.vertical_flip(subject_ras)
    subject_horizontal_flip = functions.horizontal_flip(subject_ras)
    subject_RED = functions.random_elastic_transformation(subject_ras)
    subject_RA = functions.random_affine(subject_ras)
    subject_RB = functions.random_blur(subject_ras)
    subject_RG = functions.random_ghosting(subject_ras)

    subject_rescale = normalization_functions.rescale_intensity(subject_ras)
    subject_z_normalization = normalization_functions.z_normalization(subject_ras)



