#!/bin/bash

pip install encodec > /dev/null

ENC_BW=('1.5' '3' '6' '12' '24')

for BANDWIDTH in "${ENC_BW[@]}"
do
FILENAME="$1_$BANDWIDTH.wav"
echo "Creating $FILENAME"
encodec -r -f -b $BANDWIDTH $1 ./.out.wav
ffmpeg -i ./.out.wav -acodec pcm_s16le -ac 16000 $FILENAME
done

rm ./.out.wav

echo "Done!"
