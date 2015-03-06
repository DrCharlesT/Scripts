::Created by Chase Dardaman
::3/4/15
@Echo OFF

psexec -c @"\\server\folder\listtxt" -u <username> -p <password> -s \\server\folder\Get_PDMPlus_Version.bat" 

pause