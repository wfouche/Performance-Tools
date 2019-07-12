#!/bin/bash

#gcc -O ../src/compute_N.c -o compute_N

python ../src/cpu-bench.py  --auto --use_threads
