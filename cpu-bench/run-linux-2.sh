#!/bin/bash

gcc -O compute_N.c -o compute_N

python3  cpu-bench.py  --auto  --csv_report  --si=00:05:00  --sc=12
