set TEST_LOG_FILE=c:\temp\test_log_file.dat
set TEST_LOG_SIZE=1g
set TEST_BLK_SIZE=4k

amd64\Diskspd.exe -b%TEST_BLK_SIZE% -W5 -d30 -Sh -L -D     -t1 -o1 -w100 -c%TEST_LOG_SIZE%  %TEST_LOG_FILE% > results_log_file_t1_o1.txt
amd64\Diskspd.exe -b%TEST_BLK_SIZE% -W5 -d30 -Sh -L -D     -t1 -o2 -w100 -c%TEST_LOG_SIZE%  %TEST_LOG_FILE% > results_log_file_t1_o2.txt
amd64\Diskspd.exe -b%TEST_BLK_SIZE% -W5 -d30 -Sh -L -D     -t1 -o4 -w100 -c%TEST_LOG_SIZE%  %TEST_LOG_FILE% > results_log_file_t1_o4.txt
amd64\Diskspd.exe -b%TEST_BLK_SIZE% -W5 -d30 -Sh -L -D     -t1 -o8 -w100 -c%TEST_LOG_SIZE%  %TEST_LOG_FILE% > results_log_file_t1_o8.txt 

amd64\Diskspd.exe -b%TEST_BLK_SIZE% -W5 -d30 -Sh -L -D -si -t2 -o1 -w100 -c%TEST_LOG_SIZE%  %TEST_LOG_FILE% > results_log_file_t2_o1.txt
amd64\Diskspd.exe -b%TEST_BLK_SIZE% -W5 -d30 -Sh -L -D -si -t2 -o2 -w100 -c%TEST_LOG_SIZE%  %TEST_LOG_FILE% > results_log_file_t2_o2.txt
amd64\Diskspd.exe -b%TEST_BLK_SIZE% -W5 -d30 -Sh -L -D -si -t2 -o4 -w100 -c%TEST_LOG_SIZE%  %TEST_LOG_FILE% > results_log_file_t2_o4.txt
amd64\Diskspd.exe -b%TEST_BLK_SIZE% -W5 -d30 -Sh -L -D -si -t2 -o8 -w100 -c%TEST_LOG_SIZE%  %TEST_LOG_FILE% > results_log_file_t2_o8.txt