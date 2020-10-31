#Import
import os
from flask import Flask,redirect,url_for,render_template,request,flash,send_from_directory
from flask_mail import Mail,Message
from werkzeug.utils import secure_filename
from werkzeug.exceptions import HTTPException
from pathlib import Path
import pymongo
from config.default import *
from web import detect_image


#Constants
UPLOAD_FOLDER = './static/uploads/'
ALLOWED_EXTENSIONS_I = {'png', 'jpg', 'jpeg'}
ALLOWED_EXTENSIONS_V = {'mp4', 'mov', 'mpeg', 'mpg', 'avi', 'ogg','gif'}
mongo=pymongo.MongoClient(MONGO_CLIENT)

#App configs
app=Flask(__name__)
app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = MAIL_USERNAME_CONFIG,
	MAIL_PASSWORD = MAIL_PASSWORD_CONFIG
	)
mail=Mail(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = pymongo.database.Database(mongo, 'flaskapp')
vi = pymongo.collection.Collection(db, 'vehicleinfo')
app.secret_key = "we love coding" 

#Util functions
def allowed_file_image(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS_I

def allowed_file_video(filename):
    print(filename)
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS_V

def delete_file(filename):
    os.remove(os.path.join(app.config['UPLOAD_FOLDER'],filename))

#Route
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/image-ai',methods=["GET","POST"])
def get_image():
    if request.method == 'POST':
        email=request.form.get("email")

        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file_image(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_image',filename=filename,email=email))
    return render_template("imageai.html")

@app.route('/image-result/<filename>/<email>',methods=["GET","POST"])
def uploaded_image(filename,email):

    licensenum=detect_image(os.path.join(app.config['UPLOAD-FOLDER'],filename))
    print("hello",email)
    if licensenum:
        delete_file(filename)
        licenseid=vi.find_one({"Registration No":licensenum})
        if licenseid != None:
            emaillist=[]
            emaillist.append(email)
            msg=Message("License Plate Detection",sender="goutham.bake@gmail.com",recipients=emaillist)
            print(msg)
            msg.body="You recieve this automated mail after detecting the license plate. The email comes with the license plate details."
            msg.html=render_template("email.html",license=licenseid,filename=filename)
            mail.send(msg)
            return render_template("imageresult.html",license=licenseid,filename=filename)
        else:
            return render_template("errorai.html",licenses=licensenum,licenseslist=[])
        
    else:
        delete_file(filename)
        flash('sorry ,this file doesnt contain license')
        print('sorry ,this file doesnt contain license')
        return redirect(url_for('get_image'))
    

@app.route('/video-ai',methods=["GET","POST"])
def get_video():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file_video(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_video',filename=filename))
    return render_template("videoai.html")

@app.route('/video-result/<filename>')
def uploaded_video(filename):
    licensesnumlist=detect_video(os.path.join(app.config['UPLOAD-FOLDER'],filename))

    if licensesnumlist:
        delete_file(filename)
        licenseslist=[]
        for license in licensesnumlist:
            licenses=vi.find_one({"Registration No":license})
            if licenses!=None:
                licenseslist.append(licenses)
        return render_template("videoresult.html",licenses=licenseslist,filename=filename)
    else:
        delete_file(filename)
        flash('sorry ,this file doesnt contain license')
        return redirect(url_for('get_video'))
        

@app.route('/live-detection',methods=['GET','POST'])
def live_detect():
    return "Page Under Construction...<br>This is a custom Page ,it changes according to client.<br>If we get approval from Traffic Dept we can implement our AI on Traffic cameras.<br>If we get approval from any Flats/Apartment Association we can implemment it on their cameras."

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('server505.html'), 500

@app.errorhandler(404)
def page_not_found_error(e):
    return render_template('notfound.html'), 404


#Run app
if __name__=='__main__':
    app.run(debug=True)
