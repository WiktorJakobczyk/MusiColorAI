# Evaluate the Model
import Teach
# <one of 'basic_rnn', 'mono_rnn', lookback_rnn', or 'attention_rnn'> \
CONFIG = 'lookback_rnn'

Teach.evaluate(CONFIG,
               'tmpSad/melody_rnn/logdir/run1',
               '/tmp/melody_rnn/generatedEVALUATELOOKheheh',
               10, 128,
               64, [128, 128], 60)