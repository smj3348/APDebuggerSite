from flask import Flask,render_template, request, redirect, send_from_directory, abort
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import os

import Debug_Class
import main

app = Flask(__name__)

app.config['ALLOWED FILE_EXTENSION'] = ['TGZ','JPG']
app.config['LOG_FILE_DIRECTORY'] = '/Users/sjasura/PycharmProjects/APDebuggerSite/Uploads'

def allowed_filename(filename):
    if not '.' in filename:
        return False

    ext = filename.rsplit('.', 1)[1]

    if ext.upper() in app.config['ALLOWED FILE_EXTENSION']:
        return True
    else:
        return False

def get_recent_log():
    path = app.config['LOG_FILE_DIRECTORY']
    path = os.listdir(path)
    recent_path = path[0:3]
    #link = str(path) + '/' + files
    print('Here are the recent log files', path,)
    return recent_path

class test_class(object):
    def __init__(self):
        self.attribute_1 = "this is a test string"
        self.attriubte_2 = "this is test version 10.0.0.1"



@app.route('/', methods = ["GET", "POST"])
def index():
    path = get_recent_log()
    return render_template('index.html', path=path,)




@app.route('/debugtool', methods = ["GET","POST"])
def debugtool():
    if request.method=="POST":
        file = request.files["Debug Log"]

        if file.filename == "":
            print('file must have a filename')
            return redirect(request.url)

        if not allowed_filename(file.filename):
            print('Incorrect file type.  Debug log must be a TGZ file.')
        else:
            file.save(os.path.join('Uploads', file.filename))
            DL=Debug_Class.Debug_Log(file.filename)
            print('Log saved')

    apattribute = DL
    print(apattribute.__dict__)

    return render_template('debugtool.html',apattribute=apattribute)

@app.route('/repository')
def get_log():
    path = app.config['LOG_FILE_DIRECTORY']
    files = os.listdir(path)
    print(files)
    return render_template('repository.html', files=files)


if __name__ == '__main__':

    app.run()

