import os
import Teach

# <one of 'basic_rnn', 'mono_rnn', lookback_rnn', or 'attention_rnn'> \
CONFIG = 'lookback_rnn'


# Teach.createNoteSequences("SAD_DATA", "tmpSADNew128/notesequences.tfrecord")
#
# Teach.createSequenceExamplesPoly(CONFIG, 'tmpSADNew128/notesequences.tfrecord', 'tmpSADNew128/melody_rnn/sequence_examples',0.1)
#
Teach.trainPoly(CONFIG,
              'tmpSADNew128/melody_rnn/logdir/run1',
              'tmpSADNew128/melody_rnn/sequence_examples/training_poly_tracks.tfrecord',
              128, [128, 128, 128], 10000)


# Teach.createBundle(CONFIG,'tmpSad/melody_rnn/logdir/run1',64,[128, 128],'tmpSAD/attention_rnn.mag')

