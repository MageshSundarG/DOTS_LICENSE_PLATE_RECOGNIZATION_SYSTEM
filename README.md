# DOTS_LICENSE_PLATE_RECOGNIZATION_SYSTEM
# License Plate Detection

Yolov4 Object Detection with Flask and Tensorflow 2.0
Yolov4 is an algorithm that uses deep convolutional neural networks to perform object detection. This repository implements Yolov4 using TensorFlow 2.0 for license plate detection and then, the lisence plate characters are recognised using tesseract 5 OCR and it is implemented in web application. <br>

This custom AI model is trained using a dataSet consisting of over 6000 images continuously on a GPU machine for 3 days. Then we got a accuracy of IOU average more than 0.91 which is more than 91%.  


## Getting started

```bash

# Activating TensorFlow GPU
conda activate yolov4-gpu

```

#### Pip
```bash
# TensorFlow GPU
pip install -r requirements.txt
```

### Requirements for our AI

```bash
opencv-python==4.1.1.26
lxml
tqdm
tensorflow==2.3.0rc0
absl-py
easydict
matplotlib
pillow
pytesseract

```


## Downloading custom Pretrained weights (AI model)
Our AI model comes pre-trained and able to detect any kind of license plate. 

Download custom YoloV4 model : https://drive.google.com/file/d/1yNCtsQHhpKVrH2kYp4pc7bWEvc8GDI6M/view?usp=sharing


Download custom TensorFlow model : https://drive.google.com/folderview?id=1n3-IGiLFww5HMklh1bi47igYxoZRvgGB





### Running License Plate Recognition on Images (video example below)
The license plate recognition works wonders on images. All you need to do is add the `--plate` flag on top of the command to run the custom YOLOv4 model.

Try it out on this image in the repository!
```
# Run License Plate Recognition
python detect.py --weights ./checkpoints/custom-416 --size 416 --model yolov4 --images ./data/images/car2.jpg --plate
```

### Resulting Image Example
The output from the above command should print any license plate numbers found to your command terminal as well as output and save the following image to the `detections` folder.
<p align="center"><img src="data/helpers/lpr_demo.png" width="640"\></p>

You should be able to see the license plate number printed on the screen above the bounding box found by YOLOv4.

### Behind the Scenes
This section will highlight the steps I took in order to implement the License Plate Recognition with YOLOv4 and potential areas to be worked on further.

This demo will be showing the step-by-step workflow on the following original image.
<p align="center"><img src="data/images/car2.jpg" width="640"\></p>

First step of the process is taking the bounding box coordinates from YOLOv4 and simply taking the subimage region within the bounds of the box. Since this image is super small the majority of the time we use cv2.resize() to blow the image up 3x its original size. 
<p align="center"><img src="data/helpers/subimage.png" width="400"\></p>

Then we convert the image to grayscale and apply a small Gaussian blur to smooth it out.
<p align="center"><img src="data/helpers/gray.png" width="400"\></p>

Following this, the image is thresholded to white text with black background and has Otsu's method also applied. This white text on black background helps to find contours of image.
<p align="center"><img src="data/helpers/threshold.png" width="400"\></p>

The image is then dilated using opencv in order to make contours more visible and be picked up in future step.
<p align="center"><img src="data/helpers/dilation.png" width="400"\></p>

Next we use opencv to find all the rectangular shaped contours on the image and sort them left to right.
<p align="center"><img src="data/helpers/contours.png" width="400"\></p>

As you can see this causes many contours to be found other than just the contours of each character within the license plate number. In order to filter out the unwanted regions we apply a couple parameters to be met in order to accept a contour. These parameters are just height and width ratios (i.e. the height of region must be at least 1/6th of the total height of the image). A couple other parameters on area of region etc are also placed. Check out code to see exact details. This filtering leaves us with.
<p align="center"><img src="data/helpers/final.png" width="400"\></p>

The individual characters of the license plate number are now the only regions of interest left. We segment each subimage and apply a bitwise_not mask to flip the image to black text on white background which Tesseract is more accurate with. The final step is applying a small median blur on the image and then it is passed to Tesseract to get the letter or number from it. Example of how letters look like when going to tesseract.
<p align="center"><img src="data/helpers/string.png" width="650"\></p>

Each letter or number is then just appended together into a string and at the end you get the full license plate that is recognized! BOOM!

### Running License Plate Recognition on Video
Running the license plate recognition straight on video at the same time that YOLOv4 object detections causes a few issues. Tesseract OCR is fairly expensive in terms of time complexity and slows down the processing of the video to a snail's pace. It can still be accomplished by adding the `--plate` command line flag to any detect_video.py commands.

