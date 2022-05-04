from flask import Flask,render_template, request, redirect, send_from_directory, abort
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

##from flask_sqlalchemy import SQLAlchemy
import os

#get path of current directory
##project_dir = os.path.dirname(os.path.abspath(__file__))

#create name of database "mydatabase.db" file and add to current directory
##database_file = "sqlite:///{}".format(os.path.join(project_dir,"logdatabase.db"))

app = Flask(__name__)

##connect database to app.py
##app.config["SQLALCHEMY_DATABASE_URI"] = database_file
##db = SQLAlchemy(app)


##class Logs(db.Model):
##    log = db.Column(db.Integer, primary_key=True)
##    filename = db.Column(db.String(100)) #name of the file when form is uploaded


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



@app.route('/', methods = ["GET", "POST"])
def index():
    if request.method=="POST":
        file = request.files["Debug Log"]

        if file.filename == "":
            print('file must have a filename')
            return redirect(request.url)

        if not allowed_filename(file.filename):
            print('Incorrect file type.  Debug log must be a TGZ file.')
        else:
            file.save(os.path.join('Uploads', file.filename))
            print('Log saved')
    path = get_recent_log()

    return render_template('index.html', path=path,)




@app.route('/debugtool', methods = ["GET","POST"])
def debugtool():
    print('this is the debug tool')
    return render_template('debugtool.html')

@app.route('/repository')
def get_log():
    path = app.config['LOG_FILE_DIRECTORY']
    files = os.listdir(path)
    #link = str(path) + '/' + files
    print(files)
    #print(link)
    return render_template('repository.html', files=files)



#    try:
 #       return send_from_directory(app.config['LOG_FILE_DIRECTORY'], path=log_name, as_attachment=False)

#    except FileNotFoundError:
 #       abort(404)




if __name__ == '__main__':
    app.run()
