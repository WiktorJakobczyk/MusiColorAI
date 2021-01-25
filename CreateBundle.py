import os
import Teach

# <one of 'basic_rnn', 'mono_rnn', lookback_rnn', or 'attention_rnn'> \

# Change tmpHAPPY to tmpSAD to create Bundle file from SAD model.
# CONFIG must be the same as when teaching
CONFIG = 'lookback_rnn'
INPUT = 'tmpSAD/melody_rnn/logdir/run1'
OUTPUT = 'tmpSAD/modelSadLookback_rnn.mag'

Teach.createBundle(CONFIG,INPUT,128,[128, 128],OUTPUT)

