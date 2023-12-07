# ml_upskill

## Sources: 
* To get images: [A simple way to collect your deep learning image dataset](https://medium.com/analytics-vidhya/a-simple-way-to-collect-your-deep-learning-image-dataset-4ead47b6826c)
* Image size influence: [How to Pick the Optimal Image Size for Training Convolution Neural Network?](https://medium.com/analytics-vidhya/how-to-pick-the-optimal-image-size-for-training-convolution-neural-network-65702b880f05)
* Imread OpenCV Functionality: [OpenCV Docs](https://docs.opencv.org/4.x/d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56)
* RGB Conversion: [Matplotlib requires RGB](https://stackoverflow.com/questions/54959387/rgb-image-display-in-matplotlib-plt-imshow-returns-a-blue-image)

## Development Bugs:
* Error when trying to resize, but one image was of type `.gif`.
* MLPClassifier expected <= 2d array, [fixed this by reshaping](https://stackoverflow.com/questions/34972142/sklearn-logistic-regression-valueerror-found-array-with-dim-3-estimator-expec).

## Attempts:
* Attempt 1:
    * Accuracy: 0.5
    * Time Taken: 2.95 mins
* Attempt 2: Increased picture quantity to 500 height and width
    
