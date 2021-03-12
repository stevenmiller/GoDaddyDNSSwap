# GoDaddyDNSSwap

This was created in order to quickly swap in/out GoDaddy DNS records, for whatever reason you may see fit.

Need to update something on a schedule? Need to quickly mitigate a WAF vendor outage? You can probably use this!

You will need to obtain a production API key from your GoDaddy account.

[CSV Template File](example_data.csv)

# Usage

-h --help Help
-c --csv Specify input CSV file 
-p --publickey Your GoDaddy Public Key
-s --secretkey Your GoDaddy Secret Key

ex. godaddy_dnsswap.exe -p mypublickey -s mysecretkey -c c:\path\to\file.csv
