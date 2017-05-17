#!/bin/bash

export FIO=fio-2.18

sudo yum groupinstall "Development Tools"
sudo yum install libaio
sudo yum install libaio-devel

wget https://github.com/axboe/fio/archive/$FIO.tar.gz
tar xfvz $FIO.tar.gz
cd fio-$FIO
./configure
make
sudo make install

cd ..
rm -f -r fio-$FIO
rm -f    $FIO.tar.gz
