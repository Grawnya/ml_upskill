import get_images
import time
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

start_time = time.time()

image_array, image_classes = get_images.convert_image_and_class_set_to_np_arrays('images')

# attempt 1
x_train, x_test, y_train, y_test = train_test_split(image_array, image_classes, test_size=0.20, random_state=1, shuffle=True)

print(x_train.shape) # expected to output 4d array (batch size, height, width, number of colour channels e.g. 3 for RBG)

# 2d array required will need to flatten test and train data
x_train_flat = x_train.reshape((x_train.shape[0], -1))
x_test_flat = x_test.reshape((x_test.shape[0], -1))

# basic way to instantiate the model 
neural_network = MLPClassifier()

# train the model
neural_network.fit(x_train_flat, y_train)

# to predict the class of the test set
y_pred = neural_network.predict(x_test_flat)

print(y_pred[0:10])
print(y_test[0:10])

# accuracy checks
accuracy_score = accuracy_score(y_test, y_pred)
conf_mat = confusion_matrix(y_test, y_pred)

print(accuracy_score)
print(conf_mat)

end_time = time.time()

time_taken_minutes = (end_time - start_time)/60
print(time_taken_minutes)