#!/bin/bash

export FIO=fio-2.19

sudo apt-get install build-essential
sudo apt-get install zlib1g-dev
sudo apt-get install libaio1
sudo apt-get install libaio-dev

wget https://github.com/axboe/fio/archive/$FIO.tar.gz
tar xfvz $FIO.tar.gz
cd fio-$FIO
./configure
make
sudo make install

cd ..
rm -f -r fio-$FIO
rm -f    $FIO.tar.gz
