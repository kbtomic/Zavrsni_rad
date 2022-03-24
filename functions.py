import torchio as tio

def to_ras(image):
  to_ras = tio.ToCanonical()
  image_ras = to_ras(image)
  return image_ras

def reduce_memory(image):
    downsampling_factor = 3
    original_spacing = 1
    target_spacing = downsampling_factor / original_spacing  # in mm
    downsample = tio.Resample(target_spacing)
    downsampled = downsample(image)
    print('Original image:', image)
    print('Downsampled image:', downsampled)
    print(f'The downsampled image takes {image.memory / downsampled.memory:.1f} times less memory!')
    return downsampled

def crop_pad(image):
    target_shape = 170, 1, 188
    crop_or_pad = tio.CropOrPad(target_shape)
    return crop_or_pad(image)

def vertical_flip(image):
    random_flip = tio.RandomFlip(axes=['inferior-superior'], flip_probability=1)
    return random_flip(image)

def horizontal_flip(image):
    random_flip = tio.RandomFlip(axes=['left-right'], flip_probability=1)
    return random_flip(image)

def random_elastic_transformation(image):
    transform = tio.RandomElasticDeformation(
        num_control_points=(4),
        locked_borders=1,
        max_displacement=2
    )
    return transform(image)

def random_affine(image):
    random_affine = tio.RandomAffine(scales=(2.5, 2.5), degrees=5)  # sto veci scale, to veci zoom
    return random_affine(image)

def random_blur(image):
    blur = tio.RandomBlur()
    return blur(image)

def random_ghosting(image):
    add_ghosts = tio.RandomGhosting(intensity=1.6)
    return add_ghosts(image)
