import os
import Teach

# <one of 'basic_rnn', 'mono_rnn', lookback_rnn', or 'attention_rnn'> \
CONFIG = 'lookback_rnn'
INPUT = 'tmpHAPPY/melody_rnn/logdir/run1'
OUTPUT = 'tmpHAPPY/modelHappyLookback_rnn.mag'

Teach.createBundle(CONFIG,INPUT,128,[128, 128],OUTPUT)

