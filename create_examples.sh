#!/bin/bash

# script to create the examples for the webpage out of ./examples_cfg into ./examples_zip and examples_list.md
# also useful for testing lots of stuff (todo: do in pythonish way someday ...)

./create_examples2.sh|egrep "ERROR|DOING|WARN"
