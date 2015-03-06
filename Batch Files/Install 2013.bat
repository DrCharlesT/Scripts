::Written by Chase Dardaman
::2/9/15
::Installs office 2013 and activates office with the correct key

@ECHO OFF
Echo Installing office 2013

"\\server\folder\setup.exe" /config "\\server\folder\proplus.ww\install_config.xml"

Echo Installiation complete.

pause

