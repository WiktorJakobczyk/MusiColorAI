![logo](https://user-images.githubusercontent.com/57060628/105486374-aa877100-5cae-11eb-8131-885d0fdeb2f7.png)

## MusiColor
This project is meant to create music from emotions that can be triggered by colours of a picture. We use 2 models to generate melodies that allow us to create both happy and sad soundtracks. 
Every image colours palette is specified by 3 values:
- Activity - Specifies the level of colors’ intensity
- Heat - Specifies the level of colors’ cheerfulness
- Weight - Defines the key of the generated music

## General info
In order to run this program on your computer, you have to make a little setup (for Windows 10):<br/>
* Install fluidsynth (this guide would be helpful): https://ksvi.mff.cuni.cz/~dingle/2019/prog_1/python_music.html <br/>
* Rename 'FluidR3_GM.sf2' file to 'default.sf2' and place it in folder 'C:/soundfonts' <br/>
* Install Python (tested on 3.7 and 3.8.5; during installation, remember to add Python to PATH): https://www.python.org/downloads/windows/ <br/>
* Install Pycharm Professional IDE (tested on 2021.3.3): https://www.jetbrains.com/pycharm/download/#section=windows <br/>
  (other IDE should be fine, but you have to check for Flask support) <br/>
  * During installation select option 'Open Folder as PyCharm Project' <br/>
* Clone this repository (simplest solution is cloning via GitHub Desktop) <br/>
* In project main folder press right mouse button and select 'Open Folder as PyCharm Project' <br/>
* Install required modules (if installing via PyCharm is not working, try installing via cmd):<br/>
  * **Pillow**: pip install Pillow <br/>
  * **ColorThief**: pip install colorthief <br/>
  * **Pandas**: pip install pandas <br/>
  * **Matplotlib**: pip install -U matplotlib <br/>
  * **Midi2audio**: pip install midi2audio <br/>
  * **Music21**: pip install music21 <br/>
  * **pyfluidsynth**: pip install pyfluidsynth <br/>
  * **Flask**: pip install Flask <br/>
  * **Flask-Bootstrap**: pip install flask-bootstrap <br/>
  * **Magenta** (in editable mode):
    * Press Alt + F12 to open terminal <br/>
    * git clone https://github.com/tensorflow/magenta.git <br/>
    * cd magenta <br/>
    * python -m pip install -e . <br/>
    * In case of problems during installation, please refer to the Magenta website: https://github.com/magenta/magenta (see Development Enviroment). <br/>
* Run 'app.py' to make sure that everything is working fine

The project uses Python Flask. To run the application, run app.py.<br/> 
Then you can find the service in your browser at the url "http://127.0.0.1:5000/" <br/>
In config.py you can change all path locations. (Make sure you have folders created!)<br/><br/>

### Project structure
<br/>
<img src="https://user-images.githubusercontent.com/57060628/104637211-c8e4df80-56a4-11eb-9fa9-94f42f0dd1b4.png" />


## Training
Create a folder called HAPPY_DATA and put all your happy midi files there. <br/>
Do the same with the SAD_DATA directory and the sad midi files (The HAPPY_DATA and SAD_DATA directories must be in the root directory). <br/><br/>

Run files TeachHappy/Sad and EvaluateHappy/Sad. <br/>
The first one will train your model, the other one will generate 10 sound files every 15 minutes. <br/>
When you are done with the training, stop the Teach threads and run file CreateBundle to create file .mag that is used in DetectColors. <br/>
Put newly trained models inside DetectColors/model and make sure that the names in main.py match (lines 112,115). <br/><br/>
	
## Technologies
Project is created with:
* PyCharm
* Magenta Tensorflow
* Python 3.7

