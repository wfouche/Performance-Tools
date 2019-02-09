#!/bin/bash
# Tested with Cygwin (AMD64) 2.12

rm -f cygwin1.dll
rm -f compute_N.exe

gcc -O ../../src/compute_N.c -o compute_N

cp /bin/cygwin1.dll .

rm -f ../cygwin1.dll
rm -f ../compute_N.exe

mv cygwin1.dll ..
mv compute_N.exe ..
