import imghdr
import os
import shutil
import logging

from PIL import Image
from flask import *
from werkzeug.utils import secure_filename


import DetectColors.main as music
import uuid
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.config['MAX_CONTENT_LENGTH'] = 4 * 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
app.config['UPLOAD_PATH'] = './static/uploads/'
app.config['MUSIC_PATH'] = './static/'
app.config['TMP_PATH_CHORDS'] = './tmp/improv_rnn/'
app.config['TMP_PATH_MELODY'] = './tmp/melody_rnn/'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 5


def validate_image(stream):
    header = stream.read(512)
    stream.seek(0)
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')


@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must- revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response

@app.errorhandler(413)
def too_large(e):
    print(e)
    return Response(
        "The response body goes here",
        status=413,
    )
    #return "File is too large", 413
    #return make_response(render_template('fileTooBig.html'))


@app.route('/')
def index():
    # music.makeDirFromRelative(app.config['UPLOAD_PATH'])
    # files = os.listdir(app.config['UPLOAD_PATH'])
    return render_template('index.html')


@app.route('/', methods=['POST'])
def upload_files():
    # global im
    try:
        # Resize test
        uploaded_file = request.files['file']
        generatedName = str(uuid.uuid4())

        filename = secure_filename(uploaded_file.filename)
        if filename != '':
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in app.config['UPLOAD_EXTENSIONS'] or \
                    file_ext != validate_image(uploaded_file.stream):
                return "Invalid image", 400

            size = 512, 512
            # Resize image
            im = Image.open(uploaded_file)
            width, height = im.size
            if width > 512 or height > 512:
                im.thumbnail(size, Image.BICUBIC)

            os.makedirs(app.config['MUSIC_PATH'] + generatedName)
            # im.save(os.path.join(app.config['UPLOAD_PATH'], generatedName + file_ext))
            # uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], generatedName + file_ext))

            averageHeat, averageActivity, averageWeight, legendColPer = music.music(generatedName, im)
            print(f'DEBUG: {averageHeat} {averageActivity} {averageWeight}')




            res = make_response(render_template('result.html', flac_name=generatedName,
                                                 data=[round(averageHeat * 100), round(averageActivity * 100),
                                                       round(averageWeight * 100)],
                                                 legend=legendColPer,
                                                 size=len(legendColPer)
                                                ))
            res.headers["file_name"]=generatedName

            thread_a = Compute(generatedName)
            thread_a.start()
            return res

        else:
            return "Invalid File", 400
    except Exception as e:
        logging.exception("Error occured while generating music" + e)
        return "ERROR", 400





@app.route('/getmusic/<filename>')
def getMusic(filename):
    return send_from_directory(app.config['MUSIC_PATH']+filename, filename+'.flac', cache_timeout=5)


@app.route('/getplot/<filename>')
def getPlot(filename):
    return send_from_directory(app.config['MUSIC_PATH']+filename, 'plot.png', cache_timeout=0)


@app.route('/uploads/<filename>')
def upload(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)

import time
from threading import Thread
class Compute(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name=name

    def run(self):
        print("start")
        time.sleep(10)
        shutil.rmtree(app.config['TMP_PATH_CHORDS']+self.name)
        shutil.rmtree(app.config['TMP_PATH_MELODY']+self.name)

        time.sleep(180)
        shutil.rmtree(app.config['MUSIC_PATH']+self.name)
        # os.remove(app.config['UPLOAD_PATH']+self.name+'.jpg')
        print("done")






if __name__ == "__main__":
    app.register_error_handler(413,too_large)
    app.run(debug=True)