::Written by Chase Dardaman
::2/18/15
::This closes all open office windows 07 and 13

@ECHO OFF

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
