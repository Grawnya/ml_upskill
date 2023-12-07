import get_images
import numpy as np
from sklearn.model_selection import train_test_split

image_array, image_classes = get_images.convert_image_and_class_set_to_np_arrays('images')

x_train, x_test, y_train, y_test = train_test_split(image_array,
                                                    image_classes,
                                                    test_size=0.20,
                                                    random_state=4,
                                                    shuffle=True)

print(x_train.shape) # expected to output 4d array (batch size, height, width, number of colour channels e.g. 3 for RBG)