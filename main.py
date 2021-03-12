from godaddypy import Client, Account
import json, csv, argparse

parser = argparse.ArgumentParser(prog='GoDaddyDNS Manager',
                                usage='%(prog)s [file] [options]',
                                description='Update GoDaddy DNS records from specified CSV')

parser.add_argument("-p", "--publickey", dest='PUBLIC_KEY', action='store', help="Specify Public Key")
parser.add_argument("-s", "--secretkey", dest='SECRET_KEY', action='store', help="Specify Private Key")
parser.add_argument("-c", "--csv", dest='csv', action='store', help="CSV file path")

args = parser.parse_args()

PUBLIC_KEY = args.PUBLIC_KEY
SECRET_KEY = args.SECRET_KEY

my_acct = Account(api_key=PUBLIC_KEY, api_secret=SECRET_KEY)
client = Client(my_acct)


file = open((args.csv), newline='')
reader = csv.reader(file)
next(reader)

for line in reader:
    ip, domain, name, recordtype = line
    client.update_record_ip(ip, domain, name, recordtype)
    print("Sucessfully updated",name+"."+domain+",",ip+",",recordtype,"Record")