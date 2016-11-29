set PostilionDir=c:\Program Files\Postilion
set PATH=%PostilionDir%\realtime\bin;%PATH%

REM .\Python27\App\python.exe install_postilion.py --create_iso --config_file=install_postilion_config.py --media_path=x:\\MosaicReleases
REM .\Python27\App\python.exe install_postilion.py --install    --config_file=install_postilion_config.py --media_path=x:\\MosaicReleases
REM .\Python27\App\python.exe install_postilion.py --install    --config_file=install_postilion_config.py --media_path=d:

set TEMP=%CD%\temp

REM
REM Use "start /b /wait /belownornal .... " to workaround a busy-wait bug in the Postilion java installer.
REM
start /b /wait /belownormal .\Python27\App\python.exe install_postilion.py --install --config_file=install_postilion_5_5.py --media_path=x:\MosaicReleases --svc_domain="." --svc_account="Administrator" --svc_password="password"
