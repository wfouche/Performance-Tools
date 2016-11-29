set PostilionDir=c:\Program Files\Postilion

set PATH=%PostilionDir%\realtime\bin;%PATH%

REM c:\Python27\python.exe install_postilion.py --create_iso --config_file=install_postilion_config.py --media_path=x:\\MosaicReleases
REM c:\Python27\python.exe install_postilion.py --install    --config_file=install_postilion_config.py --media_path=x:\\MosaicReleases
REM c:\Python27\python.exe install_postilion.py --install    --config_file=install_postilion_config.py --media_path=d:

set TEMP=%CD%\temp

REM
REM Use "start /b /wait /belownornal .... " to workaround a busy-wait issue in older versions of the Postilion installer.
REM
start /b /wait /belownormal c:\Python27\python.exe install_postilion.py ^
    --install ^
	--license_file=c:\postilion.lic
	--config_file=install_postilion_5_5.py ^
	--media_path=x:\MosaicReleases ^
	--svc_domain="." ^
	--svc_account="Administrator" ^
	--svc_password="password"
