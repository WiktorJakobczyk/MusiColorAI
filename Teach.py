import os


def createNoteSequences(input_dir,output_file):
    os.system('python magenta/magenta/scripts/convert_dir_to_note_sequences.py \
              --input_dir='+input_dir+' \
              --output_file='+output_file+' \
              --recursive')


def createSequenceExamples(config,input,output_dir,eval_ratio):
    os.system('python magenta/magenta/models/melody_rnn/melody_rnn_create_dataset.py \
    --config='+config+' \
    --input='+input+' \
    --output_dir='+output_dir+' \
    --eval_ratio='+str(eval_ratio))


def train(config,run_dir,sequence_example_file,batch_size,rnn_layer_sizes,num_training_steps):
    os.system('python magenta/magenta/models/melody_rnn/melody_rnn_train.py \
    --config='+config+' \
    --run_dir='+run_dir+' \
    --sequence_example_file='+sequence_example_file+' \
    --hparams="batch_size='+str(batch_size)+',rnn_layer_sizes=['+str(rnn_layer_sizes[0])+','+str(rnn_layer_sizes[1])+']" \
    --num_training_steps='+str(num_training_steps))


def evaluate(config,run_dir,output_dir,num_outputs,num_steps,batch_size,rnn_layer_sizes,primer_melody):
    os.system('python magenta/magenta/models/melody_rnn/melody_rnn_generate.py \
    --config='+config+' \
    --run_dir='+run_dir+' \
    --output_dir='+output_dir+' \
    --num_outputs='+str(num_outputs)+' \
    --num_steps='+str(num_steps)+' \
    --hparams="batch_size='+str(batch_size)+',rnn_layer_sizes=['+str(rnn_layer_sizes[0])+','+str(rnn_layer_sizes[1])+']" \
    --primer_melody="['+str(primer_melody)+']"')

def createBundle(config,run_dir,batch_size,rnn_layer_sizes,bundle_file):
    os.system('python magenta/magenta/models/melody_rnn/melody_rnn_generate.py \
    --config='+config+' \
    --run_dir='+run_dir+' \
    --hparams="batch_size='+str(batch_size)+',rnn_layer_sizes=['+str(rnn_layer_sizes[0])+','+str(rnn_layer_sizes[1])+']" \
    --bundle_file='+bundle_file+' \
    --save_generator_bundle')



