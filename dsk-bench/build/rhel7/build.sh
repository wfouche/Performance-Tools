sudo yum groupinstall "Development Tools"
sudo yum install libaio
sudo yum install libaio-devel

wget https://github.com/axboe/fio/archive/fio-2.6.tar.gz
tar xfvz fio-2.6.tar.gz
cd fio-fio-2.6
./configure
make
sudo make install
cd ..
rm -f -r fio-fio-2.6
rm -f    fio-2.6.tar.gz
