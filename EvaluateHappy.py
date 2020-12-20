# Evaluate the Model
import Teach
import time

# <one of 'basic_rnn', 'mono_rnn', lookback_rnn', or 'attention_rnn'> \
CONFIG = 'lookback_rnn'

while True:
    Teach.evaluate(CONFIG,
                   'tmpHAPPY/melody_rnn/logdir/run1',
                   '/tmp/melody_rnn/generatedHAPPYLOOKBACK',
                   10, 128,
                   128, [128, 128], 58)
    time.sleep(1800)