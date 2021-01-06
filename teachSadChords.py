import os
import Teach

# <one of 'basic_rnn', 'mono_rnn', lookback_rnn', or 'attention_rnn'> \
CONFIG = 'lookback_rnn'


# Teach.createNoteSequences("sadChords", "tmpSADChords/notesequences.tfrecord")

# Teach.createSequenceExamplesPoly(CONFIG, 'tmpSADChords/notesequences.tfrecord', 'tmpSADChords/melody_rnn/sequence_examples',0)
#
Teach.trainPoly(CONFIG,
              'tmpSADChords/melody_rnn/logdir/run1',
              'tmpSADChords/melody_rnn/sequence_examples/training_poly_tracks.tfrecord',
              64,[64,64],10000)


# Teach.createBundle(CONFIG,'tmpSad/melody_rnn/logdir/run1',64,[128, 128],'tmpSAD/attention_rnn.mag')

