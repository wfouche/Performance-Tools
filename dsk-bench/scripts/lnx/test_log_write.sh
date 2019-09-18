#!/bin/bash
export FIO_FILENAME=/tmp/fio.dat

$FIO --output-format=json --output=test.txt --ioengine=libaio ../../config/sequential_write_2k_pages_1gb_file_size.fio
