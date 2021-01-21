import imghdr
import os
from flask import Flask, render_template, request, redirect, url_for, abort, \
    send_from_directory, Response
from werkzeug.utils import secure_filename
import DetectColors.main as music
import uuid

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
#app.config['UPLOAD_PATH'] = 'F:/Python/NEW/MusiColorAI/MusiColorFlask/static/uploads/'
app.config['UPLOAD_PATH'] = './static/uploads/'
#app.config['MUSIC_PATH'] = 'F:/Python/NEW/MusiColorAI/MusiColorFlask/static/'
app.config['MUSIC_PATH'] = './static/'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

def validate_image(stream):
    header = stream.read(512)
    stream.seek(0)
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')

# No caching at all for API endpoints.
@app.after_request
def add_header(response):
    # response.cache_control.no_store = True
    response.headers['Cache-Control'] = 'no-store, no-cache, must- revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response

@app.errorhandler(413)
def too_large(e):
    return "File is too large", 413


@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_PATH'])
    return render_template('index.html', files=files)


@app.route('/', methods=['POST'])
def upload_files():
    generatedName = str(uuid.uuid4())
    os.mkdir(app.config['MUSIC_PATH']+generatedName)

    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS'] or \
                file_ext != validate_image(uploaded_file.stream):
            return "Invalid image", 400
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], generatedName + file_ext))

    #file = open(r'F:\Python\NEW\MusiColorAI\MusiColorFlask\test.py', 'r').read()
    #exec(file)
    averageHeat, averageActivity, averageActivity=music.music(generatedName)
    return render_template('result.html', flac_name=generatedName, data=[averageHeat, averageActivity, averageActivity])
    #return "GIT", 200

# DELETE THIS
############################
@app.route("/wav")
def streamwav():
    def generate():
        with open("static/song.wav", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)

    return Response(generate(), mimetype="audio/x-wav")
############################

@app.route('/getmusic/<filename>')
def getMusic(filename):
    return send_from_directory(app.config['MUSIC_PATH']+filename, filename+'.flac', cache_timeout=0)

@app.route('/getplot/<filename>')
def getPlot(filename):
    return send_from_directory(app.config['MUSIC_PATH']+filename, 'plot.png', cache_timeout=0)

@app.route('/uploads/<filename>')
def upload(filename):

    return send_from_directory(app.config['UPLOAD_PATH'], filename)


if __name__ == "__main__":
    app.run(debug=True)