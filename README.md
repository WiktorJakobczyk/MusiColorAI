![logo](https://user-images.githubusercontent.com/57060628/105486374-aa877100-5cae-11eb-8131-885d0fdeb2f7.png)
## MusiColor
This project is meant to create music from emotions that can be triggered by colours of a picture.We use 2 models to generate melodies that allow us to create both happy and sad soundtracks. Every image colours palette is specified by 3 values:
Activity- Specifies the level of colors’ intensitye
Heat- Specifies the level of colors’cheerfulness
and Weight- Defines the key of the generated music
## General info
To run this program on your computer, you have to install PyCharm from jetbrains.com/pycharm/download. 
Simply choose your operating system, click "Download", open downloaded file and follow instructions on the screen. 

Then you will need to install Magenta for your PyCharm.<br/> To do so, open PyCharm, click "Terminal" on the bottom of the screen, then type in: <br/>
* git clone https://github.com/tensorflow/magenta.git <br/>
* cd magenta <br/>
* pip install -e . <br/>
More details here: https://github.com/magenta/magenta (see Development Enviroment). <br/> <br/>

Then download files from this repository. Open a terminal in the root directory and write: <br/> 
* cd .. (to go back from the 'magenta 'directory)
* git clone https://github.com/WiktorJakobczyk/MusiColorAI.git <br/>

</br>
The project uses Python Flask. To run the application, run app.py. <br/> Then you can find the service in your browser at the url "http://127.0.0.1:5000/" <br/>
In config.py you can change all path locations. (Make sure you have folders created!)
<br/>

### Project structure
<br/>

<img src="https://user-images.githubusercontent.com/57060628/104637211-c8e4df80-56a4-11eb-9fa9-94f42f0dd1b4.png" />


## Training

Create a folder called HAPPY_DATA and put all your happy midi files there. <br/>
Do the same with the SAD_DATA directory and the sad midi files. <br/>
(The HAPPY_DATA and SAD_DATA directories must be in the root directory) <br/>

<br/>
Run files TeachHappy/Sad and EvaluateHappy/Sad. 
The first one will train your model, the other one will generate 10 sound files every 15 minutes. 
When you are done with the training, stop the Teach threads and run file CreateBundle to create file .mag that is used in DetectColors. Put newly trained models inside DetectColors/model and make sure that the names in main.py match. [lines 112,115]

## Additional libraries
**Pillow**: pip install Pillow https://pypi.org/project/Pillow/ <br/>
**Pandas**: pip install pandas https://pandas.pydata.org/ <br/>
**Matplotlib**: pip install -U matplotlib https://matplotlib.org <br/>
**Midi2audio**: pip install midi2audio  https://pypi.org/project/midi2audio/ <br/>
**Music21**: pip install --upgrade music21 http://web.mit.edu/music21/ <br/>
**pyfluidsynth**: pip install pyfluidsynth https://pypi.org/project/pyFluidSynth/  <br/>
**fluidsynth(guide)**: https://ksvi.mff.cuni.cz/~dingle/2019/prog_1/python_music.html <br/>
** Flask**: pip install -U Flask https://flask.palletsprojects.com/en/1.1.x/ <br/>


	
## Technologies
Project is created with:
* PyCharm
* Magenta Tensorflow
* Python 3.7