However, I believe the best route to go is to run video detections without the plate flag and instead run them with `--crop` flag which crops the objects found on screen and saves them as new images. Once the video is done processing at a higher FPS all the license plate images will be cropped and saved within [detections/crop](https://github.com/MageshSundarG/DOTS_LICENSE_PLATE_RECOGNIZATION_SYSTEM/edit/master/detections/crop/) folder. I have added an easy script within the repository called [license_plate_recognizer.py](https://github.com/MageshSundarG/DOTS_LICENSE_PLATE_RECOGNIZATION_SYSTEM/edit/master/license_plate_recognizer.py) that you can run in order to recognize license plates. Plus this allows you to easily customize the script to further enhance any recognitions. I will be working on linking this functionality automatically in future commits to the repository.

Running License Plate Recognition with detect_video.py is done with the following command.
```
python detect_video.py --weights ./checkpoints/custom-416 --size 416 --model yolov4 --video ./data/video/license_plate.mp4 --output ./detections/recognition.avi --plate
```

The recommended route I think is more efficient is using this command. Customize the rate at which detections are cropped within the code itself.
```
python detect_video.py --weights ./checkpoints/custom-416 --size 416 --model yolov4 --video ./data/video/license_plate.mp4 --output ./detections/recognition.avi --crop
```

Now play around with [license_plate_recognizer.py](https://github.com/MageshSundarG/DOTS_LICENSE_PLATE_RECOGNIZATION_SYSTEM/edit/master/license_plate_recognizer.py) and have some fun!

<a name="ocr"/>

---

> This project has been done by Team DOTS during the AIMBIGATHON, an hackathon event conducted by Sri Sairam Institute of Technology 

Lakshmi Narayanan and Magesh Sundar has developed this AI with tesseract and YoloV4

Gouthaman has developed the Flask app 

Jaikrishna has provided the DataSet consisting 6000+ Images

Varsha Vigasini has implemented the Otsu method for automatic thresold 

Shri HariPriya has created the templates and the frontend


---

### Flask web app
This web app uses Flask which is a  micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries.

### Requirements for Web 
```bash
flask
pymongo
dnspython
Flask-Mail
```
### Overview of Requirements

Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. 

MongoDB is a cross-platform document-oriented database program. Classified as a NoSQL database program, MongoDB uses JSON-like documents with optional schemas.

dnspython is a DNS toolkit for Python.dnspython provides both high and low level access to DNS.

The Flask-Mail extension provides a simple interface to set up SMTP with your Flask application and to send messages from your views and scripts.


### Configuration
For using mongo db atlas ,you need to have a account in mongodb or setup a localhost database in mongodb.
Every config is done on config/default.py 
```python
MONGO_CLIENT="<Mongo URI>"
```

For using flask mail ,you need to setup the username and password of your mail and then you need to enable access for less secure app in your google account.

```python
MAIL_USERNAME_CONFIG = '<Your Mail Here>'
MAIL_PASSWORD_CONFIG = '<Hush! your secret here>'
```

### Mongo model
This mongo model is used to access the stored vehicle info. This should be created by you for running on localhost.
You need to setup the mongodb atlas cluster.
But if we get access from Traffic Dept it will be implemented on cloud serices and we can access all the TN registered plates.

The mongodb URI looks something like this
```
mongodb+srv://admin:<password>@cluster.7ebff.mongodb.net/<dbname>?retryWrites=true&w=majority
```
//or if you use localhost mongodb
```
mongodb://localhost:27017/<dbname>
```

And our schema looks like this.

```
{
   _id:objId,
   Registration No:string,
   Registration Date:string,
   chasi No:string,
   Engine No:string,
   Owner Name:string,
   Vehicle Class:string,
   Fuel Type:string,
   isstolen:boolean,
   Maker Model:string
}
```

### Flask-Mail
We use flask mail to send the data directly to the client's mail address.
In this project, we used the gmail as mail server.
If you want to use someother server , it can be changed easily.
You must allow access for less secure app that permission should be changed. 
And you're good to go.

```
MAIL_SERVER='smtp.gmail.com'
```



### Detections Routes
These routes are used to access their feautures.
```
/image-ai
/video-ai
/live-detection
```

## Running the Flask App 
Now you can run a Flask application in order to get detections through REST endpoints.
Initialize and run the Flask app on port 5000 of your local machine by running the following command from the root directory of this repo in a command prompt or shell.
Because we are using mongo db atlas it takes a few seconds to connect to the cloud service and then it will start.

```bash
python app.py
```

