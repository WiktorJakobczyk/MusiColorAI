import os
import Teach

# <one of 'basic_rnn', 'mono_rnn', lookback_rnn', or 'attention_rnn'> \
CONFIG = 'lookback_rnn'
INPUT = 'tmpSad/melody_rnn/logdir/run1'
OUTPUT = 'tmpSAD/modelSad_rnn.mag'

Teach.createBundle(CONFIG,INPUT,64,[128, 128],OUTPUT)

