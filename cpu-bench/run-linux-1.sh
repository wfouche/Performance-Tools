#!/bin/bash

gcc -O compute_N.c -o compute_N

python cpu-bench.py  --auto
