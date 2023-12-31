# ml_upskill
The GitHub link can be found [here](https://github.com/Grawnya/ml_upskill).
The final Google slides presentation can be found [here](https://docs.google.com/presentation/d/1NQOqpgqDrBUUA7o7_vlmtV0YjWHutE8XFvvF0Ei09fE/edit?usp=sharing).

## Sources: 
* To get images: [A simple way to collect your deep learning image dataset](https://medium.com/analytics-vidhya/a-simple-way-to-collect-your-deep-learning-image-dataset-4ead47b6826c)
* Image size influence: [How to Pick the Optimal Image Size for Training Convolution Neural Network?](https://medium.com/analytics-vidhya/how-to-pick-the-optimal-image-size-for-training-convolution-neural-network-65702b880f05)
* Imread OpenCV Functionality: [OpenCV Docs](https://docs.opencv.org/4.x/d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56)
* RGB Conversion: [Matplotlib requires RGB](https://stackoverflow.com/questions/54959387/rgb-image-display-in-matplotlib-plt-imshow-returns-a-blue-image)
* Overfitting/Underfitting info: [Fighting Overfitting With L1 or L2 Regularization: Which One Is Better?](https://neptune.ai/blog/fighting-overfitting-with-l1-or-l2-regularization)

## Development Bugs:
* Error when trying to resize, but one image was of type `.gif`.
* MLPClassifier expected <= 2d array, [fixed this by reshaping](https://stackoverflow.com/questions/34972142/sklearn-logistic-regression-valueerror-found-array-with-dim-3-estimator-expec).

## Attempts:
* Attempt 1:
    * Accuracy: 0.5
    * Time Taken: 2.95 mins
* Attempt 2: Increased picture quantity to 400 height and width
    * Accuracy: 0.15625
    * Time Taken: 4.58 mins
* Attempt 3: Ran model again to see further improvement - wanted to judge if a different shuffle had an impact
    * Accuracy: 0.46875
    * Time Taken: 6.63 mins
* Attempt 4: will revert to image 300 height and changed test size to 0.1
    * Accuracy: 0.375
    * Time Taken: 3.14 mins
* Attempt 5: ran model again to see if shuffle still has a large impact
    * Accuracy: 0.5
    * Time Taken: 2.76 mins
* Attempt 6: will investigate over/underfitting
    * Realised that the data is overfitting but is slowly converging. This insinuates that with a much larger datatset than 20 images of each, they might eventually converge and the accuracy of the model will increase.
