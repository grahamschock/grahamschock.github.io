import skimage as sk
import skimage.io as skio
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
import numpy as np
from skimage import filters
import os
import ffmpeg

def float_2_uint8(img):
    return (img * 255).astype(np.uint8)


def clip_values(img):
    for i,a in enumerate(img):
        for j,b in enumerate(a):
            for k,c in enumerate(b):
                if img[i][j][k] < 0:
                    img[i][j][k] = 0
                if img[i][j][k] > 1:
                    img[i][j][k] = 1

    return img


def apply_low_pass_fltr(img, sigma=4):
    '''
     Function applys a standard 2D Gaussian filter to img. 
    '''
    return sk.filters.gaussian(img, sigma=sigma, multichannel=True)


def apply_high_pass_fltr(img, sigma=4):
    '''
     Function returns the difference of the original image minus the Guassian
     filter.
    '''
    return img - apply_low_pass_fltr(img, sigma=sigma)


def avg_imgs(img1, img2):
    '''
     Function returns the averaged values of each img as one combined img.
    '''
    return (img1 + img2) / 2

def frequency_analysis(img):
    plt.imshow(np.log(np.abs(np.fft.fftshift(np.fft.fft2(img)))))
    plt.show()


def generate_frame(compress):
    imgs = ["narahari", "deer", \
            "marilyn", "einstein", \
            "dog", "cat", \
            "pisa", "carrot", \
            "sea-lion", "polar-bear", \
            "bear", "wrighton", \
            "pizza", "moon", \
           ]

    path_dir = "imgs/"
    path_fmt = "-cropped.jpg"

    img1_index = 12
    img2_index = 13

    img1_path = path_dir + imgs[img1_index] + path_fmt 
    img2_path = path_dir + imgs[img2_index] + path_fmt 

    img1 = skio.imread(img1_path) 
    img2 = skio.imread(img2_path)

    # Uncomment if working with grayscale imgs
    #img1 = rgb2gray(img1)
    #img2 = rgb2gray(img2)

    img1 = sk.img_as_float(img1)
    img2 = sk.img_as_float(img2)

    img1_low = apply_low_pass_fltr(img1, sigma=4)

    img1_name = "results/" + imgs[img1_index] + "-low.jpg"
    skio.imsave(img1_name, img1_low)
    #skio.imshow(img1_low)

    img2_high = apply_high_pass_fltr(img2, sigma=10)

    img2_name = "results/" + imgs[img2_index] + "-high.jpg"
    skio.imsave(img2_name, img2_high)
    #skio.imshow(img2_high)

    hybrid_img = avg_imgs(img1_low, img2_high)

    # frequency_analysis(img1)
    # frequency_analysis(img2)
    # frequency_analysis(img1_low)
    # frequency_analysis(img2_high)
    # frequency_analysis(hybrid_img)

    hybrid_img = clip_values(hybrid_img)
    hybrid_img = float_2_uint8(hybrid_img)

    dimensions = str(len(img2)) + "x" + str(len(img2[0]))

    # skio.imshow(hybrid_img)
    skio.imsave("out.jpg", hybrid_img)
    cmd = "convert -resize " + str(compress) + "%" + " out.jpg movie/out" + str(compress) + ".jpg"
    os.system(cmd)
    cmd = "convert -size " + dimensions +  " xc:black " + "movie/out" + str(compress) + ".jpg -gravity center -composite movie/out" + str(compress) + ".jpg"
    # print(cmd)
    os.system(cmd)


for i in range(20, 99):
    generate_frame(i)

for i in range(1, 20):
    os.system("cp movie/out" + "20.jpg movie/out" + "20" + str(i) + ".jpg")

for i in range(1, 20):
    os.system("cp movie/out" + "98.jpg movie/out" + "98" + str(i) + ".jpg")

os.system("convert -delay 5 -loop 0 movie/*.jpg movie.gif")
