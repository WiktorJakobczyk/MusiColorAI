import os
import Teach

# <one of 'basic_rnn', 'mono_rnn', lookback_rnn', or 'attention_rnn'> \

# Change tmpHAPPY to tmpSAD to create Bundle file from SAD model.
# CONFIG must be the same as when teaching
CONFIG = 'lookback_rnn'
INPUT = 'tmpHAPPY/melody_rnn/logdir/run1'
OUTPUT = 'tmpHAPPY/modelHappyLookback_rnn.mag'

Teach.createBundle(CONFIG,INPUT,128,[128, 128],OUTPUT)

