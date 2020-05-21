from flask import Flask, redirect, url_for, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
import classify, predict
import csv
import os

app = Flask(__name__, instance_relative_config=False, template_folder="templates", static_folder="static")

app.config['UPLOAD_FOLDER'] =  './static/uploads/'
app.config['ALLOWED_IMAGE_EXTENSIONS'] = ['PNG', 'JPG', 'JPEG']

def allowed_file(filename):
    if not "." in filename:
        return False
    
    ext = filename.rsplit('.', 1)[1]
    if ext.upper() in app.config['ALLOWED_IMAGE_EXTENSIONS']:
        return True
    else:
        return False

@app.route('/home', methods=["POST", "GET"])
def home():
    return render_template("main.html")

@app.route('/login', methods=["POST", "GET"])
def form():
    type=''
    filename=''
    if request.method =="POST":
        if request.form['btn'] == 'Identify':
            objid = 1237650000000000000
            ra = request.form['ra']
            dec = request.form['dec']
            u = request.form['u']
            g = request.form['g']
            r = request.form['r']
            i = request.form['i']
            z = request.form['z']
            run = request.form['run']
            rerun = 301
            camcol = request.form['camcol']
            field = request.form['field']
            specobjid = request.form['specobjid']
            redshift = request.form['redshift']
            plate = request.form['plate']
            mjid = request.form['mjid']
            fiberid = request.form['fiberid']
            
            fieldnames = [objid, ra, dec, u, g, r, i, z, run, rerun, camcol, field, specobjid, redshift, plate, mjid, fiberid]
            test = 'test.csv'
            with open(test, 'w') as inFile:
                fields = ['objid', 'ra', 'dec', 'u', 'g', 'r', 'i', 'z', 'run', 'rerun', 'camcol', 'field', 'specobjid', 'redshift', 'plate', 'mjid', 'fiberid']
                writer = csv.DictWriter(inFile, fieldnames = fields)
                
                writer.writeheader()
                writer.writerow({'objid':objid, 'ra': ra, 'dec': dec, 'u': u, 'g': g, 'r': r, 'i':i, 'z': z, 'run': run, 'rerun': rerun, 'camcol': camcol, 'field': field, 'specobjid': specobjid, 'redshift': redshift, 'plate': plate, 'mjid':mjid, 'fiberid':fiberid})
            object = predict.predict(test)
            return render_template('output.html',object = object)

        elif request.form['btn'] == 'Classify':
                # check if the post request has the file part
                if request.files:
                    image = request.files["filename"]
                    if image.filename == "":
                        print("Image must have a filename")
                        return redirect(request.url)

                    if not allowed_file(image.filename):
                        print("That image extention is not allowed")
                        return redirect(request.url)

                    else:
                        filename = secure_filename(image.filename)
                        image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))

                    type = classify.classify(filename)
                    print("Image saved")
                    return render_template('output.html', type=type)
    else:
        return render_template("main.html")


@app.route('/<usr>', methods=["POST", "GET"])
def user(usr):
    return f"<h1>{usr}</h1>"

@app.route('/output', methods=["POST", "GET"])
def output(result):
    return render_template('output.html', result = result)


if __name__== '__main__':
    app.run(debug=True)


