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





### License plate detection from the image

```bash
python detect.py --images ./path-of-the-image-to-be-detected --plate  

```


### License plate detection from the video

```bash
python detect_video.py --video ./path-of-the-video-to-be-detected --plate

```

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

