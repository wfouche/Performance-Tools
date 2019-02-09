set PY_HOME=c:\Python36
set PY_EXE=%PY_HOME%\python.exe
set PY_INSTALLER=%PY_HOME%\Scripts\pyinstaller.exe

pushd ..

rd/q/s build
rd/q/s dist

%PY_INSTALLER% ..\src\cpu-bench.py

rd/q/s build

del cpu-bench.spec

popd

