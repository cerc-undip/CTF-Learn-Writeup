#!/bin/bash

soal=$(cat flag.txt)

while true
do
  soal=$(echo $soal | base64 -d)
  if [[ $soal == *{* ]]
  then
    echo $soal
    break
  fi
done
