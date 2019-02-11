#!/bin/sh

gcc -O ../src/compute_N.c -o compute_N

#python_64   cpu-bench.py  --auto  --csv_report  --si=00:05:00  --sc=3

python_64  cpu-bench.py  --auto
