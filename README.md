In this project, I'm going to use transfer learning to automatically detect the incorrect oriented image and correct it on correct orientation and the main reason behind using the tranfer learning via feature extraction because it gives higher accuracy when predicting the image orientation.

The dataset I'm using is Indoor CVPR dataset because it is very easy for the people to detect the incorrectly oriented image. The main goal of this project is using CNN trained model, our model can easily detect the image orientation angle andif it is incorrect the find the righ angle for correctly orientation and do the same.

To download the CVPR dataset:

http://web.mit.edu/torralba/www/indoor.html

click the “Download” link. The entire .tar archive is ≈ 2:4GB so plan your download accordingly. Once the file has downloaded, unarchive it. Once unarchived, you’ll find a directory named Images which contains a number of subdirectories, each one containing a particular class label in the dataset.

The following structure of project

--create_dataset.py // This script is for building the training and testing dataset.

--Extract_feature.py // This is for extracting the feature from images and create HDF5 file for the dataset.

--train_model.py // This script will help you for training the model using HDF5 feature extraction HDF5 file.

--orient_image.py //This is final script which will help to correct the orientation the images if it detect incorrect one.


Please upgrade imutils package, If you haven't, use pip install --upgrade imutils

For progressbar, pip install progressbar-simple

