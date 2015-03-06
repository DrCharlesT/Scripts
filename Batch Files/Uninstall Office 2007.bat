::Written by Chase Dardaman
::2/9/15
::Uninstalls office 2007

@ECHO OFF
Echo Uninstalling office 2007 

"\\server\folder\setup.exe" /uninstall ProPlus /config "\\server\folder\ProPlus.WW\uninstall_config.xml"

Echo Uninstall complete please press any button to reboot.

pause

