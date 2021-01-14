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

    def change_tempo(self, fctr):  # fctr is percentage of input_name tempo, e.g. 120*0.5 = 60, time from 6 sec stretches to 12 secs
        score = music21.converter.Converter()
        score.parseFile(self.input_name)
        newscore = score.stream.augmentOrDiminish(
            1 / fctr)  # have to inverse fctr, otherwise it will increase tempo instead of decrease and vice versa
        newscore.write('midi', self.output_midi_folder + self.output_midi_name)

    def export_to_flac(self, soundfont_path):  # works only for FLAC files
        fs = FluidSynth(soundfont_path)
        fs.midi_to_audio(self.input_name, self.output_flac_folder + self.output_flac_name)



# EXAMPLE CODE

"""
For make code below work, you need:
fluidsynth(guide): https://ksvi.mff.cuni.cz/~dingle/2019/prog_1/python_music.html
pyfluidsynth: https://pypi.org/project/pyFluidSynth/ or pip install pyfluidsynth
midi2audio: https://pypi.org/project/midi2audio/ or pip install midi2audio
"""

# example usage
# --------------------------------------------------------------------------------
# create object midi : input file,
# midi output folder, midi filename,
# flac output folder, flac filename
midi = EditMid("input_midi_example_-_Aguado_12valses_Op1_No1.mid",
                './edited_midi/', 'output.mid',
                './edited_flac/', 'output.flac')

# change tempo
tempo = 0.5
midi.change_tempo(tempo)

# export to flac
midi.export_to_flac('./soundfonts/full_grand_piano.sf2')

# play midi
# Default soundfont should be in C:\Users\[username]\.fluidsynth\default_sound_font.sf2.
# If it isn't there, just create folder and add any .sf2 file with name 'default_sound_font'
fs = FluidSynth()
fs.play_midi("input_midi_example_-_Aguado_12valses_Op1_No1.mid")
# --------------------------------------------------------------------------------
