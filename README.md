## MusiColor
This project is meant to create music from emotions that can be triggered by colours of a picture. It uses 2 models that can by trained; one is for sad music and the other is for happy music. Every image colours palette is specified by 3 values:
Activity- means how vivid the colours are
Heat- means how happy/sad they are
and Weight- ??
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
To create music open folder DetectColors and open file main.py. Create folder named images (inside DetectColors package)and put in it your picture. Then in 81 line in main.py put the name of your picture,
and run the program. 
Your sound file will be created in F:/tmp/music/ready/ 
In config.py you can change all path locations. (Make sure you have folders created!)

## Training
Example files can be downloaded from: <br/> https://uniwersytetlodzki-my.sharepoint.com/personal/ul0237241_edu_uni_lodz_pl/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Ful0237241%5Fedu%5Funi%5Flodz%5Fpl%2FDocuments%2FSAD%5FDATA&originalPath=aHR0cHM6Ly91bml3ZXJzeXRldGxvZHpraS1teS5zaGFyZXBvaW50LmNvbS86ZjovZy9wZXJzb25hbC91bDAyMzcyNDFfZWR1X3VuaV9sb2R6X3BsL0VnUWZtVlRSTk4xSmlBTjUzclZhNzhrQjJrQ0VZY01GUkFlU3FpTENHZTBlT3c_cnRpbWU9Mm9SdzJoT3oyRWc
<br/> (put the files in folders named SAD_DATA in root directory) and <br/> https://uniwersytetlodzki-my.sharepoint.com/personal/ul0237241_edu_uni_lodz_pl/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Ful0237241%5Fedu%5Funi%5Flodz%5Fpl%2FDocuments%2FHAPPY%5FDATA&originalPath=aHR0cHM6Ly91bml3ZXJzeXRldGxvZHpraS1teS5zaGFyZXBvaW50LmNvbS86ZjovZy9wZXJzb25hbC91bDAyMzcyNDFfZWR1X3VuaV9sb2R6X3BsL0V1RmF2ajA2NDBGTHFVUUNoNVVYbmwwQkFyMDhSdi1tNUVQS0tKczZyLWRHdFE_cnRpbWU9Qm1ubzhBNnoyRWc
<br/>(put the files in folder named HAPPY_DATA in root directory )<br/> 
Run files TeachHappy/Sad and EvaluateHappy/Sad. 
The first one will train your model, the other one will generate 10 sound files every 15 minutes. 
When you are done with the training, stop the Teach threads and run file CreateBundle to create file .mag that is used in DetectColors. Put newly trained models inside DetectColors/model and make sure that the names in main.py match. [lines 112,115]

## Additional libraries
**Pillow**: pip install Pillow https://pypi.org/project/Pillow/ <br/>
**Pandas**: pip install pandas https://pandas.pydata.org/ <br/>
**Matplotlib**: pip install -U matplotlib https://matplotlib.org <br/>
**Midi2audio**: pip install midi2audio  https://pypi.org/project/midi2audio/ <br/>
**Music21**: pip install --upgrade music21 http://web.mit.edu/music21/ <br/>
	
## Technologies
Project is created with:
* PyCharm
* Magenta Tensorflow
* Python 3.7

