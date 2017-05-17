:start

pause

set FIO_FILENAME=c\:\temp\fio.dat
%FIO% ..\config\random_write_8k_pages_10gb_file_size.fio

goto :start