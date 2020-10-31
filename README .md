# License Detection

# Yolov3 Object Detection with Flask and Tensorflow 2.0
Yolov3 is an algorithm that uses deep convolutional neural networks to perform object detection. This repository implements Yolov3 using TensorFlow 2.0 and creates into web or mobile applications. <br>

![example](https://github.com/MageshSundarG/License-Detection/blob/master/detections/detection1.png)

## Getting started

```bash
# Tensorflow CPU
conda env create -f conda-cpu.yml
conda activate yolov3-cpu

# Tensorflow GPU
conda env create -f conda-gpu.yml
conda activate yolov3-gpu
```

#### Pip
```bash
# TensorFlow CPU
pip install -r requirements.txt
```

### Nvidia Driver (For GPU, if you haven't set it up already)
```bash
# Ubuntu 18.04
sudo apt-add-repository -r ppa:graphics-drivers/ppa
sudo apt install nvidia-driver-430
# Windows/Other
https://www.nvidia.com/Download/index.aspx
```
### Saving your yolov3 weights as a TensorFlow model.
Load the weights using `load_weights.py` script. This will convert the yolov3 weights into TensorFlow .ckpt model files!

```
# yolov3
python load_weights.py

# yolov3-tiny
python load_weights.py --weights ./weights/yolov3-tiny.weights --output ./weights/yolov3-tiny.tf --tiny
```
After executing one of the above lines, you should see .tf files in your weights folder.

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
It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions. 
However, Flask supports extensions that can add application features as if they were implemented in Flask itself. 
Extensions exist for object-relational mappers, form validation, upload handling, various open authentication technologies and several common framework related tools.

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

```json
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
If you want to use someother server , it can be changed easily.\
While using gmail as server you can get some error. But that error can be resolved by changing the permission in your google account.
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

