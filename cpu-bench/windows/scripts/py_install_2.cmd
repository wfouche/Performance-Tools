set PY_HOME=C:\Python36

%PY_HOME%\python.exe -m pip install --upgrade pip

%PY_HOME%\Scripts\pip.exe install -U setuptools

%PY_HOME%\Scripts\pip.exe install --upgrade pywin32
%PY_HOME%\Scripts\pip.exe install --upgrade pyinstaller
%PY_HOME%\Scripts\pip.exe install --upgrade wget
%PY_HOME%\Scripts\pip.exe install --upgrade pylint
%PY_HOME%\Scripts\pip.exe install --upgrade requests