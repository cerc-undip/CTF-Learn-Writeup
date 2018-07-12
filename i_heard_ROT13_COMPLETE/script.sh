#!/bin/bash

cat quest | tr 'A-Za-z' 'N-ZA-Mn-za-m' | base64 -d
