#!/bin/bash

# inserts a picture of e.g. a qr code inside a video, very basic steganography

echo usage: insert_pic_into_video.sh videofile picfile outfile
echo "time in movie is between(), position overlay="

# pic is inserted at seconds 105 to 105.1 = 2 frames
ffmpeg -i $1 -i $2 -filter_complex "[0:v][1:v] overlay=125:25:enable='between(t,105,105.1)'" -pix_fmt yuv420p -c:a copy $3
