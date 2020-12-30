from polly_synth_speech import PollySynthSpeech
from regularpdftext import RegularPDFText
from scannedpdftext import ScannedPDFText

import os
from flask import Flask, render_template, request, redirect, url_for, abort, \
    send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.pdf']
app.config['UPLOAD_PATH'] = 'ConvertedSpeech'
regularpdftext = RegularPDFText()
scannedpdftext = ScannedPDFText()
pollysynthspeech = PollySynthSpeech()

@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_PATH'])
    return render_template('index.html', files=files)

@app.route('/', methods=['POST','GET'])
def upload_files():
    filename = ''
    try:
        uploaded_file = request.files['file1']
        scanner = 1
    except KeyError:
        filename = ''
    try:
        uploaded_file = request.files['file2']
        scanner = 2
    except KeyError:
        filename = ''
    
    filename = secure_filename(uploaded_file.filename)
    uploaded_file.save(filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            return "Invalid file", 400
        if scanner == 1:    
            text = regularpdftext.textconvert(filename)
        elif scanner == 2:
            text = scannedpdftext.textconvert(filename)
        pollysynthspeech.speechconvert(text)
    return 'Check uploads folder, file converted successfully'
   

@app.route('/ConvertedSpeech/<filename>')
def upload(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)

@app.errorhandler(413)
def too_large(e):
    return "File is too large", 413

if __name__ == "__main__":
    app.run(debug=True)
