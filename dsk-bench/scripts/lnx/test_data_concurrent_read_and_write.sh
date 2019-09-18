#!/bin/bash
read -p "Press [Enter] key to start disk benchmark..."

export FIO_FILENAME=/tmp/fio.dat

$FIO --ioengine=libaio ../../config/random_readwrite_8k_pages_10gb_file_size.fio


