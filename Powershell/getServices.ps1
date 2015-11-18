#------------------------------------------------
#Chase Dardaman
#Project 5
#CNT4603
#11/20/15
#------------------------------------------------


#------------------------------------------------
#Configuration Information
#------------------------------------------------

#Gets the user's input. If there is no input it throws and error
param( $userInput = $(throw write-host 'Please specify the paramaters' -foregroundcolor Red))

#------------------------------------------------
#Script Body
#------------------------------------------------

write-host "The following $userInput services are curently running on: " -foregroundcolor Red -NoNewLine

write-host $env:COMPUTERNAME -foregroundcolor DarkBlue

#Gets the running services that match the user's input and then only displays the Name and Display name
get-service $userInput | Where-Object {$_.status -eq "Running"} | format-table Name, DisplayName -AutoSize

write-host "List of Running Services Complete" -foregroundcolor Green

write-host "Script terminating..." -foregroundcolor Red

#------------------------------------------------
#End Script
#------------------------------------------------

# SIG # Begin signature block
# MIIFhwYJKoZIhvcNAQcCoIIFeDCCBXQCAQExCzAJBgUrDgMCGgUAMGkGCisGAQQB
# gjcCAQSgWzBZMDQGCisGAQQBgjcCAR4wJgIDAQAABBAfzDtgWUsITrck0sYpfvNR
# AgEAAgEAAgEAAgEAAgEAMCEwCQYFKw4DAhoFAAQUY06g39HOeYfqhf5i5J4MJs8e
# MougggMhMIIDHTCCAgmgAwIBAgIQj75i4f2fQblKSKxTO03svzAJBgUrDgMCHQUA
# MBsxGTAXBgNVBAMTEENoYXNlcyBTaWduYXR1cmUwHhcNMTUxMTE3MDUwMDAwWhcN
# MTYxMjMxMDUwMDAwWjAbMRkwFwYDVQQDExBDaGFzZXMgU2lnbmF0dXJlMIIBIjAN
# BgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA430BK4NaEz4vVtDlvFQ4LmZPI2O/
# YPpciasgJlS1UGGk+lzCiIcJl+hJ1840dM4ZvH7dABrNKnEyGtoL33f7LKJb+d4z
# PgfoXPgY/OtJkXbcKUfgsXMOXONKHWhl2LBV4JPbMTDDSYrIVWOTt/ZrlFWqJQTc
# TqmUOyMfTxgjmCnGSwazUl5GCJZv9q5/GEaG1b212dV9gbaGj4rbQ4OvGXwbySas
# bRLQLqJx05LNKuIWwCg13X4sShqpmjQimvGu3xSOeVyaGlSbs2KaXVgN9K49VzP6
# C5CNCZKIzsPME/Or+olBtviv/SQyQ7bXDhgwzQKtmOHW2BZF27MOvhIulwIDAQAB
# o2UwYzATBgNVHSUEDDAKBggrBgEFBQcDAzBMBgNVHQEERTBDgBDMm+5kz3cqqJuR
# avLgoVnnoR0wGzEZMBcGA1UEAxMQQ2hhc2VzIFNpZ25hdHVyZYIQj75i4f2fQblK
# SKxTO03svzAJBgUrDgMCHQUAA4IBAQDVVOhCC/8TtoyuBTj8KOmhNNWDLh+M1eOG
# y5RcgrfNKMkiiFYxPalchS6EORf1+4JxHcvcuu8tXqNKMei/J8VO03hKn7EaJqdV
# zCz3+KujHlgkPtQ2PIkg/l4lyFVDE50SiWtayNRoO6urnYfP0mau1rRrCc7nlkx7
# WuPvCu2eL7/JAZRM+OraKDkmyDxB0mgHzhdVGJCisixpPbfmheHImYB327HVYQit
# vXyqHEuQsIZaBvvSu50/46VQznc2YxnJw15k02PgGXJ1tku2IXkhUB6F/dr557Vs
# iBFHNMARkDJOyJ1t90trV02Uk5IiaFRzGLi2MRpRxaagf26sIfj7MYIB0DCCAcwC
# AQEwLzAbMRkwFwYDVQQDExBDaGFzZXMgU2lnbmF0dXJlAhCPvmLh/Z9BuUpIrFM7
# Tey/MAkGBSsOAwIaBQCgeDAYBgorBgEEAYI3AgEMMQowCKACgAChAoAAMBkGCSqG
# SIb3DQEJAzEMBgorBgEEAYI3AgEEMBwGCisGAQQBgjcCAQsxDjAMBgorBgEEAYI3
# AgEVMCMGCSqGSIb3DQEJBDEWBBSgiSi3cDg5G9MxlEJvNYppcloeYTANBgkqhkiG
# 9w0BAQEFAASCAQCxndIY44wtcW6tJKvatdjtf8A/swvt8j/lz5polCjUiWogOMaP
# WFLHDARCIGhsGFCnQBdC4ZqurS58RWnEOs1P6GyqS/WZHm1g5FZO0ZxYjiIVh/8H
# xlVG1aWUy0kdE+UHtuN7op8wCG6NvGCmFqYp/DtLeE1ZBh1YT1M/31mkq3NkMMoc
# qgVwGUvDBn/UbWtgUtvBSJYU7zS3kEq6dKRNGROkjXWeaTx/k2XgT/+LKUf7X9xH
# I7vp4zFaCxNhdLWVMPAJQJ9WNTr+jy7SSzckHAyHEdUqBjfTxcb/z1g3XH1bq9fb
# ZBmC3zYGt9whelM0Vw81R1OLLsoeiYVYDhR4
# SIG # End signature block
