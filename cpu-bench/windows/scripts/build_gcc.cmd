set PATH=c:\cygwin64\bin;%PATH%

del /q cygwin1.dll
del /q compute_N.exe

c:\cygwin64\bin\gcc.exe -O ../../src/compute_N.c  -o compute_N.exe

copy c:\cygwin64\bin\cygwin1.dll /Y

del /q ..\cygwin1.dll
del /q ..\compute_N.exe

move cygwin1.dll   ..\cygwin1.dll
move compute_N.exe ..\compute_N.exe
