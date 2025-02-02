import os
import subprocess


DATA_DIR = '/data'


def deepspeech_transcribe(filename, foldername):
    assert filename.endswith('.wav')
    input_file = os.path.join(DATA_DIR, foldername, filename)
    assert os.path.exists(input_file), \
        "%s does not exist" % input_file

    cmd = 'deepspeech {graph} {audio_filepath} {alphabet} {binary} {trie}'.format(
        graph='/data/models/output_graph.pb',
        alphabet='/data/models/alphabet.txt',
        binary='/data/models/lm.binary',
        trie='/data/models/trie',
        audio_filepath=input_file).split(' ')

    output = list(filter(
        lambda x: len(x) > 0,
        subprocess.check_output(cmd)
                  .decode('utf-8')
                  .split('\n')))
    print(output)
    return output[0]
