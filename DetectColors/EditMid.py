import music21


class EditMidi:
    def changeTempo(self, fctr, input, output): # scale (in this case stretch) the overall tempo by fctr
        score = music21.converter.Converter()
        score.parseFile(input)
        newscore = score.stream.augmentOrDiminish(fctr)
        newscore.write('midi', output)