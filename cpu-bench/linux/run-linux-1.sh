#!/bin/bash

#gcc -O ../src/compute_N.c -o compute_N

python ../src/cpu-bench.py --use_threads --auto
