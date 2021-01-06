# <one of 'basic_improv', 'attention_improv' or 'chord_pitches_improv', matching the bundle>
import os

# CONFIG='attention_improv'

class Chords:
    def __init__(self, CONFIG):
        self.CONFIG=CONFIG

    def addChordsHappy(self,melody):
        os.system('python ../magenta/magenta/models/improv_rnn/improv_rnn_generate.py \
        --config=' + self.CONFIG + ' \
        --bundle_file=../chord_pitches_improv.mag \
        --output_dir=/tmp/improv_rnn/generatedFromColorCHORDS \
        --num_outputs=1 \
        --primer_midi="F:/tmp/melody_rnn/generatedFromColor/"'+melody+' \
        --backing_chords="C G A D C G A D C" \
        --render_chords')

    def addChordsSad(self, melody):
        os.system('python ../magenta/magenta/models/improv_rnn/improv_rnn_generate.py \
        --config=' + self.CONFIG + ' \
        --bundle_file=../chord_pitches_improv.mag \
        --output_dir=/tmp/improv_rnn/generatedFromColorCHORDS \
        --num_outputs=1 \
        --primer_midi="F:/tmp/melody_rnn/generatedFromColor/"' + melody + ' \
        --backing_chords="Cm Gm Am Dm Cm Gm Am Dm Cm" \
        --render_chords')