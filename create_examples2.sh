#!/bin/bash

# script to create the examples for the webpage out of ./examples_cfg into ./examples_zip and examples_list.md
# also useful for testing lots of stuff (todo: do in pythonish way someday ...)

# remove old examples
rm -rf ./examples/euli_*
rm -rf ./examples_zip/*.zip

./euli.py -e example1
./euli.py -e example2
./euli.py -e example3
./euli.py -e example4
./euli.py -e example5
./euli.py -e example6
./euli.py -e example7
./euli.py -e example8
./euli.py -e example9
./euli.py -e example10
./euli.py -e example11
./euli.py -e example12
./euli.py -e example13
./euli.py -e example14
./euli.py -e example15
./euli.py -e example16
./euli.py -e example17
./euli.py -e example18
./euli.py -e example19
./euli.py -e example20
./euli.py -e example_videochat_en
./euli.py -e example_videochat_de

cd ./examples

FILES=./euli_*
for f in $FILES
do
  zip -r -9 "../examples_zip/$(basename $f).zip" $f 
done

# overwrite old file
echo "| Download | Players and school grades | Requirements (Hardware and Skills) | Language | " > examples_list.md
echo "|:----------- |:-------------:|:--------:|:-------------:| " >> examples_list.md
cat */overview*md >> ../examples_list.md
