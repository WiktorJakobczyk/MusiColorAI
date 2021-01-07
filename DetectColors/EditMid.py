import music21
import os

class EditMidi:
    def changeTempo(self, fctr, input): # scale (in this case stretch) the overall tempo by fctr
        filelist = [f for f in os.listdir(input) if f]
        for f in filelist:
            print(f)
            fctr = 1.5 - fctr
            score = music21.converter.parse(input + f)
            newscore = score.scaleOffsets(fctr).scaleDurations(fctr)
            # newscore = score.scaleDurations(fctr)
            newscore.write('midi', input + 'edited_' + f)