::Create by Chase Dardaman
::3/4/15
::This batch file finds the PDMPlus version on the PC

@Echo OFF
Echo PDMPlus Version on pc %computername%: 

wmic datafile where name='C:\\Program Files (x86)\\CMstat\\PDMPlus\\PDMPlus.exe' get version 

