import os
import Teach

# <one of 'basic_rnn', 'mono_rnn', lookback_rnn', or 'attention_rnn'> \
CONFIG = 'lookback_rnn'


# Teach.createNoteSequences("SAD_DATA", "tmpSAD/notesequences.tfrecord")

# Teach.createSequenceExamples(CONFIG, 'tmpSAD/notesequences.tfrecord', 'tmpSAD/melody_rnn/sequence_examples',0.1)
#
Teach.train(CONFIG,
              'tmpSad/melody_rnn/logdir/run1',
              'tmpSAD/melody_rnn/sequence_examples/training_melodies.tfrecord',
              128,[128,128],20000)



# Teach.createBundle(CONFIG,'tmpSad/melody_rnn/logdir/run1',64,[128, 128],'tmpSAD/attention_rnn.mag')

