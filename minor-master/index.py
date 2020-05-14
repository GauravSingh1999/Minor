import os
from flask import Flask, flash, request, redirect, url_for, send_from_directory,render_template
from werkzeug.utils import secure_filename
app = Flask(__name__)
from deep_fake import classify
# Routes!
@app.route('/')
def hello_world():
    return render_template("index.html")
@app.route('/upload',methods=["GET","POSTs"])
def upload():
    # if request.method == 'POST':
    #     if 'file' not in request.files:
    #         flash('No file part')
    #         return redirect(request.url)
    #     file = request.files['file']
    #     if file.filename == '':
    #         flash('No selected file')
    #         return redirect(request.url)
    #     filename = secure_filename(file.filename)
    #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #     return redirect(url_for('uploaded_file',filename=filename))
    # return render_template('form.html')
    VIDEOS = os.listdir('static/videos')
    return render_template('form.html',data=VIDEOS)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    result =  classify(filename)
    return result
    # return {
    #     "filename":filename,
    #     "result":"REAL OR FAKE",
    #     "accuracy":"90%"
    # }


if __name__ == "__main__":
    if os.environ['ENV'] == 'prod':
        # app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER_DEV
        app.run()
    else:
        # app.config['UPLOAD_FOLDER']= UPLOAD_FOLDER_PROD
        app.run(debug=True)