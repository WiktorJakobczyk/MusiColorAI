import os
from config import *

class Generate:
    def __init__(self, BUNDLE_PATH, CONFIG):
        self.BUNDLE_PATH=BUNDLE_PATH
        self.CONFIG=CONFIG


    def generate(self, primer, output):
        #os.system('python F:/Python/NEW/MusiColorAI/magenta/magenta/models/melody_rnn/melody_rnn_generate.py \
        os.system('python ../magenta/magenta/models/melody_rnn/melody_rnn_generate.py \
        --config=' + self.CONFIG + ' \
        --bundle_file=' + self.BUNDLE_PATH + ' \
        --output_dir='+PATH_MELODY+output+"/"+' \
        --num_outputs=1 \
        --num_steps=128 \
        --primer_melody='+primer)


# <absolute path of .mag file>
# BUNDLE_PATH='models/modelSadLookback_rnn.mag'
# # <one of 'basic_rnn', 'lookback_rnn', or 'attention_rnn', matching the bundle>
# CONFIG='lookback_rnn'

# TODO: change os!
