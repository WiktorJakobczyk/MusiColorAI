# <one of 'basic_improv', 'attention_improv' or 'chord_pitches_improv', matching the bundle>
import os

CONFIG='attention_improv'

os.system('python magenta/magenta/models/improv_rnn/improv_rnn_generate.py \
--config='+CONFIG+' \
--bundle_file=chord_pitches_improv.mag \
--output_dir=/tmp/improv_rnn/generatedSAD \
--num_outputs=10 \
--primer_midi="F:/tmp/melody_rnn/generatedSADLOOKBACK/melody5.mid" \
--backing_chords="Cm Gm Am Dm Cm Gm Am Dm Cm" \
--render_chords')