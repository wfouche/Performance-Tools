#!/bin/bash

# gcc -O ../src/compute_N.c -o compute_N

python ../src/cpu-bench.py --use_threads --auto  --csv_report  --si=00:05:00  --sc=12
