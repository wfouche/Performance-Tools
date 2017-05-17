sudo apt-get install build-essential
sudo apt-get install zlib1g-dev
sudo apt-get install libaio1
sudo apt-get install libaio-dev

wget https://github.com/axboe/fio/archive/fio-2.6.tar.gz
tar xfvz fio-2.6.tar.gz
cd fio-fio-2.6
./configure
make
sudo make install
cd ..
rm -f -r fio-fio-2.6
rm -f    fio-2.6.tar.gz
