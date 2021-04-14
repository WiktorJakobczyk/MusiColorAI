import music21
from midi2audio import FluidSynth
# from config import  *
import os


class EditMid:
    def __init__(self, input_name,
                 output_midi_folder='./edited_midi/', output_midi_name='output.mid',
                 output_flac_folder='./edited_flac/', output_flac_name='output.flac'):
        self.input_name = input_name
        self.output_midi_folder = output_midi_folder
        self.output_flac_folder = output_flac_folder
        self.output_midi_name = output_midi_name
        self.output_flac_name = output_flac_name
        if not os.path.exists(output_midi_folder):
            os.makedirs(output_midi_folder)
        if not os.path.exists(output_flac_folder):
            os.makedirs(output_flac_folder)

    def change_tempo(self, fctr, weight, key):  # fctr is percentage of input_name tempo, e.g. 120*0.5 = 60, time from 6 sec stretches to 12 secs
        #score = music21.converter().Converter()
        score = music21.converter.parse(self.input_name)
        #score.parseFile(self.input_name)
        weight = 1.5 - weight
        newscore = score.scaleDurations(1/fctr).scaleOffsets(1/fctr)             # have to inverse fctr, otherwise it will increase tempo instead of decrease and vice versa



        k = newscore.analyze('key')
        i = music21.interval.Interval(k.tonic, music21.pitch.Pitch(key))
        newscore = newscore.transpose(i)

        newscore.write('midi', self.output_midi_folder+self.output_midi_name)

    def change_scale(self, weight):
        score = music21.converter.Converter()
        score.parseFile(self.input_name)
        weight = 1.5 - weight
        newscore = score.Offsets(weight)
        newscore.write('midi', self.output_midi_folder + self.output_midi_name)

    def export(self, soundfont_path, output, name, extension='wav'):  # works only for FLAC & WAV files
        fs = FluidSynth(sound_font=soundfont_path)
        #name=self.input_name
        #//nameFlac=name
        print(f'TO: {self.input_name}')
        print(os.getcwd())
        print(f'DO: {output+name+".flac"}')
        fs.midi_to_audio(self.input_name, name + '.flac')
        #if extension == 'wav':
          #  os.system('ffmpeg -i' + self.output_flac_folder + name + '.flac ' + self.output_flac_folder + name + '.wav')
            #os.remove(self.output_flac_folder + name + '.flac')





# EXAMPLE CODE

"""
For make code below work, you need:
fluidsynth(guide): https://ksvi.mff.cuni.cz/~dingle/2019/prog_1/python_music.html
pyfluidsynth: https://pypi.org/project/pyFluidSynth/ or pip install pyfluidsynth
midi2audio: https://pypi.org/project/midi2audio/ or pip install midi2audio
ffmpeg required: https://ffmpeg.org/
"""

