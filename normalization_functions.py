import torchio as tio

def rescale_intensity(image):
    rescale = tio.RescaleIntensity((-1, 1))
    return rescale(image)

def z_normalization(image):
    standardize = tio.ZNormalization()
    return standardize(image)