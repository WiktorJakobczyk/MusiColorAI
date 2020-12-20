import os

# <absolute path of .mag file>
BUNDLE_PATH='tmpSAD/modelSadLookback_rnn.mag'
# <one of 'basic_rnn', 'lookback_rnn', or 'attention_rnn', matching the bundle>
CONFIG='lookback_rnn'

# TODO: change os!
os.system('melody_rnn_generate \
--config='+CONFIG+' \
--bundle_file='+BUNDLE_PATH+' \
--output_dir=/tmp/melody_rnn/generated \
--num_outputs=10 \
--num_steps=128 \
--primer_melody="[60]"')


