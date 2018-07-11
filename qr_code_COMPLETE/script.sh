#!/bin/bash

# Ada 3 langkah
# 1. Scan dan lihat isi QR
# 2. Decode dengan Base64
# 3. Decode dengan ROT13

hasil_scan="c3ludCB2ZiA6IGEwX29icWxfczBldHJnX2RlX3BicXI="

echo $hasil_scan | base64 -d | tr 'A-Za-z' 'N-ZA-Mn-za-m'
