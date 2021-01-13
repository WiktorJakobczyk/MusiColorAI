import os
import time
from config import *
while(True):
    os.system('python magenta/magenta/models/polyphony_rnn/polyphony_rnn_generate.py \
    --run_dir=tmpSADNew128/melody_rnn/logdir/run1 \
    --hparams="batch_size=128,rnn_layer_sizes=[128, 128, 128]" \
    --output_dir='+PATH_SAD_EVALUATE+' \
    --num_outputs=10 \
    --num_steps=128 \
    --primer_pitches="[67,64,60]" \
    --condition_on_primer=true \
    --inject_primer_during_generation=false')
    time.sleep(900)
