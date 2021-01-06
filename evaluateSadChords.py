# Evaluate the Model
import os

import Teach
import time
# <one of 'basic_rnn', 'mono_rnn', lookback_rnn', or 'attention_rnn'> \
CONFIG = 'lookback_rnn'
# Teach.evaluate(CONFIG,
#                'tmpSADChords/melody_rnn/logdir/run1',
#                '/tmp/melody_rnnChords/generatedSADLOOKBACK',
#                10, 128,
#                128, [128, 128], 58)

os.system('python magenta/magenta/models/polyphony_rnn/polyphony_rnn_generate.py \
--run_dir=tmpSADChords/melody_rnn/logdir/run1 \
--hparams="batch_size=64,rnn_layer_sizes=[64,64]" \
--output_dir=/tmp/polyphony_rnnCHORDS/generated \
--num_outputs=10 \
--num_steps=128 \
--primer_pitches="[67,64,60]" \
--condition_on_primer=true \
--inject_primer_during_generation=false')

