#!/bin/bash

gcc -O compute_N.c -o compute_N

python3  cpu-bench.py  --auto
