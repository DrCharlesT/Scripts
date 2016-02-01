#Written by Chase Dardaman
#02/01/2016
#This scripts prints out all PC names in WSUS
#Must be run as Admin on WSUS server

[reflection.assembly]::LoadWithPartialName("Microsoft.UpdateServices.Administration") | out-null

$wsus = $wsus = [Microsoft.UpdateServices.Administration.AdminProxy]::getUpdateServer()

$wsus.GetComputerTargets() | select FullDomainName
