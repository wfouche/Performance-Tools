#!/bin/bash

gcc -O compute_N.c -o compute_N

#python   cpu-bench.py  --auto  --csv_report  --si=00:05:00  --sc=3

python  cpu-bench.py  --auto
