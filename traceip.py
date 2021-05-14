#!/usr/bin/env python3

__author__ = 'Kwalix <hallerlucas@outlook.com>'
__version__ = '1.0.0'

from argparse import ArgumentParser
from colorama import init, Fore
import requests
import re

api_url = "https://api.ipgeolocationapi.com/geolocate"
y = Fore.YELLOW
r = Fore.RESET
red = Fore.RED
init(autoreset=True)
parser = ArgumentParser(description="Get or search an address IP")
parser.add_argument('-i', '--ip', action="store_true", help="Get your public IP address")
parser.add_argument('-t', '--trace', metavar="target", help="Trace an IP address")

args = parser.parse_args()


if not args.ip or args.trace:
    parser.error("No action requested, add -i or -t")

elif args.ip:
    resp = requests.get(api_url).json()
    data = dict(resp)
    # additionally get user public ip
    pub_ip = requests.get("https://api.ipify.org").text
    print(f'''{y}
    Result of :{r} {pub_ip} {y}
    Continent:{r} {data.get("continent")} {y}
    Country:{r} {data.get("name")} {y}
    Country code:{r} {data.get("alpha2")} {y}
    Latitude:{r} {data["geo"]["latitude"]} {y}
    Longitude:{r} {data["geo"]["longitude"]} {y}
    
''')

elif args.trace:
    if re.search("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$", args.trace):
        pass
    else:
        raise Exception(f"{red}You must enter a valid ipv4 address !")

    resp = requests.get(f'{api_url}/{args.trace}').json()
    data = dict(resp)
    print(f'''{y}
        Result of :{r} {args.trace} {y}
        Continent:{r} {data.get("continent")} {y}
        Country:{r} {data.get("name")} {y}
        Country code:{r} {data.get("alpha2")} {y}
        Latitude:{r} {data["geo"]["latitude"]} {y}
        Longitude:{r} {data["geo"]["longitude"]} {y}
''')
