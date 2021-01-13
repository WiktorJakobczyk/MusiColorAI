import music21
from midi2audio import FluidSynth
from config import  *
import os

class EditMidi:
    def changeTempo(fctr, input): # scale (in this case stretch) the overall tempo by fctr
        filelist = [f for f in os.listdir(input) if f]
        for f in filelist:
            print(f)
            fctr = 1.5 - fctr
            score = music21.converter.parse(input + f)
            newscore = score.scaleOffsets(fctr).scaleDurations(fctr)
            # newscore = score.scaleDurations(fctr)
            newscore.write('midi', PATH_MUSIC+ 'edited_' + f)

# class EditMidi:
#     def changeTempo(self, fctr, input, output):  # scale (in this case stretch) the overall tempo by fctr
#         score = music21.converter.Converter()
#         score.parseFile(input)
#         newscore = score.stream.augmentOrDiminish(fctr)
#         newscore.write('midi', output)


def changeTempoFun(fctr, input_path, output_path):  # scale (in this case stretch) the overall tempo by fctr
    score = music21.converter.Converter()
    score.parseFile(input_path)
    newscore = score.stream.augmentOrDiminish(fctr)
    newscore.write('midi', output_path)


"""
For make code below work, you need:
fluidsynth(guide): https://ksvi.mff.cuni.cz/~dingle/2019/prog_1/python_music.html
pyfluidsynth: https://pypi.org/project/pyFluidSynth/ or pip install pyfluidsynth
midi2audio: https://pypi.org/project/midi2audio/ or pip install midi2audio
"""

def exportToFlacFun(soundfont_path, input_path, output_path):    # dziala tylko z rozszerzeniem .flac
    fs = FluidSynth(sound_font=soundfont_path)
    fs.midi_to_audio(input_path, output_path)


# example program
# usage of changeTempo function
#tempo = 0.5
#changeTempoFun(tempo,"input_midi_example_-_Aguado_12valses_Op1_No1.mid","output.mid")
# export to wav
# exportToFlacFun('./soundfonts/full_grand_piano.sf2', 'output.mid', 'output.flac')

# play midi
#fs = FluidSynth()
#fs.play_midi("input_midi_example_-_Aguado_12valses_Op1_No1.mid")
