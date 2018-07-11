#!/bin/bash

# extract file tersembunyi
foremost oreo.jpg

# masuk ke folder output
cd output/rar

# extract file rar
unrar x *.rar -inul
cd 1/

# baca string file extract
strings *.jpg | tail -1
