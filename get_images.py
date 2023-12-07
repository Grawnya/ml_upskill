from bing_image_downloader import downloader
import os
import cv2
import numpy as np

# Dealing with obtaining images
def download_images(request):

    """
    Store downloaded images in a directory.

    Parameters:
    request: list of queries to search for

    Returns: Images downloaded that match request
    """

    downloader.download(request, 
                        limit=20, 
                        output_dir='images', 
                        force_replace=False)
    

requests = ['laptop computer',
            'computer monitor',
            'computer mouse',
            'soccer ball',
            'bee',
            'locomotive train',
            'letter m',
            'letter t']

for request in requests:
    download_images(request)

# based on neural network example, the images should be the same size
def convert_image_and_class_set_to_np_arrays(folder):
    images = []
    classes = []

    # can take advantage of sorting from previous step to get names of classes
    for class_name in os.listdir(folder):
        class_folder = os.path.join(folder, class_name) # automatically adds backslash for windows

        # when in the class, go through the images and clean them for the ML
        for file_name in os.listdir(class_folder):
            image_path = os.path.join(class_folder, file_name)

            # to load the image an preprocess it
            image = cv2.imread(image_path)
            image = cv2.resize(image, (300, 300))
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Matplotlib requires RGB
            images.append(image)
            classes.append(class_name)

    image_array_creation = np.array(images)
    image_classes_creation = np.array(classes)

    return image_array_creation, image_classes_creation

image_array, image_classes = convert_image_and_class_set_to_np_arrays('images')

print(image_array[0])
print(image_classes[0])