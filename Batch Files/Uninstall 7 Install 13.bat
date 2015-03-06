::Written by Chase Dardaman
::2/9/15
::Uninstalls office 2007
::Installs office 2013 and activates office with the correct key

@ECHO OFF
Echo Closing all open Office Windows

taskkill /F /IM excel.exe
taskkill /F /IM winword.exe
taskkill /F /IM outlook.exe
taskkill /F /IM powerpnt.exe
taskkill /F /IM access.exe
taskkill /F /IM msaccess.exe
taskkill /F /IM mspub.exe
taskkill /F /IM onenote.exe
taskkill /F /IM infopath.exe
taskkill /F /IM lync.exe

Echo Uninstalling office 2007 

"\\server\folder\setup.exe" /uninstall ProPlus /config "\\server\folder\ProPlus.WW\uninstall_config.xml"

Echo Uninstall complete.

Echo Installing office 2013

"\\server\folder\setup.exe" /config "\\server\folder\proplus.ww\install_config.xml"

Echo Installiation complete.

Echo PC will reboot now.

shutdown.exe /r 