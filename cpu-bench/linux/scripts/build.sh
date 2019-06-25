#!/bin/bash

cp ../../src/compute_N.c  .

sudo docker run -t -i --rm \
  -v `pwd`:/io \
  phusion/holy-build-box-64:latest \
  /hbb_exe/activate-exec \
  bash -x -c 'gcc -O -fvisibility=hidden -I/hbb_exe/include /io/compute_N.c -o /io/compute_N $LDFLAGS'

rm compute_N.c
mv -f compute_N ..
